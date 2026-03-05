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
**Physical table:** `OSUSR_uqm_AsyncProcess`  
**Description:** Auxiliar entity that contains all waivers asynchronous processes, which will run through the Progression_AP BPT process  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## AutoPromoteQueue
**Physical table:** `OSUSR_uqm_AutoPromoteQueue`  
**Description:** Queue of Client Progressions to be auto-promoted  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## CertificatePlaceholders
**Physical table:** `OSUSR_uqm_CertificatePlaceholders`  
**Description:** Placeholder text for certificates with descriptions  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ClientProgression
**Physical table:** `OSUSR_7g1_ClientProgression`  
**Description:** Data used for tracking a Client's Level and progress in a Progression  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ClientProgression_Archive
**Physical table:** `OSUSR_uqm_ClientProgression_Archive`  
**Description:** Archive of Client Progression data  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ClientProgressionHistory
**Physical table:** `OSUSR_7g1_ClientProgressionHistory`  
**Description:** Client Progression History is copied from ClientProgression when a Client's Level changes  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ClientProgressionHistory_Archive
**Physical table:** `OSUSR_uqm_ClientProgressionHistory_Archive`  
**Description:** Archive of Client Progression History data  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ClientTracker
**Physical table:** `OSUSR_uqm_ClientTracker`  
**Description:** A client's progress measured against a Tracker  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ClientTracker_Archive
**Physical table:** `OSUSR_uqm_ClientTracker_Archive2`  
**Description:** Archive of ClientTracker data  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ClientTrackerHistory
**Physical table:** `OSUSR_uqm_ClientTrackerHistory`  
**Description:** A Client's Trackers related to Levels held in the past  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ClientTrackerHistory_Archive
**Physical table:** `OSUSR_uqm_ClientTrackerHistory_Archive2`  
**Description:** Archive of ClientTrackerHistory data  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## GlobalCertificateTemplate
**Physical table:** `OSUSR_uqm_GlobalCertificateTemplate`  
**Description:** Stores wodify global certificate templates to federate to certificate templates across environments  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Level
**Physical table:** `OSUSR_7g1_Progression`  
**Description:** Levels in a Progression  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Level_Archive
**Physical table:** `OSUSR_uqm_Level_Archive`  
**Description:** Archive of Level data for disabled Progressions or Customers  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LevelProgram
**Physical table:** `OSUSR_uqm_LevelProgram1`  
**Description:** Associates a Level with an individual Program  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LevelProgram_Archive
**Physical table:** `OSUSR_uqm_LevelProgram_Archive1`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LevelVisualType
**Physical table:** `OSUSR_uqm_LevelVisualType1`  
**Description:** Options for visual representation of a level  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Progression
**Physical table:** `OSUSR_7g1_ProgressionSystem`  
**Description:** Organized levels used to track Client progress in a program  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Progression_Archive
**Physical table:** `OSUSR_uqm_Progression_Archive`  
**Description:** Archive of Progression data  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Request
**Physical table:** `OSUSR_uqm_Request`  
**Description:** Contains all Progression requests made by our Customers or Customer's Clients, that will run in the background  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Request_File
**Physical table:** `OSUSR_uqm_Request_File`  
**Description:** Entity to store temporarily files needed for processing a request.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## RequestType
**Physical table:** `OSUSR_uqm_RequestType`  
**Description:** Contains all request types that are possible to be made by our Customers or Customer's Clients, that will run in the background  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## StripeOption
**Physical table:** `OSUSR_uqm_StripeOption1`  
**Description:** Number of stripes available for the Color/Stripe LevelVisualType  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Tracker
**Physical table:** `OSUSR_uqm_Tracker`  
**Description:** Used to track or measure a requirements for progressing in a Level  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Tracker_Archive
**Physical table:** `OSUSR_uqm_Tracker_Archive2`  
**Description:** Archive of Tracker data  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## TrackerProgram
**Physical table:** `OSUSR_uqm_TrackerProgram`  
**Description:** Associates a Tracker with an individual Program  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## TrackerProgram_Archive
**Physical table:** `OSUSR_uqm_TrackerProgram_Archive`  
**Description:** Archive of TrackerProgram data  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## TrackerTimeTypes
**Physical table:** `OSUSR_uqm_TrackerTimeTypes`  
**Description:** Different time option types for the Time Tracker  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## TrackerType
**Physical table:** `OSUSR_uqm_TrackerType`  
**Description:** Defines the way a tracker is being measured  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._
