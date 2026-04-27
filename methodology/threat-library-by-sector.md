# Threat Library by Sector

> Curated threat catalogue organised by industry sector with MITRE ATT&CK mapping. Use this during Step 3 (Threat Identification) of the risk assessment process.

---

## 🏦 BFSI — US T1 Banking Threat Library

| Threat ID | Threat | Vector | Likelihood | Impact | MITRE ATT&CK |
|-----------|--------|--------|:---:|:---:|-------------|
| BNK-T01 | Business Email Compromise (BEC) | Social engineering / email | High | Critical | T1566, T1534 |
| BNK-T02 | Ransomware — targeted attack | Phishing + lateral movement | High | Critical | T1486, T1490 |
| BNK-T03 | Insider threat — data exfiltration | Privileged access abuse | Medium | Critical | T1052, T1041 |
| BNK-T04 | Supply chain compromise | Third-party software/vendor | Medium | Critical | T1195, T1199 |
| BNK-T05 | Account takeover (ATO) | Credential stuffing / phishing | High | High | T1110, T1539 |
| BNK-T06 | ATM/POS malware | Physical + network | Low | High | T1543 |
| BNK-T07 | SWIFT network fraud | Credential theft + SWIFT access | Low | Critical | T1078 |
| BNK-T08 | DDoS attack on banking services | Botnet / amplification | Medium | High | T1498, T1499 |
| BNK-T09 | Core banking system exploit | Unpatched vulnerabilities | Low | Critical | T1190 |
| BNK-T10 | Regulatory data breach (PII/PCI) | Multiple vectors | Medium | Critical | T1530, T1567 |
| BNK-T11 | Mobile banking app compromise | Malicious app / MITM | Medium | High | T1417 |
| BNK-T12 | Third-party API abuse | Insecure API integration | Medium | High | T1190 |

**Banking-Specific Risk Amplifiers:**
- Interconnected financial systems (contagion risk)
- 24/7 operational requirements (minimal maintenance windows)
- Regulatory reporting obligations (adds reputational risk to every incident)
- SWIFT connectivity (nation-state targeting)

---

## 🛡️ Defence / Government Threat Library

| Threat ID | Threat | Actor | Likelihood | Impact | MITRE ATT&CK |
|-----------|--------|-------|:---:|:---:|-------------|
| DEF-T01 | Nation-state APT — espionage | Nation-state | High | Critical | Multiple |
| DEF-T02 | CUI/classified data exfiltration | Insider / APT | High | Critical | T1052, T1048 |
| DEF-T03 | Supply chain hardware implant | Nation-state | Low | Critical | T1195.003 |
| DEF-T04 | Spear-phishing of senior officials | APT groups | High | Critical | T1566.001 |
| DEF-T05 | Zero-day exploit on classified systems | APT | Medium | Critical | T1203 |
| DEF-T06 | Insider sabotage | Malicious insider | Low | Critical | T1485, T1561 |
| DEF-T07 | Watering hole attack | APT | Medium | High | T1189 |
| DEF-T08 | Social engineering of cleared personnel | APT / foreign intelligence | Medium | Critical | T1598 |
| DEF-T09 | Adversarial AI attacks on defence systems | Nation-state | Low | Critical | Novel TTPs |
| DEF-T10 | ITAR/export control violation | Insider / third party | Low | Critical | — |

**Key Threat Actors (Defence Sector):**
- APT29 (Cozy Bear) — Russia — Espionage
- APT41 (Double Dragon) — China — Espionage + Financial
- Lazarus Group — DPRK — Financial + Sabotage
- Charming Kitten (APT35) — Iran — Espionage

---

## ⚡ Energy & OT/SCADA Threat Library

| Threat ID | Threat | Vector | Likelihood | Impact | Notes |
|-----------|--------|--------|:---:|:---:|-------|
| ENR-T01 | Ransomware on IT/OT network | Phishing + IT-OT pivot | High | Critical | Colonial Pipeline model |
| ENR-T02 | SCADA/ICS targeted attack | Direct access / IT pivot | Medium | Critical | Triton/TRISIS precedent |
| ENR-T03 | Unauthorised remote access to OT | VPN compromise, T1133 | Medium | Critical | Common post-COVID |
| ENR-T04 | PLC/RTU firmware manipulation | Physical + logical | Low | Critical | Stuxnet precedent |
| ENR-T05 | IT-OT boundary breach | Inadequate segmentation | High | Critical | Most common path |
| ENR-T06 | Vendor remote access abuse | Third-party OT access | Medium | High | NERC CIP-005 risk |
| ENR-T07 | Physical attack on grid assets | Nation-state / terrorism | Low | Critical | CIP-006 relevance |
| ENR-T08 | GPS spoofing affecting timing | Radio frequency attack | Low | High | Affects grid synchronisation |
| ENR-T09 | Supply chain — counterfeit ICS components | Nation-state | Low | Critical | CIP-013 relevance |

**OT-Specific Considerations:**
- Safety implications: Some attacks can cause physical harm (TRITON targeted safety systems)
- Legacy systems: Many ICS run on unsupported OS (Windows XP, etc.)
- Patch cycles: OT patching may require plant shutdowns — months of planning
- Air gaps: Often not true air gaps; historian servers typically bridge IT/OT

---

## 🏥 Healthcare Threat Library

| Threat ID | Threat | Vector | Likelihood | Impact | Regulatory Impact |
|-----------|--------|--------|:---:|:---:|-----------------|
| HLT-T01 | Ransomware on hospital systems | Phishing + RDP | High | Critical | HIPAA breach + patient safety |
| HLT-T02 | PHI data breach (bulk exfiltration) | Insider / external | Medium | Critical | HIPAA, HHS OCR notification |
| HLT-T03 | Medical device exploit | Network / physical | Low | Critical | FDA 21 CFR, patient safety |
| HLT-T04 | EHR system compromise | Credential theft | Medium | High | HIPAA §164.312 |
| HLT-T05 | Telemedicine platform attack | API / app exploit | Medium | High | HIPAA, patient privacy |
| HLT-T06 | Business Associate (BA) breach | BA system compromise | Medium | High | HIPAA BAA obligations |
| HLT-T07 | Healthcare sector-specific phishing | COVID themes, Rx fraud | High | Medium | HIPAA breach notification |

---

## 💻 Technology / Cloud Threat Library

| Threat ID | Threat | Vector | Likelihood | Impact | Notes |
|-----------|--------|--------|:---:|:---:|-------|
| TEC-T01 | Cloud misconfiguration | Developer error | High | High | S3 buckets, storage ACLs |
| TEC-T02 | CI/CD pipeline compromise | Supply chain | Medium | Critical | SolarWinds, 3CX model |
| TEC-T03 | API security exploit | Insecure APIs | High | High | OWASP API Top 10 |
| TEC-T04 | Container escape / k8s exploit | Cloud-native | Medium | High | CISA k8s guidance |
| TEC-T05 | Credential theft (cloud IAM) | Phishing, SSRF | High | Critical | Primary cloud attack vector |
| TEC-T06 | Cryptojacking | Exposed compute | Medium | Medium | Cost + performance impact |
| TEC-T07 | Open-source dependency attack | Supply chain | Medium | High | Log4Shell, XZ Utils |
| TEC-T08 | Prompt injection / AI system abuse | LLM-enabled apps | High | Medium | Emerging threat vector |

---

*Threat library updated: 2024 | Sources: MITRE ATT&CK, CISA advisories, sector ISACs, threat intelligence reports*
