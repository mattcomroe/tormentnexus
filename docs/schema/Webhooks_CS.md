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
**Physical table:** `OSUSR_R5I_FAILEDREQUESTQUEUE1`  
**Description:** Entity to queue all the failed requests made for events (Zapier).  

_Column definitions not found in schema export._

## InboundRequestHistory
**Physical table:** `OSUSR_R5I_INBOUNDREQUESTHISTORY1`  
**Description:** Keeps the hashed content of recent requests, so that we can prevent duplicate requests from creating garbage in our database.  

_Column definitions not found in schema export._

## OutboundRequestHistory
**Physical table:** `OSUSR_R5I_OUTBOUNDREQUESTHISTORY1`  
**Description:** Keeps a record of CREATE events that were triggered, so that they aren't triggered again. This table was created as a hotfix for an issue where CREATE events were being triggered multiple times.  

_Column definitions not found in schema export._

## WebhookEventType
**Physical table:** `OSUSR_R5I_WEBHOOKEVENTTYPE1`  
**Description:** Entity containing the available event types to be used on the webhooks subscriptions.  

_Column definitions not found in schema export._

## WebhookSource
**Physical table:** `OSUSR_R5I_WEBHOOKSOURCE`  
**Description:** Source of webhook. Ex. Workato, Zapier, Customer, etc...  

_Column definitions not found in schema export._

## WebhookSubscription
**Physical table:** `OSUSR_R5I_WEBHOOKSUBSCRIPTION1`  
**Description:** Entity to store the webhooks subscriptions in the format "target_url": "https://.../<unique_target_url>".  

_Column definitions not found in schema export._

## WebhookSubscriptionEvent
**Physical table:** `OSUSR_R5I_WEBHOOKSUBSCRIPTIONEVENT1`  
**Description:** Relates subscriptions and events.  

_Column definitions not found in schema export._
