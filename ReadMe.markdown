Welcome to the MC/DC Encrypted Electronic Medical Records Authorization Audit System
====================

The MC/DC infrastructure leverages the ZCash blockchain to ensure medical record request metadata is private and secured. Provider to Provider as well as Patient-mediated exchange is authorized using the MC/DC PolicyService which receives and returns authorization requests through the ZCash blockchain transactions.  Only authorized parties (i.e. the Patient and the Provider requesting authorization) can audit their relevant transactions.        

We elected to use ZCash protocols because of unique features that provide anonymity for patients and providers as well as strong encryption for request metadata.  Simulating these benefits on other blockchains would require complex smart contracts.  While we do not store any patient data on any components of our system, the ZCash blockchain does securely maintain auditing information for requests and authorizations relating to sharing PHI.


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

### Audit Application
While third parties are not able to see the requests, the MC/DC system does allow for Patients and Providers to access an audit trail of their authorization requests and the respective responses.

### AuthClient & API
A service needs to handle the generation of requests to take action on Patient medical data, whether to send, receive, delete, store, copy the protected information.  Our aim is to provide an open API that allows any EMR system or Provider to easily confirm the actions they plan to take through the MC/DC system.  By engaging the Patient's policies in a secure way, Providers mitigate many risks relating to unauthorized release of PHI.


Sample MetaData:
---------------------

Sample metadata for Policies and authorization requests can be found under the [JSON directory](/JSON)



Resources Used:
---------------------

NPI https://en.wikipedia.org/wiki/National_Provider_Identifier<br>
CMS NPI https://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/downloads/NPIBooklet.pdf<br>
USPS Electronic Postmark® https://www.cccinnovationcenter.com/wp-content/uploads/2017/01/USPS-EPM-Service-SDK-Interface-Document-v1H.pdf<br>
MedRec https://www.pubpub.org/pub/medrec<br>





