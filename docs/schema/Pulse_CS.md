# Pulse_CS

## Tables

- [CustomerPulseSettings](#customerpulsesettings)
- [LocationPulseSettings](#locationpulsesettings)
- [PulseDevice](#pulsedevice)
- [PulseDeviceAssignHistory](#pulsedeviceassignhistory)
- [PulseDeviceGlobalUser](#pulsedeviceglobaluser)
- [PulseDeviceType](#pulsedevicetype)
- [PulseLoanerDeviceLocation](#pulseloanerdevicelocation)

## CustomerPulseSettings
**Physical table:** `OSUSR_k9a_TenantPulseSettings`  
**Description:** Pulse settings that apply to all locations of a Customer.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| SHOWDATAFORNEARBYUSERS | bit |  | YES | ((0)) |
| ENABLEAUTOMATICSIGNIN | bit |  | YES | ((0)) |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## LocationPulseSettings
**Physical table:** `OSUSR_k9a_LocationPulseSettings`  
**Description:** Contains the Pulse feature settings for a given location.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| LOCATIONID | int |  | NO |  |
| MYZONEFACILITYID | nvarchar | 50 | YES | ('') |
| MYZONEFACILITYNAME | nvarchar | 50 | YES | ('') |
| MYZONEAPIKEY | nvarchar | 50 | YES | ('') |
| MYZONESOFTWAREPASSWORD | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISBILLEDBYMYZONE | bit |  | YES | ((0)) |
| MYZONETEAMVIEWERID | nvarchar | 10 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PulseDevice
**Physical table:** `OSUSR_k9a_PulseDevice`  
**Description:** Represents a Pulse device to be used for heart rate monitoring.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| DEVICESERIAL | bigint |  | YES | ((0)) |
| PULSEDEVICETYPEID | int |  | YES | (NULL) |
| LASTUSEDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## PulseDeviceAssignHistory
**Physical table:** `OSUSR_k9a_PulseDeviceAssignHistory`  
**Description:** Represents the history of the belts assinged to a UserClassLogin.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| PULSEDEVICEID | bigint |  | YES | (NULL) |
| USERCLASSLOGINID | int |  | YES | (NULL) |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PulseDeviceGlobalUser
**Physical table:** `OSUSR_k9a_PulseDeviceGlobalUser`  
**Description:** Represents a Pulse Device that is tied to a Global User. The Pulse Device's represented here should have a Personal device type.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| PULSEDEVICEID | bigint |  | NO |  |
| GLOBALUSERID | int |  | YES | (NULL) |
| GUID | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EMAIL | nvarchar | 250 | YES | ('') |
| MYZONEFACILITYID | nvarchar | 50 | YES | ('') |
| MYZONEFACILITYNAME | nvarchar | 50 | YES | ('') |

## PulseDeviceType
**Physical table:** `OSUSR_k9a_PulseDeviceType`  
**Description:** The possible types of Pulse devices.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## PulseLoanerDeviceLocation
**Physical table:** `OSUSR_k9a_PulseLoanerDeviceLocation`  
**Description:** Represents a Pulse Device that is tied to a location. The Pulse Device's represented here should have a Loaner device type.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| PULSEDEVICEID | bigint |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| NICKNAME | nvarchar | 10 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |
