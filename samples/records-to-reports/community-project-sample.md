# Synthetic Scenario: Community Project Reporting

This second example represents a fictional community organisation's single-month project register. It is provided only to exercise the reporting engine against a different dataset and must not be represented as real client work.

- Reporting period: July 2026
- Valid records: 5
- Income entries: 2 totalling K16,500.00
- Expense entries: 3 totalling K3,510.00
- Net listed income less expenses: K12,990.00

The figures are simple arithmetic over the supplied fictional rows. They do not establish that funding was received, expenses were authorised, or the source register is complete. Run it with:

```bash
python src/report_engine.py samples/records-to-reports/community-project-sample.csv --output-dir output/community-project --period "1-31 July 2026" --organisation "Example Community Project"
```
