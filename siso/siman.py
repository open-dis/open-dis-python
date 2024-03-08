import enum


"""
22 SIMAN
22.1 Reason [UID 67]
Value Description
0 Other
1 Recess
2 Termination
3 System Failure
4 Security Violation
5 Entity Reconstitution
6 Stop for reset
7 Stop for restart
8 Abort Training Return to Tactical Operations
22.2 Frozen Behavior [UID 68]
Any individual bit set to one indicates that the simulation application is to continue the corresponding
activity in the frozen state; a bit set to zero indicates that the activity is to cease in the frozen state.
Name Bits Description Reference
Run Simulation Clock 0 Describes whether a simulation application should run the internal simulation clock or not
Transmit Updates 1 Describes whether a simulation application should transmit
updates and interactions or not
Process Updates 2 Describes whether a simulation application should update
simulation models of other entities via received updates or
interactions
22.3 Acknowledge Flag [UID 69]
Value Description
1 Create Entity
2 Remove Entity
3 Start/Resume
4 Stop/Freeze
5 Transfer Ownership
22.4 Response Flag [UID 70]
Value Description
0 Other
1 Able to comply
2 Unable to comply
3 Pending Operator Action
22.5 Action ID [UID 71]
Value Description
0 Other
1 Local storage of the requested information
2 Inform SM of event "ran out of ammunition"
3 Inform SM of event "killed in action"
4 Inform SM of event "damage"
5 Inform SM of event "mobility disabled"
6 Inform SM of event "fire disabled"
7 Inform SM of event "ran out of fuel"
8 Recall checkpoint data
9 Recall initial parameters
10 Initiate tether-lead
11 Initiate tether-follow
12 Unthether
13 Initiate service station resupply
14 Initiate tailgate resupply
15 Initiate hitch lead
16 Initiate hitch follow
17 Unhitch
18 Mount
19 Dismount
20 Start DRC (Daily Readiness Check)
21 Stop DRC
22 Data Query
23 Status Request
24 Send Object State Data
25 Reconstitute
26 Lock Site Configuration
27 Unlock Site Configuration
28 Update Site Configuration
29 Query Site Configuration
30 Tethering Information
31 Mount Intent
33 Accept Subscription
34 Unsubscribe
35 Teleport entity
36 Change aggregate state
37 Request Start PDU
38 Wakeup get ready for initialization
39 Initialize internal parameters
40 Send plan data
41 Synchronize internal clocks
42 Run
43 Save internal parameters
44 Simulate malfunction
45 Join exercise
46 Resign exercise
47 Time advance
100 TACCSF LOS Request-Type 1
101 TACCSF LOS Request-Type 2
4303 Airmount Mount Request
4304 Airmount Dismount Request
4305 Airmount Information Request
22.6 Request Status [UID 72]
Value Description
0 Other
1 Pending
2 Executing
3 Partially Complete
4 Complete
5 Request rejected
6 Retransmit request now
7 Retransmit request later
8 Invalid time parameters
9 Simulation time exceeded
10 Request done
100 TACCSF LOS Reply-Type 1
101 TACCSF LOS Reply-Type 2
201 Join Exercise Request Rejected
22.7 Event Type [UID 73]
Value Description
0 Other
2 Ran Out of Ammunition
3 Killed in Action (KIA)
4 Damage
5 Mobility Disabled
6 Fire Disabled
7 Ran Out of Fuel
8 Entity Initialization
9 Request for Indirect Fire or CAS Mission
10 Indirect Fire or CAS Fire
11 Minefield Entry
12 Minefield Detonation
13 Vehicle Master Power On
14 Vehicle Master Power Off
15 Aggregate State Change Requested
16 Prevent Collision / Detonation
17 Ownership Report
18 Radar Perception
19 Detect
22.8 Required Reliability Service [UID 74]
This field specifies the 8-bit enumeration for the Required Reliability Service field in the Create Entity-R,
Remove Entity-R, Start/Resume-R, Stop/Freeze-R, Action Request-R, Data Query-R, Set Data-R, Data-
R, Record Query-R, Set Record-R, and Record-R PDUs.
Value Description
0 Acknowledged
1 Unacknowledged
22.9 Record-R Event Type [UID 333]
Value Description
0 Other
22.10 Record Query-R Event Type [UID 334]
Value Description
0 Periodic
1 Internal Entity State Data
"""
# []