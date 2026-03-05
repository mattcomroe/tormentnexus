# WodifyFirebaseCloudMessagingPlugin

## Tables

- [ActionEvent](#actionevent)
- [ActionType](#actiontype)
- [Platform](#platform)
- [TimeUnit](#timeunit)

## ActionEvent
**Physical table:** `OSUSR_zfb_ActionEvent`  
**Description:** The event of the custom action. Can have the values of: - internalRoute: the action type that triggers an event to be handled by the app, similar to a default or silent notification press. - appRoute: the action type that routes the user to another app. - webRoute: the action type that opens a given URL in the device’s browser.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ActionType
**Physical table:** `OSUSR_zfb_ActionType`  
**Description:** The type of the custom action. It can be:    - standard, an action item with the standard appearance  - destructive, an action item with red as the text color. Only applicable for iOS.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## Platform
**Physical table:** `OSUSR_zfb_Platform`  
**Description:** The identifiers for the SendToPlatform parameter.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## TimeUnit
**Physical table:** `OSUSR_zfb_TimeUnit`  

_Table not present in the dev environment — schema unavailable. May exist in production only._
