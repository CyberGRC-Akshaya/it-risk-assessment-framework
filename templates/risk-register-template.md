# Enterprise IT Risk Register

**Organisation:** [NAME]  
**Risk Owner:** [CISO / Risk Manager]  
**Version:** [X.X]  
**Last Updated:** [DATE]  
**Next Review:** [DATE + 3 months]

---

## Risk Scoring Matrix

**Likelihood Scale:**
| Score | Level | Definition |
|-------|-------|-----------|
| 5 | Almost Certain | Expected to occur in most circumstances (>80% in 12 months) |
| 4 | Likely | Will probably occur in most circumstances (60–80%) |
| 3 | Possible | Might occur at some time (40–60%) |
| 2 | Unlikely | Could occur at some time (10–40%) |
| 1 | Rare | May only occur in exceptional circumstances (<10%) |

**Impact Scale:**
| Score | Level | Definition |
|-------|-------|-----------|
| 5 | Critical | Catastrophic operational/financial/regulatory/reputational impact |
| 4 | Major | Significant impact requiring executive response; regulatory notification likely |
| 3 | Moderate | Noticeable impact; manageable with existing resources |
| 2 | Minor | Limited impact; handled at operational level |
| 1 | Negligible | Minimal impact; no significant business effect |

**Risk Score = Likelihood × Impact**
| Score Range | Rating | Colour |
|------------|--------|--------|
| 20–25 | Critical | 🔴 |
| 12–19 | High | 🟠 |
| 6–11 | Medium | 🟡 |
| 1–5 | Low | 🟢 |

---

## Risk Register

| Risk ID | Risk Description | Threat Source | Asset/Process | L | I | Inherent Score | Existing Controls | Control Rating | Residual Score | Risk Level | Treatment | Owner | Review Date | Status |
|---------|-----------------|--------------|---------------|---|---|---------------|------------------|---------------|---------------|-----------|-----------|-------|-------------|--------|
| **RISK-001** | Ransomware attack encrypts production systems causing extended outage and potential data loss | External Threat Actor | All IT systems, data | 4 | 5 | **20 🔴** | EDR, email filtering, backups, segmentation | Partial | **12 🟠** | High | Mitigate: Immutable backups, IR playbook, tabletop exercise | CISO | Q1 | Open |
| **RISK-002** | Privileged account compromise leads to lateral movement and data exfiltration | External / Insider | IAM, production systems | 3 | 5 | **15 🟠** | PAM vault, MFA, monitoring | Partial | **9 🟡** | Medium | Mitigate: PAM JIT, quarterly privilege review | IT Mgr | Q1 | In progress |
| **RISK-003** | Third-party vendor breach exposes customer PII through shared integration | External (Vendor) | Customer data, APIs | 3 | 5 | **15 🟠** | Vendor assessments, DPA, monitoring | Partial | **9 🟡** | Medium | Mitigate: Enhanced vendor monitoring, supply chain assessment | Risk Mgr | Q2 | Open |
| **RISK-004** | Business Email Compromise results in fraudulent wire transfer | External (Social Eng.) | Finance systems, email | 4 | 4 | **16 🔴** | Email security, training, approval workflows | Adequate | **8 🟡** | Medium | Mitigate: Dual-control for transfers, enhanced email filtering | CFO | Q1 | Open |
| **RISK-005** | Unpatched critical vulnerability exploited before patch cycle | External Threat Actor | All internet-facing systems | 4 | 4 | **16 🔴** | Vulnerability scanning, patch management | Partial | **12 🟠** | High | Mitigate: 72-hour critical patch SLA, compensating controls | IT Mgr | Monthly | Open |
| **RISK-006** | Data breach of personal data leads to GDPR/DPDPA regulatory action | External / Insider | Customer PII, databases | 3 | 5 | **15 🟠** | DLP, encryption, access controls | Adequate | **6 🟡** | Medium | Mitigate: DSPM tools, quarterly access review | DPO | Q2 | Open |
| **RISK-007** | Insider threat — disgruntled employee exfiltrates intellectual property | Insider | Source code, IP, client data | 2 | 5 | **10 🟡** | DLP, UBA, background checks, monitoring | Partial | **6 🟡** | Medium | Mitigate: UBA/UEBA tool, post-termination monitoring | HR + CISO | Q2 | Open |
| **RISK-008** | Cloud misconfiguration exposes sensitive data publicly | Internal (Error) | Cloud storage, APIs | 4 | 4 | **16 🔴** | CSPM tool, cloud security policy | Partial | **8 🟡** | Medium | Mitigate: CSPM enforcement, Infrastructure as Code | Cloud Eng | Q1 | In progress |
| **RISK-009** | Loss of critical system availability exceeds RTO due to BCP failure | Natural disaster / Technical | Production systems | 2 | 5 | **10 🟡** | BCP, DR plan, offsite backup | Adequate | **4 🟢** | Low | Accept: Maintain current controls; annual DR test | IT Mgr | Annual | Open |
| **RISK-010** | Change management failure introduces defect causing regulatory non-compliance | Internal (Process) | Production applications | 3 | 4 | **12 🟠** | CAB, change controls, testing | Adequate | **4 🟢** | Low | Mitigate: Automated regression testing pipeline | IT Mgr | Q2 | Open |

---

## Risk Treatment Summary

| Treatment | Count | Total Budget Required |
|-----------|-------|----------------------|
| Mitigate | [X] | $[X] |
| Transfer (Insurance) | [X] | $[X] premium |
| Accept | [X] | — |
| Avoid | [X] | — |

---

## Key Risk Indicators (KRI) Dashboard

| KRI | Metric | Green | Amber | Red | Current |
|-----|--------|-------|-------|-----|---------|
| Critical vuln patch time | Avg days to patch critical CVE | <3 days | 3–7 days | >7 days | |
| Access review completion | % completed on time | >95% | 85–95% | <85% | |
| Security incidents | P1/P2 per month | 0 | 1 | >1 | |
| Phishing click rate | % staff clicking test phishing | <3% | 3–10% | >10% | |
| Overdue CARs | # open corrective actions past due | 0 | 1–3 | >3 | |
| Vendor assessments overdue | # Tier 1 vendors overdue | 0 | 1 | >1 | |

---

*Risk Register Owner: [CISO/Risk Manager] | Reviewed by Risk Committee: [DATE] | Next review: [DATE]*
