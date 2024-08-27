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
def parse_file(filename: str, csvfile):
    """
    with open(filename, "r") as f:
        f = f.readlines()
    print(f)

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

    # Tags should be case-insensitive
    for row in lookup:
        tag = row['tag'].lower()
        tags.append(tag)
        port = row['dstport'].lower()
        protocol = row['protocol'].lower()
        port_protocol.append((port, protocol))
    c = Counter(tags)
    p_counter = Counter(port_protocol)
    #print(p_counter)
    #print(c)
    f.close()

    with open("output.txt", 'w') as output_txt:
        output_txt.write("Tag Counts: " + '\n' + "Tag,Count" + '\n')
        for tag, times in c.items():
            line = tag + "," + str(times) + '\n'
            output_txt.write(line)

        output_txt.write("\nPort/Protocol Combination Counts: " + '\n' + "Port,Protocol,Count" + '\n')
        for dp, times in p_counter.items():
            d, p = dp
            comb = d + "," + p
            line = comb + "," + str(times) + '\n'
            output_txt.write(line)


    # eventually spit out output file with:
    # Count of matches for each tag
    # Count of matches for each port/protocol combination
file_name = "flow_logs.txt"
csv_file = "lookup-table.csv"

parse_file(file_name, csv_file)

# Maybe store lookup table in nested dict?
# DSTPORT: 8th value in line (7th index)
# Protocol: ?
# Tag?
'''
Ex: look = {
    'dstport': {
        "22": 22,
        "21": 21
    },
    'protcol': {},
    'tag'; {}
}
'''