# ZSandboxDonFireBase

## Tables

- [ClassSync](#classsync)

## ClassSync
**Physical table:** `OSUSR_v0m_ClassSync`  
**Description:** Recrords are created here and locked to prevent multi/signin and signout across devcies  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CLASSID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
