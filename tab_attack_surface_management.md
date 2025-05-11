---
title: Attack_Surface_Management
displaytext: Attack Surface Management
layout: null
tab: true
order: 2
tags: cbas
---
# Attack Surface Management
Understanding your SAP attack surface enables you to better prioritze and apply security controls that help mature your SAP security posture. The below tools are designed to identify and provide you with possible threats and attack vectors that your SAP environment might posses.

- [SAP Attack Surface Discovery](#sap-attack-surface-discovery)
- [SAPKiln](#sapkiln)
- [sncscan](#sncscan)

## SAP Attack Surface Discovery

The project aims to help organizations and security professionals to identify and discover open SAP services through the use of different network scanning techniques. This allows individuals to further test these services for any potential threat that might affect SAP applications in their organizations.

[SAP Attack Surface Discovery Project Page](https://github.com/SecuritySilverbacks/SAP-AttackSurfaceDiscovery)

## SAPKiln
![SAPiln Version](https://img.shields.io/badge/1.0-0000?label=Version)

The world :earth_americas: of SAP is very vast and unique. SAP has multiple products to tackle various problems as well as multiple technology platforms such as NetWeaver etc. SAPKiln is an open-source GUI tool :computer: designed to empower security researchers in conducting efficient auditing and penetration testing of SAP systems through SAP Logon/GUI (desktop application). It caters to both experienced SAP professionals and those unfamiliar with the SAP environment, as it streamlines the process of performing security checks with a user-friendly interface:sparkles:.

Powered :battery: by saplogon.exe and SAP scripting in its backend, SAPKiln executes automated checks in the SAP system. The current version (v1.0) boasts a comprehensive array of over 70+ checks :exclamation: divided into 10 modules. Beyond its built-in checks, SAPKiln provides flexibility with dynamic checks, accommodating custom user inputs. By automating security assessments, SAPKiln effectively bridges the knowledge gap for security researchers :cop: compared to SAP domain experts:eyeglasses:.

[SAPKiln Project Page](https://github.com/OWASP/SAPKiln)

### Modules Included
* Attempt Login with Default SAP Credentials
* Enumerate for Accessible T-Codes
* Enumerate for Accessible Tables
* Enumerate for Usage of SAP_ALL Profile
* Enumerate Password Policies
* Enumerate Weak Password Hashes (Users)
* Enumerate Weak Password Hashes (Hashes)
* OS Commands Execution - RSBDCOS0
* OS Commands Execution - SAPXPG
* Enumerate Instances for Lateral Movement

## sncscan
Tool for analyzing SAP Secure Network Communications (SNC).

### How to use?
In its current state, `sncscan` can be used to read the SNC configurations for SAP Router and DIAG (SAP GUI) connections. The implementation for the SAP RFC protocol is currently in development.

[sncscan Project Page](https://github.com/usdAG/sncscan)
