import csv
from collections import Counter

"""
Parse file containing log flow data into a csv file with 3 columns: dstport, protocol, and tag.
The dstport and protocol combination decide what tag can be applied.
"""

'''
Function to parse file.
Should return csv file with proper data
'''


def parse_file(filename: str, csvfile: str, protocol_map: dict):
    with open(filename, "r") as f:
        lines = [l for l in (line.strip() for line in f) if l]

    log_ports = []
    log_protocols = []
    log_port_protocol = []
    for line in lines:
        fields = line.split(" ")
        # Maybe store port/protocol string in tuple list instead
        port = fields[6].lower()
        protocol = fields[7].lower()
        if protocol in protocol_map:
            protocol = protocol_map[protocol]
        log_port_protocol.append((port, protocol))
        #log_ports.append(fields[6])
        #log_protocols.append(fields[7])

    #print(log_port_protocol)
    #print(log_ports)
    #print(log_protocols)
    #print(lines)
    """
    Do I need to check if lookup file combos are inside input log file?
    Ie, check if dstport in dict exists in data retrieved from log
    Only then, add to counter?

    # Store lookup csv file
    # Maybe map something to dstport
    lookup = csv.reader(csvfile)
    next(lookup)
    for row in lookup:
        print(row)
    """
    f = open(csvfile, 'r')
    lookup = csv.DictReader(f)
    tags = []
    port_protocol = []
    untagged = 0

    # Look for port, protocol in lookup exists in log list
    # If match, add to new list (port, protocol) tuple
    # if match, create counter for tag done below
    # keep counter of untagged (ones where port, protocol arent found)
    #for row in lookup:
    for row in lookup:
        #print(row)
        lookup_port = row['dstport'].lower()
        lookup_protocol = row['protocol'].lower()
        if (lookup_port, lookup_protocol) in log_port_protocol:
            port_protocol.append((lookup_port, lookup_protocol))
            tag = row['tag'].lower()
            tags.append(tag)
        else:
            untagged += 1
    f.close()
    c = Counter(tags)
    p_counter = Counter(port_protocol)

    #print(c)
    #print(p_counter)

    """
    # This is only using lookup table as a reference
    # Tags should be case-insensitive
    for row in lookup:
        tag = row['tag'].lower()
        tags.append(tag)
        port = row['dstport'].lower()
        protocol = row['protocol'].lower()
        port_protocol.append((port, protocol))
    c = Counter(tags)
    p_counter = Counter(port_protocol)
    # print(p_counter)
    # print(c)
    f.close()
    """
    # Store ports in input log file in a list
    # Check for every entry, that port exists in port_protocol (ports)
    #

    with open("output.txt", 'w') as output_txt:
        output_txt.write("Tag Counts: " + 2*'\n' + "Tag,Count" + '\n')
        for tag, times in c.items():
            line = tag + "," + str(times) + '\n'
            output_txt.write(line)
        output_txt.write("Untagged," + str(untagged) + '\n')

        output_txt.write("\nPort/Protocol Combination Counts: " + 2*'\n' + "Port,Protocol,Count" + '\n')
        for dp, times in p_counter.items():
            d, p = dp
            comb = d + "," + p
            line = comb + "," + str(times) + '\n'
            output_txt.write(line)

# create mapping for protocol to str combo
protocol_map = {
    "0": "hopopt",
    "1": "icmp",
    "2": "igmp",
    "3": "ggp",
    "4": "ipv4",
    "5": "st",
    "6": "tcp",
    "7": "cbt",
    "8": "egp",
    "9": "igp",
}

file_name = "flow_logs.txt"
csv_file = "lookup-table.csv"

parse_file(file_name, csv_file, protocol_map)



