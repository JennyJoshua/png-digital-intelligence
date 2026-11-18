"""Generate an Excel workbook and PDF summary from a transaction CSV.

Use only synthetic or properly authorised data. This is not accounting software,
an audit tool, or independent verification of source records.
"""
from __future__ import annotations
import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from xml.sax.saxutils import escape

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

REQUIRED = ("date", "reference", "description", "category", "type", "amount_p_g_k", "status")

@dataclass(frozen=True)
class Record:
    date: date
    reference: str
    description: str
    category: str
    kind: str
    amount: Decimal
    status: str

@dataclass
class ReportData:
    records: list[Record]
    issues: list[str]
    income: Decimal
    expenses: Decimal
    income_count: int
    expense_count: int
    expense_by_category: dict[str, Decimal]

def load_csv(path: Path) -> ReportData:
    records, issues, seen_refs = [], [], set()
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = set(reader.fieldnames or [])
        missing = [field for field in REQUIRED if field not in headers]
        if missing:
            raise ValueError("Missing required CSV columns: " + ", ".join(missing))
        for line_no, row in enumerate(reader, start=2):
            try:
                ref = (row.get("reference") or "").strip()
                if not ref:
                    raise ValueError("reference is blank")
                if ref in seen_refs:
                    raise ValueError(f"duplicate reference {ref!r}; record not included")
                parsed_date = date.fromisoformat((row.get("date") or "").strip())
                amount = Decimal((row.get("amount_p_g_k") or "").strip()).quantize(Decimal("0.01"))
                if amount < 0:
                    raise ValueError("amount cannot be negative")
                kind = (row.get("type") or "").strip().title()
                if kind not in {"Income", "Expense"}:
                    raise ValueError("type must be Income or Expense")
                category = (row.get("category") or "").strip()
                if not category:
                    raise ValueError("category is blank")
                records.append(Record(parsed_date, ref, (row.get("description") or "").strip(),
                                      category, kind, amount, (row.get("status") or "").strip()))
                seen_refs.add(ref)
            except (ValueError, InvalidOperation) as exc:
                issues.append(f"Line {line_no}: {exc}")
    if not records:
        raise ValueError("No valid records found; correct the input before generating a report")
    income = sum((r.amount for r in records if r.kind == "Income"), Decimal("0.00"))
    expenses = sum((r.amount for r in records if r.kind == "Expense"), Decimal("0.00"))
    by_category = defaultdict(lambda: Decimal("0.00"))
    for record in records:
        if record.kind == "Expense":
            by_category[record.category] += record.amount
    return ReportData(records, issues, income, expenses,
                      sum(r.kind == "Income" for r in records),
                      sum(r.kind == "Expense" for r in records), dict(by_category))

def money(value: Decimal) -> str:
    return f"K{value:,.2f}"

def build_workbook(data: ReportData, output: Path, period: str) -> None:
    wb = Workbook()
    summary = wb.active
    summary.title = "Summary"
    for row in [
        ["Records-to-Reports | Management Summary"],
        ["Reporting period", period],
        ["Valid records", len(data.records)],
        ["Income entries", data.income_count],
        ["Total income (PGK)", float(data.income)],
        ["Expense entries", data.expense_count],
        ["Total expenses (PGK)", float(data.expenses)],
        ["Net listed income less expenses (PGK)", float(data.income-data.expenses)],
        ["Data issues requiring attention", len(data.issues)],
        [],
        ["Expense category", "Amount (PGK)"],
    ]:
        summary.append(row)
    for category, amount in sorted(data.expense_by_category.items()):
        summary.append([category, float(amount)])
    records_ws = wb.create_sheet("Cleaned Records")
    records_ws.append(list(REQUIRED))
    for r in data.records:
        records_ws.append([r.date.isoformat(), r.reference, r.description, r.category,
                           r.kind, float(r.amount), r.status])
    issues_ws = wb.create_sheet("Data Issues")
    issues_ws.append(["Issue"])
    for issue in data.issues:
        issues_ws.append([issue])
    for ws in wb.worksheets:
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions if ws.max_row > 1 else "A1:A1"
        for cell in ws[1]:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill("solid", fgColor="17365D")
            cell.alignment = Alignment(vertical="center")
        for col in ws.columns:
            width = min(max(max(len(str(c.value or "")) for c in col) + 2, 12), 48)
            ws.column_dimensions[get_column_letter(col[0].column)].width = width
    output.parent.mkdir(parents=True, exist_ok=True)
    wb.save(output)

