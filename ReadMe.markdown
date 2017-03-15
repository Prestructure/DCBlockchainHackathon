Welcome to the MC/DC Encrypted Electronic Medical Records Authorization Audit System
====================

The MC/DC infrastructure leverages the ZCash blockchain to ensure medical record request metadata is private and secured. Provider to Provider as well as Patient-mediated exchange is authorized using the MC/DC PolicyService which receives and returns authorization requests through the ZCash blockchain transactions.  Only authorized parties (i.e. the Patient and the Provider requesting authorization) can audit their relevant transactions.        

We elected to use ZCash protocols because of unique features that provide anonymity for patients and providers as well as strong encryption for request metadata.  Simulating these benefits on other blockchains would require complex smart contracts.  While we do not store any patient data on any components of our system, the ZCash blockchain does securely maintain auditing and provenance information for authorizations.


Our Team:
---------------------

Adrian Diaz<br>
Andrew Baine<br>
Christian Duffus<br>
David Anderson<br>
Gabriel Baltazar Pérez<br>
Sergio Ceron<br>


Infrastructure:
---------------------

### Diagram
![Image of Components](/images/Diagram.png)


### PolicyServer User Interface
The PolicyServer has a user-interface for a Patient to create and manage their policies.  These policies may be set up by a patient's health insurance provider, or other authorized party.  These policies determine whether a request is approved or denied.
Additional functionality can be implemented to allow Patients to be notified, view and approve or deny Provider requests to access or share their medical information, but the current system relies on pre-defined policies that act on behalf of the patient.

### PolicyServer
The aforementioned policies reside within the Policy Server.  These policies are accessed via a REST API and can be edited by the Patient or an authorized agent acting on behalf of the patient, such as an insurance provider.

### Decision Engine
The Decision Engine detects, processes and responds to authorization requests coming in via the ZCash blockchain.  

### MC/DC Message Sender/Receiver
This component plays a key role in leveraging the built-in encryption and anonymity offered by ZCash.  It is able to both write and read to the blockchain.  In doing so it ensures that information requests are untraceable, obfuscating both Patient and Provider.  No third party will be able to read a request or measure the request activity attributable to a patient or a provider.





Resources Used:
---------------------

https://en.wikipedia.org/wiki/National_Provider_Identifier<br>
https://www.pubpub.org/pub/medrec





