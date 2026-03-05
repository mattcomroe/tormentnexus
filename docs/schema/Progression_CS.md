# Progression_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [AutoPromoteQueue](#autopromotequeue)
- [CertificatePlaceholders](#certificateplaceholders)
- [ClientProgression](#clientprogression)
- [ClientProgression_Archive](#clientprogression-archive)
- [ClientProgressionHistory](#clientprogressionhistory)
- [ClientProgressionHistory_Archive](#clientprogressionhistory-archive)
- [ClientTracker](#clienttracker)
- [ClientTracker_Archive](#clienttracker-archive)
- [ClientTrackerHistory](#clienttrackerhistory)
- [ClientTrackerHistory_Archive](#clienttrackerhistory-archive)
- [GlobalCertificateTemplate](#globalcertificatetemplate)
- [Level](#level)
- [Level_Archive](#level-archive)
- [LevelProgram](#levelprogram)
- [LevelProgram_Archive](#levelprogram-archive)
- [LevelVisualType](#levelvisualtype)
- [Progression](#progression)
- [Progression_Archive](#progression-archive)
- [Request](#request)
- [Request_File](#request-file)
- [RequestType](#requesttype)
- [StripeOption](#stripeoption)
- [Tracker](#tracker)
- [Tracker_Archive](#tracker-archive)
- [TrackerProgram](#trackerprogram)
- [TrackerProgram_Archive](#trackerprogram-archive)
- [TrackerTimeTypes](#trackertimetypes)
- [TrackerType](#trackertype)

## AsyncProcess
**Physical table:** `OSUSR_UQM_ASYNCPROCESS`  
**Description:** Auxiliar entity that contains all waivers asynchronous processes, which will run through the Progression_AP BPT process  

_Column definitions not found in schema export._

## AutoPromoteQueue
**Physical table:** `OSUSR_UQM_AUTOPROMOTEQUEUE`  
**Description:** Queue of Client Progressions to be auto-promoted  

_Column definitions not found in schema export._

## CertificatePlaceholders
**Physical table:** `OSUSR_UQM_CERTIFICATEPLACEHOLDERS`  
**Description:** Placeholder text for certificates with descriptions  

_Column definitions not found in schema export._

## ClientProgression
**Physical table:** `OSUSR_7G1_CLIENTPROGRESSION`  
**Description:** Data used for tracking a Client's Level and progress in a Progression  

_Column definitions not found in schema export._

## ClientProgression_Archive
**Physical table:** `OSUSR_UQM_CLIENTPROGRESSION_ARCHIVE`  
**Description:** Archive of Client Progression data  

_Column definitions not found in schema export._

## ClientProgressionHistory
**Physical table:** `OSUSR_7G1_CLIENTPROGRESSIONHISTORY`  
**Description:** Client Progression History is copied from ClientProgression when a Client's Level changes  

_Column definitions not found in schema export._

## ClientProgressionHistory_Archive
**Physical table:** `OSUSR_UQM_CLIENTPROGRESSIONHISTORY_ARCHIVE`  
**Description:** Archive of Client Progression History data  

_Column definitions not found in schema export._

## ClientTracker
**Physical table:** `OSUSR_UQM_CLIENTTRACKER`  
**Description:** A client's progress measured against a Tracker  

_Column definitions not found in schema export._

## ClientTracker_Archive
**Physical table:** `OSUSR_UQM_CLIENTTRACKER_ARCHIVE2`  
**Description:** Archive of ClientTracker data  

_Column definitions not found in schema export._

## ClientTrackerHistory
**Physical table:** `OSUSR_UQM_CLIENTTRACKERHISTORY`  
**Description:** A Client's Trackers related to Levels held in the past  

_Column definitions not found in schema export._

## ClientTrackerHistory_Archive
**Physical table:** `OSUSR_UQM_CLIENTTRACKERHISTORY_ARCHIVE2`  
**Description:** Archive of ClientTrackerHistory data  

_Column definitions not found in schema export._

## GlobalCertificateTemplate
**Physical table:** `OSUSR_UQM_GLOBALCERTIFICATETEMPLATE`  
**Description:** Stores wodify global certificate templates to federate to certificate templates across environments  

_Column definitions not found in schema export._

## Level
**Physical table:** `OSUSR_7G1_PROGRESSION`  
**Description:** Levels in a Progression  

_Column definitions not found in schema export._

## Level_Archive
**Physical table:** `OSUSR_UQM_LEVEL_ARCHIVE`  
**Description:** Archive of Level data for disabled Progressions or Customers  

_Column definitions not found in schema export._

## LevelProgram
**Physical table:** `OSUSR_UQM_LEVELPROGRAM1`  
**Description:** Associates a Level with an individual Program  

_Column definitions not found in schema export._

## LevelProgram_Archive
**Physical table:** `OSUSR_UQM_LEVELPROGRAM_ARCHIVE1`  

_Column definitions not found in schema export._

## LevelVisualType
**Physical table:** `OSUSR_UQM_LEVELVISUALTYPE1`  
**Description:** Options for visual representation of a level  

_Column definitions not found in schema export._

## Progression
**Physical table:** `OSUSR_7G1_PROGRESSIONSYSTEM`  
**Description:** Organized levels used to track Client progress in a program  

_Column definitions not found in schema export._

## Progression_Archive
**Physical table:** `OSUSR_UQM_PROGRESSION_ARCHIVE`  
**Description:** Archive of Progression data  

_Column definitions not found in schema export._

## Request
**Physical table:** `OSUSR_UQM_REQUEST`  
**Description:** Contains all Progression requests made by our Customers or Customer's Clients, that will run in the background  

_Column definitions not found in schema export._

## Request_File
**Physical table:** `OSUSR_UQM_REQUEST_FILE`  
**Description:** Entity to store temporarily files needed for processing a request.  

_Column definitions not found in schema export._

## RequestType
**Physical table:** `OSUSR_UQM_REQUESTTYPE`  
**Description:** Contains all request types that are possible to be made by our Customers or Customer's Clients, that will run in the background  

_Column definitions not found in schema export._

## StripeOption
**Physical table:** `OSUSR_UQM_STRIPEOPTION1`  
**Description:** Number of stripes available for the Color/Stripe LevelVisualType  

_Column definitions not found in schema export._

## Tracker
**Physical table:** `OSUSR_UQM_TRACKER`  
**Description:** Used to track or measure a requirements for progressing in a Level  

_Column definitions not found in schema export._

## Tracker_Archive
**Physical table:** `OSUSR_UQM_TRACKER_ARCHIVE2`  
**Description:** Archive of Tracker data  

_Column definitions not found in schema export._

## TrackerProgram
**Physical table:** `OSUSR_UQM_TRACKERPROGRAM`  
**Description:** Associates a Tracker with an individual Program  

_Column definitions not found in schema export._

## TrackerProgram_Archive
**Physical table:** `OSUSR_UQM_TRACKERPROGRAM_ARCHIVE`  
**Description:** Archive of TrackerProgram data  

_Column definitions not found in schema export._

## TrackerTimeTypes
**Physical table:** `OSUSR_UQM_TRACKERTIMETYPES`  
**Description:** Different time option types for the Time Tracker  

_Column definitions not found in schema export._

## TrackerType
**Physical table:** `OSUSR_UQM_TRACKERTYPE`  
**Description:** Defines the way a tracker is being measured  

_Column definitions not found in schema export._
