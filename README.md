# ⚠️ IT Risk Assessment Framework

> **Enterprise IT risk assessment methodology and toolkit — validated across BFSI, US T1 Banking, Defence, Energy, and Technology sectors. COSO ERM, ISO 27005, and NIST RMF aligned.**

[![COSO ERM](https://img.shields.io/badge/COSO_ERM-2017_Aligned-orange?style=flat-square)](https://www.coso.org/)
[![ISO 27005](https://img.shields.io/badge/ISO_27005-2022_Aligned-green?style=flat-square)](https://www.iso.org/standard/80585.html)
[![NIST RMF](https://img.shields.io/badge/NIST_RMF-SP_800--37-blue?style=flat-square)](https://csrc.nist.gov/projects/risk-management)
[![FAIR](https://img.shields.io/badge/FAIR-Methodology_Reference-purple?style=flat-square)](https://www.fairinstitute.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

---

## 🎯 About

This framework provides a **complete, practical methodology** for assessing and managing IT risks across regulated industries. It bridges the gap between theory and practice — built from real risk programme implementations, not just framework text.

### What makes this different?
- **Sector-specific threat libraries** — banking threats aren't the same as OT/SCADA threats
- **Quantitative risk scoring** (FAIR-inspired) alongside qualitative methods
- **Ready-to-use Python tools** — heat maps, risk calculators, KRI dashboards
- **Regulatory alignment built in** — FFIEC, NERC CIP, HIPAA, DPDPA risk requirements addressed

---

## 📁 Structure

```
it-risk-assessment-framework/
├── methodology/
│   ├── risk-assessment-methodology.md    ← Full methodology (ISO 27005 / NIST aligned)
│   ├── threat-library-by-sector.md       ← Curated threats: BFSI, Defence, Energy, Health, Tech
│   └── risk-appetite-framework.md        ← Risk appetite & tolerance guidance
├── templates/
│   ├── risk-register-template.md         ← Enterprise risk register
│   ├── risk-assessment-worksheet.md      ← Per-asset assessment worksheet
│   └── risk-treatment-plan.md            ← Treatment options and tracking
├── scripts/
│   ├── risk_heatmap_advanced.py          ← Advanced dual-axis heatmap + bar chart
│   ├── risk_calculator.py                ← Quantitative risk scoring tool
│   └── kri_dashboard.py                  ← Key Risk Indicator dashboard
└── sector-guides/
    ├── bfsi-banking-risk-guide.md         ← FFIEC, OCC, RBI risk requirements
    ├── defence-risk-guide.md              ← NIST 800-171, CMMC, DRDO
    ├── energy-ot-risk-guide.md            ← NERC CIP, IEC 62443
    └── healthcare-risk-guide.md           ← HIPAA, HITRUST risk requirements
```

---

## 🔬 Risk Assessment Methodology Overview

```
STEP 1: SCOPE DEFINITION
  └── Asset identification, boundaries, threat landscape
  
STEP 2: ASSET VALUATION  
  └── CIA classification, business criticality rating
  
STEP 3: THREAT IDENTIFICATION
  └── Sector-specific threat library + MITRE ATT&CK mapping
  
STEP 4: VULNERABILITY ASSESSMENT
  └── Technical scan + procedural gap analysis
  
STEP 5: RISK CALCULATION
  └── Inherent risk = Likelihood × Impact
  └── Residual risk = Inherent risk × Control effectiveness
  
STEP 6: RISK EVALUATION
  └── Compare to risk appetite; prioritise treatment
  
STEP 7: RISK TREATMENT
  └── Mitigate / Transfer / Avoid / Accept
  
STEP 8: MONITORING & REVIEW
  └── KRIs, quarterly reviews, trigger-based reassessment
```

---

## 📊 Sector Risk Profiles

| Sector | Top Threats | Key Frameworks | Risk Focus |
|--------|-------------|---------------|------------|
| 🏦 US T1 Banking | BEC, Ransomware, Insider Threat, Supply Chain | FFIEC, NIST CSF, OCC | Systemic risk; customer impact |
| 🏦 India BFSI | APT, Fraud, Regulatory Non-compliance | RBI, SEBI, IRDAI | Regulatory risk; reputational |
| 🛡️ Defence | Nation-State APT, Espionage, Supply Chain | NIST 800-171, CMMC, DRDO | Data exfiltration; sabotage |
| ⚡ Energy/OT | ICS/SCADA attacks, Ransomware on OT, Physical | NERC CIP, IEC 62443 | Grid reliability; safety |
| 🏥 Healthcare | Ransomware, PHI breach, Medical device exploits | HIPAA, HITRUST | Patient safety; PHI exposure |
| 💻 Technology | Supply chain attacks, Cloud misconfig, API exploits | SOC 2, ISO 27001 | IP theft; data exposure |

---

## ✍️ Author

**Akshaya** | Sr. Manager, Risk & Compliance | ISO 27001 LA | CIAP (DRDO/MoD)

*"Every risk register I've built has been from scratch — no inherited templates, no existing baselines. This framework distils what actually works across real enterprise environments."*

📧 akshayshrm39@gmail.com | 🌐 [Akshaya-grc.netlify.app](https://Akshaya-grc.netlify.app)
