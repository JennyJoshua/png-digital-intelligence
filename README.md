# PNG Digital Intelligence

**Turning scattered information into valuable intelligence.**

PNG Digital Intelligence is a Papua New Guinea-focused data, research and digital knowledge services venture. It helps organisations turn scattered information, manual records and institutional knowledge into organised, reliable and usable digital assets.

## Initial service areas

1. **Data intelligence and research** — structured datasets, source-verified research, sector intelligence and data preparation.
2. **Business automation and reporting** — data cleaning, records-to-reports services, recurring management reports and practical workflow automation.
3. **Digital knowledge infrastructure** — document and archive preparation, searchable knowledge collections and retrieval-augmented generation (RAG) data preparation.

## First commercial service: Records-to-Reports

The initial offer is a fixed-scope monthly reporting service. The current pilot offer hypothesis is K500 for one reporting period, up to 3 input files and 200 rows, a clean Excel workbook, a concise PDF summary and one consolidated correction round. Price and scope may be adjusted as delivery experience develops.

### Product and operating documents

- [Service definition](products/records-to-reports.md)
- [Customer intake and scope template](operations/customer-intake-template.md)
- [Delivery standard operating procedure](operations/records-to-reports-sop.md)
- [Pilot acceptance criteria](operations/pilot-acceptance-criteria.md)
- [Customer discovery plan](operations/customer-discovery-plan.md) — retained as reference; the business has chosen to proceed with implementation rather than delay for interviews.
- [Synthetic sample report](samples/records-to-reports/sample-report.md)
- [Synthetic sample data](samples/records-to-reports/sample-data.csv)

### Report engine

The Python report engine accepts a transaction CSV and generates:
- An Excel workbook with Summary, Cleaned Records and Data Issues sheets.
- A PDF management summary with key totals and expense categories.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run against the fictional sample:

```bash
python src/report_engine.py samples/records-to-reports/sample-data.csv --output-dir output --period "1-30 June 2026" --organisation "Example Community Services"
```

Run automated tests:

```bash
python -m pytest -q
```

GitHub Actions runs the test suite when relevant engine, test, dependency or sample files change.

## Working principles

- Build reusable delivery systems and improve them through real operating experience.
- Use free or low-cost tools until customer revenue justifies upgrades.
- Verify source quality, dates, reuse rights and limitations before selling data.
- Never publish confidential client records or personal information in this public repository.
- Distinguish verified facts from estimates, assumptions and recommendations.
- Do not silently invent, alter or discard uncertain customer records.

## Repository purpose

This repository is the venture's business control and implementation workspace. It holds strategy, market evidence, product definitions, operating procedures, sample assets and software used to deliver services.

## Current stage

**Stage: first service implementation and operational readiness.** The report engine is an initial prototype tested against synthetic data. It is not yet a full accounting system or a secure customer-data platform.

## Important data-handling boundary

Use synthetic data in this public repository. Real customer files must be handled through an appropriate access-controlled transfer and working location under agreed written scope and authority. Do not put customer records, personal information, credentials or confidential documents in GitHub.

This service provides data organisation and management reporting; it does not provide an audit opinion, tax/legal advice or independent verification of the customer's source records.
