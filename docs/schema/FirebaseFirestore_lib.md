# FirebaseFirestore_lib

## Tables

- [ChangeType](#changetype)
- [FBAuthenticationType](#fbauthenticationtype)
- [FBGlobalQueryCallbackType](#fbglobalquerycallbacktype)
- [WhereClauseDataType](#whereclausedatatype)
- [WhereClauseOperator](#whereclauseoperator)

## ChangeType
**Physical table:** `OSUSR_0T1_CHANGETYPE`  
**Description:** The ChangeType static entity categorizes the types of changes that can occur to Firestore documents. It is crucial for identifying the nature of the change during Firestore data synchronization. The records include:  Add: Indicates that a new document has been added to the Firestore collection. All: Used to denote any and all changes, including additions, deletions, and modifications. Removed: Specifies that a document has been removed from the Firestore collection.  

_Column definitions not found in schema export._

## FBAuthenticationType
**Physical table:** `OSUSR_0T1_FBAUTHENTICATIONTYPE`  
**Description:** The FBAuthenticationType static entity defines the available methods of user authentication within the Firestore integration. This entity supports multiple authentication strategies, enhancing security and flexibility. The records include:  None: No authentication is applied. Anonymous: Users are authenticated anonymously, without personal identifiers. EmailAndPassword: Standard email and password authentication. CustomToken: Authentication using a custom secure token. OAuthProvider: Authentication through an OAuth provider for integrating with services like Google, Facebook, etc.  

_Column definitions not found in schema export._

## FBGlobalQueryCallbackType
**Physical table:** `OSUSR_0T1_FBGLOBALQUERYCALLBACKTYPE`  
**Description:** The FBGlobalQueryCallbackType static entity lists the types of global query callback responses that an application can handle, providing structured handling of Firestore query events. The records include:  DocumentReceived ("onDocReceived"): Indicates that a document has been successfully received as a result of a query. FailedInitialization ("onFailedInitialization"): Indicates a failure in initializing a query or a query-related process.  

_Column definitions not found in schema export._

## WhereClauseDataType
**Physical table:** `OSUSR_0T1_WHERECLAUSEDATATYPE`  
**Description:** The WhereClauseDataType static entity specifies the data types that can be associated with values in Firestore queries, ensuring that comparisons and operations on data fields are accurately performed. This entity is used in the WhereClause data structure to define the type of the value being compared in a query condition, ensuring that data integrity and type consistency are maintained across Firestore operations.  

_Column definitions not found in schema export._

## WhereClauseOperator
**Physical table:** `OSUSR_0T1_WHERECLAUSEOPERATOR`  
**Description:** The WhereClauseOperator static entity specifies the operators that can be used to form conditions in Firestore queries. This entity facilitates the creation of dynamic and complex query operations by providing a variety of operator types suited to different filtering needs. The records include:  ArrayContains: Used to check if an array field contains a specific element. Represented as "array-contains" in Firestore queries. ArrayContainsAny: Allows checking if any element of a specified set is present in an array field. Represented as "array-contains-any". Equal: Checks if a field is equal to a specified value. Represented by "=" in queries. GreaterThan: Used to filter documents where a specified field is greater than a provided value. Represented by ">". GreaterThanOrEqual: Filters documents where a field is greater than or equal to a specified value. Represented as ">=". In: Checks if a field's value matches any value in a provided array. Represented as "in". LessThan: Used for filtering documents where a field is less than a specified value. Represented by "<". LessThanOrEqual: Filters documents where a field is less than or equal to a specified value. Represented as "<=". NotEqual: Filters documents where a field does not equal a specified value. Represented as "!=". NotIn: Used to filter documents where a field's value does not match any value in a provided array. Represented as "not-in".  

_Column definitions not found in schema export._
