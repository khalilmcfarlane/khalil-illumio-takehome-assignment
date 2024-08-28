import csv
from collections import Counter

'''
Function to parse file.
Should return output file with proper data.
'''


def parse_file(filename: str, csvfile: str, protocolmap: dict):
    # Parse log file and remove empty lines.
    with open(filename, "r") as f:
        lines = [l for l in (line.strip() for line in f) if l]
    log_port_protocol = []
    for line in lines:
        fields = line.split(" ")
        port = fields[6].lower()
        protocol = fields[7].lower()
        if protocol in protocolmap:
            protocol = protocolmap[protocol]
        log_port_protocol.append((port, protocol))

    # Look for port, protocol in lookup exists in log list.
    # If match, add to new list (port, protocol) tuple.
    # if match, create counter for tag done below.
    # keep counter of untagged (ones where port, protocol aren't found).
    tags = []
    port_protocol = []
    untagged = 0

    with open(csvfile, 'r') as f:
        # Parse lookup_table csv file.
        lookup = csv.DictReader(f)
        for row in lookup:
            lookup_port = row['dstport'].lower()
            lookup_protocol = row['protocol'].lower()
            if (lookup_port, lookup_protocol) in log_port_protocol:
                port_protocol.append((lookup_port, lookup_protocol))
                tag = row['tag'].lower()
                tags.append(tag)
            else:
                untagged += 1
    c = Counter(tags)
    p_counter = Counter(port_protocol)

    # Store results into output file
    with open("output.txt", 'w') as output_txt:
        output_txt.write("Tag Counts: " + 2 * '\n' + "Tag,Count" + '\n')
        for tag, times in c.items():
            line = tag + "," + str(times) + '\n'
            output_txt.write(line)
        output_txt.write("Untagged," + str(untagged) + '\n')

        output_txt.write("\nPort/Protocol Combination Counts: " + 2 * '\n' + "Port,Protocol,Count" + '\n')
        for dp, times in p_counter.items():
            d, p = dp
            comb = d + "," + p
            line = comb + "," + str(times) + '\n'
            output_txt.write(line)


# Mapping for protocol to str combo.
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
# Two input files for testing purposes, you can replace respective files in your own testing.
file_name = "flow_logs.txt"
csv_file = "lookup-table.csv"

parse_file(file_name, csv_file, protocol_map)
