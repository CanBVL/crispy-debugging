#!/usr/bin/env python3

input_file = "Glosarry.txt"
output_file = "Glosarry_sorted.txt"
with open(input_file, 'r') as f:
    with open(output_file, 'w') as o:
        o.write("\n".join(sorted(f.read().splitlines())))
