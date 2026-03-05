# FirebaseCloudMessagingPlugin

## Tables

- [ActionEvent](#actionevent)
- [ActionType](#actiontype)
- [Platform](#platform)
- [TimeUnit](#timeunit)

## ActionEvent
**Physical table:** `OSUSR_938_ActionEvent1`  
**Description:** The event of the custom action. Can have the values of: - internalRoute: the action type that triggers an event to be handled by the app, similar to a default or silent notification press. - appRoute: the action type that routes the user to another app. - webRoute: the action type that opens a given URL in the device’s browser.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ActionType
**Physical table:** `OSUSR_938_ActionType1`  
**Description:** The type of the custom action. It can be:    - standard, an action item with the standard appearance  - destructive, an action item with red as the text color. Only applicable for iOS.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## Platform
**Physical table:** `OSUSR_938_Platform1`  
**Description:** The identifiers for the SendToPlatform parameter.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## TimeUnit
**Physical table:** `OSUSR_938_TimeUnit1`  

_Table not present in the dev environment — schema unavailable. May exist in production only._
