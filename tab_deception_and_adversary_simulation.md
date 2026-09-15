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
- [SAP Pentest Playbook](#sap-pentest-playbook)
- [SAPMAP](#sapmap)

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

## SAPMAP

Like BloodHound for Active Directory, but for SAP.

SAPMAP is an offensive security and attack-path mapping tool for SAP landscapes - similar in concept to BloodHound for Active Directory.

The goal of SAPMAP is to make complex SAP trust relationships and attack paths visible. It discovers SAP systems, maps connections between them, identifies potential weaknesses, and helps security teams understand how an attacker could move through an SAP landscape.

Rather than looking at individual SAP systems in isolation, SAPMAP focuses on the entire landscape and the relationships between SAP applications, infrastructure, credentials, RFC connections, SAP BTP, SAP Cloud Connector, and the underlying operating systems.

### What SAPMAP includes

* SAP landscape discovery and enumeration - identify SAP systems, services, clients, databases, SAPControl endpoints, and exposed interfaces.
* Attack-path visualization - graph SAP systems and their RFC/trust relationships to highlight possible lateral movement paths.
* Security configuration testing - identify weak Gateway, Message Server, authentication, and trust configurations.
* Exploitation capabilities - validate real-world SAP vulnerabilities and misconfigurations during authorized security assessments.
* Credential and Secure Store analysis - analyze SAP credentials, RFC destinations, Secure Stores, password hashes, and authentication material.
* Lateral movement - follow RFC, SSH, SAP BTP, Cloud Connector, and other trust relationships across the landscape.
* Privilege escalation and post-exploitation - assess what an attacker could achieve after compromising an SAP system.
* SAP BTP and hybrid landscape support - map attack paths between cloud and on-premise SAP environments.
* Business impact analysis - demonstrate how technical weaknesses could lead to access to sensitive SAP data and business processes.
* Detection and defense guidance - provide defenders with indicators, detection ideas, and hardening recommendations for the techniques used by SAPMAP.

[SAPMAP Project Page](https://github.com/SecuritySilverbacks/www-project-core-business-application-security)