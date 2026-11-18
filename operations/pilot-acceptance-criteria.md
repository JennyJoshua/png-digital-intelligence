# Records-to-Reports Pilot Acceptance Criteria

**Product:** PROD-001 — Monthly Records-to-Reports  
**Purpose:** Ensure the pilot is properly scoped, safe to process and objectively complete.

## Gate 1 — Before accepting the job

All must be satisfied:

- [ ] A named customer organisation and authorised contact are identified.
- [ ] The customer confirms authority to share the supplied records and authorises the agreed processing.
- [ ] The reporting purpose, period, audience and required measures are written down.
- [ ] Input file count and total row count are within the agreed scope (initial offer: up to 3 files and 200 rows).
- [ ] Data fields and calculation rules are understood.
- [ ] Sensitive or unnecessary personal information has been removed or masked where possible.
- [ ] A secure, access-controlled transfer method is agreed; no confidential records are placed in the public GitHub repository.
- [ ] Price, payment arrangement, delivery date, one correction round and exclusions are agreed in writing.
- [ ] Customer understands that the service is not an audit or independent verification of source facts.

If any gate fails, do not begin processing. Clarify, reduce scope or decline the job.

## Gate 2 — Intake and data readiness

- [ ] Original input files are retained unchanged in the restricted working area.
- [ ] File names, formats, reporting period and receipt date are recorded.
- [ ] Source row counts are recorded.
- [ ] Required columns are present or missing fields are documented.
- [ ] Date, amount, category and status formats are understood.
- [ ] Potential duplicates are identified and not silently removed.
- [ ] Invalid, incomplete or ambiguous records are listed for clarification.
- [ ] Customer questions are resolved or explicitly carried as limitations.

If source data is materially incomplete or unreliable, tell the customer before proceeding with a revised scope or documented limitation.

## Gate 3 — Processing and quality control

- [ ] Every transformation is documented (for example, date normalisation or category mapping).
- [ ] Source values remain traceable to the cleaned records.
- [ ] No uncertain value is silently guessed or fabricated.
- [ ] Any excluded record has a documented reason.
- [ ] Input and output row counts reconcile, with exclusions and duplicates explained.
- [ ] Numeric totals are independently recalculated or checked using a second method.
- [ ] Formula cells and summary figures are checked.
- [ ] PDF totals match the final workbook.
- [ ] Reporting period and currency are clearly labelled.
- [ ] Assumptions, missing data and limitations are visible in the report.

## Gate 4 — Customer review and acceptance

- [ ] Draft workbook and report are supplied for the agreed review.
- [ ] Customer receives one consolidated correction round.
- [ ] Corrections are limited to errors or agreed scope clarifications; new analysis is separately quoted.
- [ ] Final files open correctly and are readable.
- [ ] Customer confirms receipt of the agreed outputs.
- [ ] Any unresolved issue is documented and disclosed.

## Completion definition

A pilot is complete when:

1. All agreed deliverables have been provided.
2. The checks in Gates 1–4 have passed or any exception has been explicitly accepted and documented.
3. The customer has confirmed receipt.
4. Actual effort, rework, costs and customer feedback have been recorded.
5. The agreed retention/deletion date is recorded.

## Stop-work triggers

Stop processing and contact the customer if:
- The customer cannot confirm authority to share the data.
- Unexpected sensitive personal information appears.
- The files appear corrupted, materially incomplete or outside scope.
- The requested work would require an audit opinion, legal/tax advice or unsupported certification.
- A security incident or unauthorised disclosure is suspected.

## Pilot scorecard

| Measure | Target |
|---|---|
| Delivery | Within agreed date |
| Calculation accuracy | All reported totals reconcile to source/cleaned data |
| Traceability | Every material transformation documented |
| Unresolved data issues | Disclosed, none concealed |
| Rework | No more than one consolidated correction round |
| Customer usefulness | Customer says the report supports a real task or decision |
| Commercial viability | Actual effort and costs support a sustainable fee |
| Repeat demand | Customer expresses a concrete willingness to purchase another cycle or refer a buyer |
