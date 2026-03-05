# Email_CS

## Tables

- [EmailProcess](#emailprocess)
- [EmailProcessType](#emailprocesstype)

## EmailProcess
**Physical table:** `OSUSR_tau_EmailProcess`  
**Description:** Auxiliar entity that contains all platform emails that will run through a BPT  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EMAILPROCESSTYPEID | int |  | YES | (NULL) |
| USERNAME | nvarchar | 150 | YES | ('') |
| DEVICE | nvarchar | 150 | YES | ('') |
| FEEDBACKMESSAGE | nvarchar | 2000 | YES | ('') |
| FILENAME | nvarchar | 250 | YES | ('') |
| FILECONTENT | nvarchar | 2000 | YES | ('') |
| FILETYPE | nvarchar | 150 | YES | ('') |
| REPORTEDCONTENTID | bigint |  | YES | ((0)) |
| REPORTEDUSERID | bigint |  | YES | ((0)) |
| REPORTEDUSERNAME | nvarchar | 150 | YES | ('') |
| REPORTEDBYID | bigint |  | YES | ((0)) |
| REPORTEDBYNAME | nvarchar | 150 | YES | ('') |
| REPORTEDBYEMAIL | nvarchar | 250 | YES | ('') |
| CLASSDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| REPORTEDCONTENTREFERENCEID | nvarchar | 150 | YES | ('') |
| COMPONENTNAME | nvarchar | 150 | YES | ('') |
| REPORTEDCONTENT | nvarchar | 2000 | YES | ('') |
| REPORTERNOTE | nvarchar | 2000 | YES | ('') |
| CUSTOMERID | bigint |  | YES | ((0)) |
| CUSTOMERNAME | nvarchar | 150 | YES | ('') |
| CONVERSATIONSID | nvarchar | 150 | YES | ('') |
| USERID | bigint |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | 2000 | YES | ('') |
| CUSTOMERPUBLICNAME | nvarchar | 150 | YES | ('') |
| SUBJECT | nvarchar | 500 | YES | ('') |
| BODY | nvarchar | -1 | YES | ('') |
| KEY | nvarchar | 150 | YES | ('') |
| FILESTORAGEID | bigint |  | YES | ((0)) |
| BUCKETTYPEID | bigint |  | YES | ((0)) |
| TIMERNAME | nvarchar | 150 | YES | ('') |
| MESSAGE | nvarchar | 2000 | YES | ('') |
| ISERROR | bit |  | YES | ((0)) |
| FROMEMAILADDRESS | nvarchar | 250 | YES | ('') |
| FROM | nvarchar | 250 | YES | ('') |
| TO | nvarchar | 250 | YES | ('') |
| CC | nvarchar | 250 | YES | ('') |
| BCC | nvarchar | 250 | YES | ('') |
| BASE64 | nvarchar | -1 | YES | ('') |
| GLOBALUSERFIRSTNAME | nvarchar | 150 | YES | ('') |
| GLOBALUSERLASTNAME | nvarchar | 150 | YES | ('') |
| USERHASROLEADMIN | bit |  | YES | ((0)) |
| USERHASROLEMANAGER | bit |  | YES | ((0)) |
| LOCATIONID | bigint |  | YES | ((0)) |
| INVOICEHEADERID | bigint |  | YES | ((0)) |
| TRANSACTIONID | bigint |  | YES | ((0)) |
| INVOICEID | nvarchar | 150 | YES | ('') |
| DISPUTEAMOUNT | decimal |  | YES | ((0)) |
| CHARGEBACKFEEAMOUNT | decimal |  | YES | ((0)) |
| EVIDENCEDUEBYDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TOUSERNAME | nvarchar | 150 | YES | ('') |
| ACCEPTEDBYUSERNAME | nvarchar | 150 | YES | ('') |
| ACCEPTEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| DISPUTEEVIDENCEID | bigint |  | YES | ((0)) |
| BILLINGCONTACTNAME | nvarchar | 150 | YES | ('') |
| ISFORREFUND | bit |  | YES | ((0)) |
| SUSPENSIONDAYOFMONTH | int |  | YES | ((0)) |
| LOCATIONIDS | nvarchar | 500 | YES | ('') |
| CLIENTCODE | nvarchar | 150 | YES | ('') |
| BRANCHCODE | nvarchar | 150 | YES | ('') |
| CCEMAILADDRESS | nvarchar | 250 | YES | ('') |
| ORDERID | nvarchar | 150 | YES | ('') |
| AMOUNTTOVOID | decimal |  | YES | ((0)) |
| TRANSACTIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| BANKRECEIPTID | nvarchar | 150 | YES | ('') |
| AMOUNTTOREFUND | decimal |  | YES | ((0)) |
| PAYMENTPROCESSORNAME | nvarchar | 50 | YES | ('') |
| MANDATEREQUESTLOOKUP | nvarchar | 150 | YES | ('') |
| EXCEPTIONTEXT | nvarchar | 2000 | YES | ('') |
| PAYEENAME | nvarchar | 250 | YES | ('') |
| INVOICENUMBER | nvarchar | 150 | YES | ('') |
| TRANSACTIONAMOUNT | decimal |  | YES | ((0)) |
| ERRORTEXT | nvarchar | 2000 | YES | ('') |
| SHAREDPAYMENTMETHODID | bigint |  | YES | ((0)) |
| STRIPESHAREDPAYMENTMETHODID | bigint |  | YES | ((0)) |
| DEFAULTSET | bit |  | YES | ((0)) |
| CLASSRESERVATIONID | bigint |  | YES | ((0)) |
| ISSESSIONEXPIRED | bit |  | YES | ((0)) |
| DURINGLATECANCELLATION | bit |  | YES | ((0)) |
| ADMINFIRSTNAME | nvarchar | 150 | YES | ('') |
| ATHLETEFIRSTNAME | nvarchar | 150 | YES | ('') |
| ATHLETELASTNAME | nvarchar | 150 | YES | ('') |
| ATHLETEID | bigint |  | YES | ((0)) |
| ATHLETEEMAILADDRESS | nvarchar | 250 | YES | ('') |
| ATHLETEPHONENUMBER | nvarchar | 20 | YES | ('') |
| MEMBERSHIPNAME | nvarchar | 150 | YES | ('') |
| MEMBERPLANID | bigint |  | YES | ((0)) |
| ONLINEMEMBERSHIPSALEID | bigint |  | YES | ((0)) |
| ATHLETEFULLNAME | nvarchar | 250 | YES | ('') |
| PROGRAMS | nvarchar | 500 | YES | ('') |
| LOCATIONS | nvarchar | 500 | YES | ('') |
| PAYMENTSCHEDULETEMPLATENAME | nvarchar | 150 | YES | ('') |
| INITIALCOMMITMENTLABEL | nvarchar | 150 | YES | ('') |
| INITIALCOSTLABEL | nvarchar | 150 | YES | ('') |
| RENEWCOMMITMENLABEL | nvarchar | 150 | YES | ('') |
| RENEWCOSTLABEL | nvarchar | 150 | YES | ('') |
| FORMATTEDSTARTDATE | nvarchar | 250 | YES | ('') |
| CLASSFORMATTEDSTARTDATE | nvarchar | 250 | YES | ('') |
| CLASSFORMATTEDSTARTTIME | nvarchar | 250 | YES | ('') |
| CLASSNAME | nvarchar | 150 | YES | ('') |
| LOCATION | nvarchar | 150 | YES | ('') |
| APPOOINTMENTFORMATTEDSTARTDA | nvarchar | 150 | YES | ('') |
| APPOINTMENTFORMATTEDSTARTTIM | nvarchar | 150 | YES | ('') |
| SERVICENAME | nvarchar | 150 | YES | ('') |
| PROVIDERNAME | nvarchar | 150 | YES | ('') |
| EMAILTEXT | nvarchar | -1 | YES | ('') |
| ONLINEMEMBERSHIPNAME | nvarchar | 150 | YES | ('') |
| SUBJECTLINE | nvarchar | 250 | YES | ('') |
| ISFROMMEMBERPLANCREATE | bit |  | YES | ((0)) |
| PAYMENTMETHODID | bigint |  | YES | ((0)) |
| SENDFROMUSERID | bigint |  | YES | ((0)) |
| SENDTOUSERID | bigint |  | YES | ((0)) |
| MANDRILLEVENT | nvarchar | 50 | YES | ('') |
| MANDRILLSUBJECT | nvarchar | 256 | YES | ('') |
| MANDRILLFAILEDEMAILADDRESS | nvarchar | 50 | YES | ('') |
| MANDRILLSTATE | nvarchar | 50 | YES | ('') |
| MANDRILLORIGINALSENDER | nvarchar | 250 | YES | ('') |
| MANDRILLTIMESTAMP | datetime |  | YES | ('1900-01-01 00:00:00') |
| MANDRILLMESSAGEID | nvarchar | 256 | YES | ('') |
| USERFIRSTNAME | nvarchar | 50 | YES | ('') |
| UNIQUEKEY | nvarchar | 50 | YES | ('') |
| PUBLICNAME | nvarchar | 50 | YES | ('') |
| TASKID | nvarchar | 50 | YES | ('') |
| ATTRIBUTES | nvarchar | 2000 | YES | ('') |

## EmailProcessType
**Physical table:** `OSUSR_tau_EmailProcessType`  
**Description:** contains all BPTs that can run asynchronously through the Email_AP  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
