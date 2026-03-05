-- Run this against the OSLogDB database
SELECT
    t.TABLE_SCHEMA,
    t.TABLE_NAME,
    c.COLUMN_NAME,
    c.DATA_TYPE,
    c.CHARACTER_MAXIMUM_LENGTH,
    c.IS_NULLABLE,
    c.COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.TABLES t
JOIN INFORMATION_SCHEMA.COLUMNS c
    ON t.TABLE_NAME = c.TABLE_NAME
    AND t.TABLE_SCHEMA = c.TABLE_SCHEMA
WHERE t.TABLE_TYPE = 'BASE TABLE'
AND t.TABLE_NAME IN (
  'oslog_Cyclic_Job',
  'oslog_Cyclic_Job_Previous',
  'oslog_Error',
  'oslog_Error_Previous',
  'oslog_Extension',
  'oslog_Extension_Previous',
  'oslog_General',
  'oslog_General_Previous',
  'oslog_Int_Detail',
  'oslog_Int_Detail_Previous',
  'oslog_Integration',
  'oslog_Integration_Previous',
  'oslog_MR_Detail',
  'oslog_MR_Detail_Previous',
  'oslog_Parameter',
  'oslog_RequestEvent',
  'oslog_RequestEvent_Previous',
  'oslog_Screen',
  'oslog_Screen_Previous',
  'oslog_SrvAPI',
  'oslog_SrvAPI_Detail',
  'oslog_SrvAPI_Detail_Previous',
  'oslog_SrvAPI_Previous',
  'oslog_Web_Reference',
  'oslog_Web_Reference_Previous',
  'oslog_Web_Service',
  'oslog_Web_Service_Previous',
  'oslog_mobile_request',
  'oslog_mobile_request_Previous'
)
ORDER BY t.TABLE_NAME, c.ORDINAL_POSITION;
