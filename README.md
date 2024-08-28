# khalil-illumio-takehome-assignment
Take home assessment for Illumio.

## Assumptions
1. Only version 2 flow logs are supported.
2. Flow logs are stored in a plain txt file.
3. Lookup table is stored in a csv file.
4. All elements in flow log entry map to correct field. 
   1. Ex: 2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
         1. 49153 is port, 6 is protocol
5. Only store first 10 (0-10) Assigned Internet Protocol Numbers
6. Built on Python3.

## Steps to Run
1. Add lookup table csv file to project (Sample file provided named `lookup-table.csv`).
2. Add flow log txt file to project (Sample file provided named` flow_logs.txt`).
3. Run `python parse_flow_log.py` on Windows or `python3 parse_flow_log.py` on other OS's.
4. ` output.txt `file will then be created with necessary data.
## Description 

Write a program that can parse a file containing flow log data and maps each row to a tag based on a lookup table. The lookup table is defined as a csv file, and it has 3 columns, dstport,protocol,tag.   The dstport and protocol combination decide what tag can be applied. **NOTE: Only version 2 is supported.**
Sample flow logs are included in flow_logs.txt. Lookup table is also included, but can be replaced with your own custom file.
Just change the names in parse_flow_log.py.
The program will generate an output file similar to the following: 

Count of matches for each tag, sample o/p shown below 
 

Tag Counts: 

Tag,Count 

sv_P2,1 

sv_P1,2 

sv_P4,1 

email,3 

Untagged,9          

Count of matches for each port/protocol combination 
Port/Protocol Combination Counts: 

 Port,Protocol,Count 

22,tcp,1 

23,tcp,1 

25,tcp,1 

110,tcp,1 

143,tcp,1 

443,tcp,1 

993,tcp,1 

1024,tcp,1 

49158,tcp,1 

80,tcp,1 

 
## Requirement details 

1. Input file as well as the file containing tag mappings are plain text (ascii) files  
2. The flow log file size can be up to 10 MB 
3. The lookup file can have up to 10000 mappings 
4. The tags can map to more than one port, protocol combinations.  for e.g. sv_P1 and sv_P2 in the sample above. 
5. The matches should be case insensitive 