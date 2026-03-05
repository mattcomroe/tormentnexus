# AndroidPermissionsPlugin

## Tables

- [AndroidPermission](#androidpermission)

## AndroidPermission
**Physical table:** `OSUSR_IAY_ANDROIDPERMISSION`  
**Description:** Contains the different types of android permissions.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| PERMISSIONNAME | nvarchar | 50 | YES | ('') |
| ANDROIDPERMISSION | nvarchar | 100 | NO |  |
| HASPERMISSION | bit |  | YES | ((0)) |
