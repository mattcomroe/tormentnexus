# EmailService_CS

## Tables

- [DNSRecordStatus](#dnsrecordstatus)
- [EmailServiceConfigurationSet](#emailserviceconfigurationset)
- [EmailServiceEmail](#emailserviceemail)
- [EmailServiceEmailBatch](#emailserviceemailbatch)
- [EmailServiceEmailFeature](#emailserviceemailfeature)
- [EmailServiceSenderDomain](#emailservicesenderdomain)
- [EmailServiceSenderDomainStatus](#emailservicesenderdomainstatus)
- [EmailServiceSenderEmailAddress](#emailservicesenderemailaddress)
- [EmailServiceSenderEmailAddressLocation](#emailservicesenderemailaddresslocation)
- [EmailServiceSenderEmailAddressStatus](#emailservicesenderemailaddressstatus)
- [EmailServiceSenderRestrictedDomain](#emailservicesenderrestricteddomain)
- [TempInboxMigration](#tempinboxmigration)
- [TempLeadBackfillMigration](#templeadbackfillmigration)

## DNSRecordStatus
**Physical table:** `OSUSR_CWJ_DNSRECORDSTATUS`  
**Description:** Contains possible statuses for DNS records  

_Column definitions not found in schema export._

## EmailServiceConfigurationSet
**Physical table:** `OSUSR_CWJ_EMAILSERVICECONFIGURATIONSET`  
**Description:** Possible configuration set labels to use for the email service  

_Column definitions not found in schema export._

## EmailServiceEmail
**Physical table:** `OSUSR_CWJ_EMAILSERVICEEMAIL1`  
**Description:** Data related to sending an email through the email service (SES)  

_Column definitions not found in schema export._

## EmailServiceEmailBatch
**Physical table:** `OSUSR_CWJ_EMAILSERVICEEMAILBATCH1`  

_Column definitions not found in schema export._

## EmailServiceEmailFeature
**Physical table:** `OSUSR_CWJ_EMAILSERVICEEMAILFEATURE`  
**Description:** This table holds the possible features associated with Emails that are sent through the EmailService  

_Column definitions not found in schema export._

## EmailServiceSenderDomain
**Physical table:** `OSUSR_CWJ_EMAILSERVICESENDERDOMAIN`  
**Description:** This table holds data related to verified domains in SES for the Email Service  

_Column definitions not found in schema export._

## EmailServiceSenderDomainStatus
**Physical table:** `OSUSR_CWJ_EMAILSERVICESENDERDOMAINSTATUS`  
**Description:** This table holds verification statuses for sender domains  

_Column definitions not found in schema export._

## EmailServiceSenderEmailAddress
**Physical table:** `OSUSR_CWJ_EMAILSERVICESENDEREMAILADDRESS`  
**Description:** This table holds data related to verified email addresses in SES for the Email Service  

_Column definitions not found in schema export._

## EmailServiceSenderEmailAddressLocation
**Physical table:** `OSUSR_CWJ_EMAILSERVICESENDEREMAILADDRESSLOCATION`  
**Description:** Represents the default email service email address for a location, if different than the email designated as IsSystem for the customer. If a record does not exist in this table for a given location, the EmailServiceSenderEmailAddress marked as IsSystem will be used  

_Column definitions not found in schema export._

## EmailServiceSenderEmailAddressStatus
**Physical table:** `OSUSR_CWJ_EMAILSERVICESENDEREMAILADDRESSSTATUS`  
**Description:** This table holds statuses for sender email addresses  

_Column definitions not found in schema export._

## EmailServiceSenderRestrictedDomain
**Physical table:** `OSUSR_CWJ_EMAILSERVICESENDERRESTRICTEDDOMAIN1`  
**Description:** Domains that are restricted, in that customers cannot add them as identities. Use format label.* if domains might different end top level domains  

_Column definitions not found in schema export._

## TempInboxMigration
**Physical table:** `OSUSR_CWJ_TEMPINBOXMIGRATION`  
**Description:** Temporary table to hold migration records for Inbox  

_Column definitions not found in schema export._

## TempLeadBackfillMigration
**Physical table:** `OSUSR_CWJ_TEMPLEADBACKFILLMIGRATION`  
**Description:** Table to restore records for replacing lead conversations for converted leads whose data needs to be backfilled in the comms service  

_Column definitions not found in schema export._
