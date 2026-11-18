from pathlib import Path
from decimal import Decimal
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from report_engine import load_csv, money

SAMPLE = Path(__file__).resolve().parents[1] / "samples" / "records-to-reports" / "sample-data.csv"

def test_sample_totals_and_counts():
    data = load_csv(SAMPLE)
    assert len(data.records) == 10
    assert data.income_count == 3
    assert data.expense_count == 7
    assert data.income == Decimal("5500.00")
    assert data.expenses == Decimal("2575.00")
    assert data.income - data.expenses == Decimal("2925.00")

def test_money_format():
    assert money(Decimal("2925.00")) == "K2,925.00"

def test_duplicate_reference_is_flagged(tmp_path):
    p = tmp_path / "duplicate.csv"
    p.write_text("date,reference,description,category,type,amount_p_g_k,status\n"
                 "2026-01-01,A,one,Sales,Income,10,Confirmed\n"
                 "2026-01-02,A,two,Sales,Income,20,Confirmed\n", encoding="utf-8")
    data = load_csv(p)
    assert len(data.records) == 1
    assert len(data.issues) == 1
    assert "duplicate reference" in data.issues[0]


def test_second_synthetic_scenario_totals():
    sample = Path(__file__).resolve().parents[1] / "samples" / "records-to-reports" / "community-project-sample.csv"
    data = load_csv(sample)
    assert len(data.records) == 5
    assert data.income == Decimal("16500.00")
    assert data.expenses == Decimal("3510.00")
    assert data.income - data.expenses == Decimal("12990.00")

def test_invalid_date_and_negative_amount_are_flagged(tmp_path):
    p = tmp_path / "invalid.csv"
    p.write_text("date,reference,description,category,type,amount_p_g_k,status\n"
                 "not-a-date,A,one,Sales,Income,10,Confirmed\n"
                 "2026-01-02,B,two,Sales,Expense,-2,Paid\n", encoding="utf-8")
    import pytest
    with pytest.raises(ValueError, match="No valid records"):
        load_csv(p)

def test_missing_required_columns_are_rejected(tmp_path):
    p = tmp_path / "missing.csv"
    p.write_text("date,reference,amount_p_g_k\n2026-01-01,A,10\n", encoding="utf-8")
    import pytest
    with pytest.raises(ValueError, match="Missing required CSV columns"):
        load_csv(p)
