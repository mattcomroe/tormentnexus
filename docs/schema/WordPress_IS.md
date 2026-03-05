# WordPress_IS

## Tables

- [WordpressCom](#wordpresscom)
- [WordpressOrg](#wordpressorg)

## WordpressCom
**Physical table:** `OSUSR_M74_WORDPRESSCOM`  
**Description:** Table that contain the information of the blog connection throw the rest api and use the oauth 2  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CSRFTOKEN | nvarchar | 150 | YES | ('') |
| CODE | nvarchar | 250 | YES | ('') |
| TOKEN | nvarchar | 300 | YES | ('') |
| BLOG_ID | nvarchar | 50 | YES | ('') |
| BLOG_URL | nvarchar | 400 | YES | ('') |
| TOKEN_TYPE | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| PRODUCTID | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## WordpressOrg
**Physical table:** `OSUSR_M74_WORDPRESSORG`  
**Description:** Table that contain the information of the blog connection throw the rest api and use the oauth 1.0a  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| BLOGURL | nvarchar | 500 | YES | ('') |
| CONSUMERKEY | nvarchar | 50 | YES | ('') |
| CONSUMERSECRET | nvarchar | 50 | YES | ('') |
| TOKEN | nvarchar | 150 | YES | ('') |
| TOKENSECRET | nvarchar | 150 | YES | ('') |
| OAUTH_VERIFIER | nvarchar | 50 | YES | ('') |
| OAUTH_TOKEN | nvarchar | 150 | YES | ('') |
| OAUTH_TOKENSECRET | nvarchar | 150 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| PRODUCTID | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
