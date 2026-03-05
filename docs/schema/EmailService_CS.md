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
**Physical table:** `OSUSR_cwj_DNSRecordStatus`  
**Description:** Contains possible statuses for DNS records  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## EmailServiceConfigurationSet
**Physical table:** `OSUSR_cwj_EmailServiceConfigurationSet`  
**Description:** Possible configuration set labels to use for the email service  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## EmailServiceEmail
**Physical table:** `OSUSR_cwj_EmailServiceEmail1`  
**Description:** Data related to sending an email through the email service (SES)  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## EmailServiceEmailBatch
**Physical table:** `OSUSR_cwj_EmailServiceEmailBatch1`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## EmailServiceEmailFeature
**Physical table:** `OSUSR_cwj_EmailServiceEmailFeature`  
**Description:** This table holds the possible features associated with Emails that are sent through the EmailService  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## EmailServiceSenderDomain
**Physical table:** `OSUSR_cwj_EmailServiceSenderDomain`  
**Description:** This table holds data related to verified domains in SES for the Email Service  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## EmailServiceSenderDomainStatus
**Physical table:** `OSUSR_cwj_EmailServiceSenderDomainStatus`  
**Description:** This table holds verification statuses for sender domains  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## EmailServiceSenderEmailAddress
**Physical table:** `OSUSR_cwj_EmailServiceSenderEmailAddress`  
**Description:** This table holds data related to verified email addresses in SES for the Email Service  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## EmailServiceSenderEmailAddressLocation
**Physical table:** `OSUSR_cwj_EmailServiceSenderEmailAddressLocation`  
**Description:** Represents the default email service email address for a location, if different than the email designated as IsSystem for the customer. If a record does not exist in this table for a given location, the EmailServiceSenderEmailAddress marked as IsSystem will be used  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## EmailServiceSenderEmailAddressStatus
**Physical table:** `OSUSR_cwj_EmailServiceSenderEmailAddressStatus`  
**Description:** This table holds statuses for sender email addresses  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## EmailServiceSenderRestrictedDomain
**Physical table:** `OSUSR_cwj_EmailServiceSenderRestrictedDomain1`  
**Description:** Domains that are restricted, in that customers cannot add them as identities. Use format label.* if domains might different end top level domains  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## TempInboxMigration
**Physical table:** `OSUSR_cwj_TempInboxMigration`  
**Description:** Temporary table to hold migration records for Inbox  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## TempLeadBackfillMigration
**Physical table:** `OSUSR_cwj_TempLeadBackfillMigration`  
**Description:** Table to restore records for replacing lead conversations for converted leads whose data needs to be backfilled in the comms service  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._
