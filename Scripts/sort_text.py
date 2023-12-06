#!/usr/bin/env python3

#This script receives a .text file, sorts it alphabetically, and creates a new file with the final result

input_file = <File_name>
output_file = <File_name>
with open(input_file, 'r') as f:
    with open(output_file, 'w') as o:
        o.write("\n".join(sorted(f.read().splitlines())))
f.close()
o.close()
