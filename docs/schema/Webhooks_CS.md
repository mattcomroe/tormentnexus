# Webhooks_CS

## Tables

- [FailedRequestQueue](#failedrequestqueue)
- [InboundRequestHistory](#inboundrequesthistory)
- [OutboundRequestHistory](#outboundrequesthistory)
- [WebhookEventType](#webhookeventtype)
- [WebhookSource](#webhooksource)
- [WebhookSubscription](#webhooksubscription)
- [WebhookSubscriptionEvent](#webhooksubscriptionevent)

## FailedRequestQueue
**Physical table:** `OSUSR_r5i_FailedRequestQueue1`  
**Description:** Entity to queue all the failed requests made for events (Zapier).  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## InboundRequestHistory
**Physical table:** `OSUSR_r5i_InboundRequestHistory1`  
**Description:** Keeps the hashed content of recent requests, so that we can prevent duplicate requests from creating garbage in our database.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## OutboundRequestHistory
**Physical table:** `OSUSR_r5i_OutboundRequestHistory1`  
**Description:** Keeps a record of CREATE events that were triggered, so that they aren't triggered again. This table was created as a hotfix for an issue where CREATE events were being triggered multiple times.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## WebhookEventType
**Physical table:** `OSUSR_r5i_WebhookEventType1`  
**Description:** Entity containing the available event types to be used on the webhooks subscriptions.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## WebhookSource
**Physical table:** `OSUSR_r5i_WebhookSource`  
**Description:** Source of webhook. Ex. Workato, Zapier, Customer, etc...  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## WebhookSubscription
**Physical table:** `OSUSR_r5i_WebhookSubscription1`  
**Description:** Entity to store the webhooks subscriptions in the format "target_url": "https://.../<unique_target_url>".  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## WebhookSubscriptionEvent
**Physical table:** `OSUSR_r5i_WebhookSubscriptionEvent1`  
**Description:** Relates subscriptions and events.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._
