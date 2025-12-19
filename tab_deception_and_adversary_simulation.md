---
title: Deception_and_Adversary_Simulation
displaytext: Deception & Adversary Simulation
layout: null
tab: true
order: 1
tags: cbas
---
# Deception & Adversary Simulation
We create tools that emulate advanced threat tactics, techniques, and procedures (TTPs) in SAP systems, helping teams to stay one step ahead by visualizing attack patterns and preparing adaptive responses.

- [HoneySAP: SAP low-interaction honeypot](#honeysap-sap-low-interaction-honeypot)
- [pysap - Python library for crafting SAP's network protocols packets](#pysap---python-library-for-crafting-saps-network-protocols-packets)
- [SAPKiln](#sapkiln)
- [SAP Pentest Playbook](#sap-pentest-playbook)

## HoneySAP: SAP Low-interaction honeypot

[![Build and test HoneySAP](https://github.com/OWASP/HoneySAP/actions/workflows/build_and_test.yml/badge.svg)](https://github.com/OWASP/HoneySAP/actions/workflows/build_and_test.yml)

Version 0.1.2.dev0 (XXX 2022)

### Overview
HoneySAP is a low-interaction research-focused honeypot specific for SAP services. It's aimed at learn the techniques and motivations behind attacks against SAP systems.

[HoneySAP Project Page](https://github.com/OWASP/HoneySAP)

### Features
- Low-interaction honeypot for SAP services
- YAML and JSON-based configuration
- Pluggable datastore backend
- Modular services system
- Modular feeds system
- Console logging

## pysap - Python library for crafting SAP's network protocols packets
[![Build and test pysap](https://github.com/OWASP/pysap/workflows/Build%20and%20test%20pysap/badge.svg)](https://github.com/OWASP/pysap/actions?query=workflow%3A%22Build+and+test+pysap%22)
[![Latest Version](https://img.shields.io/pypi/v/pysap.svg)](https://pypi.python.org/pypi/pysap/)

Version 0.1.20.dev0 (XXX 2022)

### Overview
[SAP Netweaver](https://www.sap.com/platform/netweaver/index.epx) and [SAP HANA](https://www.sap.com/products/hana.html) are technology platforms for building and integrating SAP business applications. Communication between components uses different network protocols and some services and tools make use of custom file formats as well. While some of them are standard and well-known protocols, others are proprietaries and public information is generally not available.

pysap is an open source Python 2 library that provides modules for crafting and sending packets
using SAP's NI, Diag, Enqueue, Router, MS, SNC, IGS, RFC and HDB protocols. In addition, support for creating and parsing different proprietary file formats is included. The modules are built on top of [Scapy](https://scapy.net/) and are based on information acquired at researching the different protocols, file formats and services.

[pysap Project Page](https://github.com/OWASP/pysap)

### Features

* Dissection and crafting of the following network protocols:

    * SAP Network Interface (NI)
    * SAP Diag
    * SAP Enqueue
    * SAP Router
    * SAP Message Server (MS)
    * SAP Secure Network Connection (SNC)
    * SAP Internet Graphic Server (IGS)
    * SAP Remote Function Call (RFC)
    * SAP HANA SQL Command Network (HDB)

* Client interfaces for handling the following file formats:

    * SAP [SAR archive files](https://www.iana.org/assignments/media-types/application/vnd.sar)
    * SAP Personal Security Environment (PSE) files
    * SAP SSO Credential (Credv2) files
    * SAP Secure Storage in File System (SSFS) files

* Library implementing SAP's LZH and LZC compression algorithms.

* Automatic compression/decompression of payloads with SAP's algorithms.

* Client, proxy and server classes implemented for some of the protocols.

* Example scripts to illustrate the use of the different modules and protocols.

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

## SAP Pentest Playbook
[![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

The SAP Pentest Playbook is a community-driven, open-source resource that documents practical techniques, tools, and methodologies for conducting penetration tests on SAP systems and landscapes.
It is part of the [OWASP Core Business Application Security (CBAS)](https://owasp.org/www-project-core-business-application-security/) project and aims to serve as a single, reliable point of reference for SAP security professionals, pentesters, and researchers.

The Playbook consolidates distributed, often outdated or hard-to-find knowledge into a structured and up-to-date guide that covers:

- SAP-specific attack vectors
- Misconfigurations and “works as designed” behaviors that can be exploited
- Reconnaissance, exploitation, and post-exploitation techniques
- Detection and mitigation considerations

> [!WARNING]
> Disclaimer:
> Make sure you have the appropriate permissions to actively scan and test applications. Without doing so, you might face legal implications

[SAP Pentest Playbook Project Page](https://playbook.securitysilverbacks.com/)