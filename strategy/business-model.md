# Business Model — PNG Digital Intelligence

**Version:** 1.0  
**Status:** Working hypothesis  
**Date:** 18 November 2026

## Value proposition

We help PNG organisations make better use of information they already hold or can lawfully access. We organise, verify, analyse and maintain information, then deliver it in practical formats such as clean datasets, reports, searchable collections and repeatable workflows.

## Customer segments and likely needs

| Segment | Potential problem | Possible service |
|---|---|---|
| SMEs | Records spread across spreadsheets, PDFs and paper | Data cleaning, monthly reporting |
| Schools and training institutions | Student, attendance, assessment and resource records | Records conversion and management reports |
| NGOs and development organisations | Project documents, indicators and reporting burdens | Data preparation, evidence packs, reporting |
| Contractors and suppliers | Difficulty tracking opportunities and preparing documentation | Tender-readiness research and document checklists |
| Consultants and researchers | Time-consuming secondary research and source preparation | Verified datasets and research support |
| Public institutions | Dispersed documents and institutional knowledge | Archive inventories and searchable knowledge collections |

These are hypotheses to test through customer conversations.

## Revenue streams

1. **Project fees:** data cleaning, conversions, research briefs, archive preparation and report production.
2. **Recurring services:** monthly reporting, scheduled data updates, monitoring, knowledge-base maintenance and support.
3. **Reusable products:** templates, sector datasets, structured source collections and workflow packages, subject to reuse rights.
4. **Licensing:** access to maintained collections or tools under clearly defined terms.

## Delivery model

A typical engagement should define:
- Customer problem and intended decision or workflow.
- Source data supplied by the customer or lawfully accessed.
- Scope, exclusions and data-quality limitations.
- Deliverable format and acceptance criteria.
- Delivery date, revision allowance and price.
- Confidentiality, retention, access and deletion arrangements.
- Ownership and permitted reuse of deliverables.

## First pilot hypothesis: Records-to-Reports

Offer a tightly scoped conversion of one customer-provided reporting period into:
- A cleaned and documented spreadsheet.
- A concise PDF summary report.
- A short list of data-quality issues and recommended next steps.

An initial K500 pilot price was previously considered as a test price, not a verified PNG market rate. Validate willingness to pay before publishing a standard price. Define record limits, complexity, turnaround and revision scope before quoting.

## Pricing approach

Use fixed prices for well-defined packages and custom quotes for uncertain or complex work. Price should account for:
- Time required for extraction, cleaning, checking and analysis.
- Data volume and complexity.
- Source access and licensing costs.
- Security and confidentiality requirements.
- Revision and support obligations.
- Ongoing update frequency.

Any earlier illustrative price ranges are planning assumptions only. Record actual quotes, objections, wins and losses in the pricing register once customer evidence exists.

## Cost and technology principles

Start with GitHub for versioned code and non-sensitive documentation, Python for repeatable processing, pandas for data work, openpyxl for spreadsheets, and ReportLab for PDF output. Use GitHub Actions for suitable scheduled or event-driven automation.

GitHub is not a customer database or secure document vault. Never commit identifiable customer records, credentials, private source documents or confidential reports to this public repository. Select secure, access-controlled storage for client work.

Use hosted databases, paid APIs or paid infrastructure only when a real customer requirement and budget justify them.

## Key risks

- Customers may not pay for data work they currently perform manually.
- Existing local providers may already meet the need.
- Third-party data may not be reusable commercially.
- Poor source quality can undermine trust.
- Custom projects may consume too much time to scale.
- Confidential data may be exposed if storage and access are poorly designed.

## Validation gates

Do not build a subscription platform until:
1. A clearly defined customer problem is confirmed by multiple target customers.
2. At least one customer pays for a pilot or provides a credible purchase commitment.
3. Delivery effort and costs are measured.
4. The data can be lawfully sourced and maintained.
5. A repeatable workflow can be demonstrated.
