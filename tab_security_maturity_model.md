---
title: Security_Maturity_Model
displaytext: Security Maturity Model
layout: null
tab: true
order: 3
tags: cbas
---

# SAP Security Maturity Model

The CBAS - SAP Security Maturity Model (CBAS-SSMM) project allows organizations to determine their SAP security posture based on controls used to define a maturity level that organizations can maintain or adopt. This enables organizations to plan and enhance their security mechanisms when protecting SAP resources.


## Whats In It For Me (WIIFM)

The project intends to be used by different professionals:

- SAP Security Experts
- non-SAP Security Experts
- Consultants
- Auditors
- Advisors

1. The project helps operations, security, and audit teams assess, plan, and verify security controls that affect SAP implementations in their organizations.
2. Helps organizations determine their maturity in protecting their SAP applications.
3. Enables and supports organizations with implementing security controls that are required to protect their SAP applications.  

## Maturity Levels

We follow different methodologies and standards to define the different controls for each maturity level.

In our initial release, and for defining maturity level 1, we want to create a security baseline every organization __must__ maintain to secure SAP applications.

#### Maturity level 1:

The first maturity level is the initial baseline and derived from the below standards:

- SAP Security Baseline Template V2.1
- German Federal Office for Information Security - BSI 4.2 SAP ERP System
- German Federal Office for Information Security - BSI 4.6 SAP ABAP Programming
- SAP security white papers - used for critical areas missing in the security baseline template and BSI standards

## Controls

We aim to create controls in a structured, easy, and understandable way.

- Every control follows the same identification schema and structure
- Markdown language used for presenting the controls
- Excel tool to present maturity levels, risk areas represented by the [NO MONKEY Security Matrix](https://github.com/NO-MONKEY/CBAS-SAP/blob/master/No_MONKEY_Security_Matrix.md), and implementation status

#### Control Header:

- NIST Security Function
- NIST Category
- [IPAC Model](https://github.com/NO-MONKEY/CBAS-SAP/blob/master/No_MONKEY_Security_Matrix.md)
- SAP Technology
- Maturity Level
- Defender (People, Process, Technology)
- Control Prerequisite

*[Appendix A](https://github.com/NO-MONKEY/CBAS-SAP-SecurityMaturityModel/blob/master/Appendix/Appendix_A_Acronyms.md) lists the acronyms used in either the control header or the naming convention for controls.*

#### Control Structure:

- Description of the control
- Implementing the control
- Verification of the control
- References

#### Example:

<img src="assets/images/control.png"><br>

[![button](assets/images/cio.png)](https://github.com/NO-MONKEY/CBAS-SAP-SecurityMaturityModel)