def build_pdf(data: ReportData, output: Path, period: str, organisation: str) -> None:
    styles = getSampleStyleSheet()
    story = [
        Paragraph("Monthly Management Summary", styles["Title"]),
        Paragraph(f"Organisation: {escape(organisation)}", styles["Normal"]),
        Paragraph(f"Reporting period: {escape(period)} | Currency: PGK", styles["Normal"]),
        Spacer(1, 8*mm),
        Paragraph("Executive summary", styles["Heading2"]),
        Paragraph(
            f"The supplied register contains {len(data.records)} valid records: "
            f"{data.income_count} income entries totalling {money(data.income)} and "
            f"{data.expense_count} expense entries totalling {money(data.expenses)}. "
            f"The net of listed income less listed expenses is {money(data.income-data.expenses)}.",
            styles["BodyText"]),
        Spacer(1, 5*mm), Paragraph("Key figures", styles["Heading2"])
    ]
    rows = [["Indicator", "Value"], ["Valid records", str(len(data.records))],
            ["Income", money(data.income)], ["Expenses", money(data.expenses)],
            ["Net listed income less expenses", money(data.income-data.expenses)],
            ["Data issues", str(len(data.issues))]]
    table = Table(rows, colWidths=[105*mm, 55*mm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#17365D")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), .4, colors.grey), ("PADDING", (0,0), (-1,-1), 6)
    ]))
    story.extend([table, Spacer(1, 5*mm), Paragraph("Expense categories", styles["Heading2"])])
    cat_rows = [["Category", "Amount"]] + [[escape(k), money(v)] for k, v in sorted(data.expense_by_category.items())]
    cat_table = Table(cat_rows, colWidths=[105*mm, 55*mm])
    cat_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#17365D")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), .4, colors.grey), ("PADDING", (0,0), (-1,-1), 6)
    ]))
    story.extend([cat_table, Spacer(1, 5*mm), Paragraph("Data limitations", styles["Heading2"]),
                  Paragraph("This summary reports only the records supplied. It is not an audit, bank "
                            "reconciliation, or independent verification that all transactions are complete or valid.",
                            styles["BodyText"])])
    if data.issues:
        story.append(Paragraph("Input issues requiring attention", styles["Heading2"]))
        for issue in data.issues:
            story.append(Paragraph(escape(issue), styles["BodyText"]))
    output.parent.mkdir(parents=True, exist_ok=True)
    SimpleDocTemplate(str(output), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm,
                      topMargin=18*mm, bottomMargin=18*mm).build(story)

def generate(input_csv: Path, output_dir: Path, period: str, organisation: str) -> ReportData:
    data = load_csv(input_csv)
    build_workbook(data, output_dir / "management-report.xlsx", period)
    build_pdf(data, output_dir / "management-summary.pdf", period, organisation)
    return data

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("output"))
    parser.add_argument("--period", required=True, help="e.g. 1-30 June 2026")
    parser.add_argument("--organisation", default="Customer organisation")
    args = parser.parse_args()
    data = generate(args.input_csv, args.output_dir, args.period, args.organisation)
    print(f"Generated {len(data.records)} valid records; {len(data.issues)} issue(s).")
    print(f"Income: {money(data.income)} | Expenses: {money(data.expenses)} | Net: {money(data.income-data.expenses)}")
    if data.issues:
        print("Review the Data Issues sheet and do not deliver until issues are resolved or disclosed.")

if __name__ == "__main__":
    main()
