#!/usr/bin/env python3
import sys
import argparse
import csv
from typing import Dict, List
from ldif import LDIFParser


class LDIFParserNoError(LDIFParser):
    # Remove annoying warnings
    def _error(self, msg):
        if self._strict:
            raise ValueError(msg)

def get_ldif_attributes(filename) -> List:
    attributes = set()
    with open(filename, "rb") as ldif_file:
        parser = LDIFParserNoError(ldif_file, strict=False)
        for dn, record in parser.parse():
            attributes = (attributes | set(record.keys()))
        ldif_file.close()
    attributes = list(attributes)
    attributes.sort()
    return attributes


def generate_csv(ldif_attributes: List[str], filename: str, output: str, delimiter: str, separator: str):
    # Open the LDIF file for reading
    with open(filename, "rb") as ldif_file:
        parser = LDIFParserNoError(ldif_file, strict=False)
        with open(output, 'w', newline='', encoding='utf-8-sig') as report_file:
            csvwriter = csv.DictWriter(report_file, fieldnames=ldif_attributes, extrasaction='ignore', delimiter=delimiter)
            csvwriter.writeheader()
            for dn, record in parser.parse():
                for k, v in record.items():
                    record[k] = separator.join(v)
                csvwriter.writerow(record)
        report_file.close()
    ldif_file.close()


def main():
    if len(sys.argv) == 1:
        print('ldif2csv [-h] --input <filename> [--output <filename>] [--separator <sep>] [--delimeter <delim>]')
        exit(1)

    parser = argparse.ArgumentParser(prog="ldif2csv",
                                     description="""Tool to convert LDIF to CSV""",
                                     formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80))
    parser.add_argument('-i','--input', metavar='<filename>', dest="input_file", type=str, required=True,
                        help='LDIF to read as input.')
    parser.add_argument('-o','--output', metavar='<filename>', dest="output_file", type=str, required=True,
                        help='CSV file to create as output.')
    parser.add_argument('-s','--separator', default=',', metavar='<sep>', dest='field_sep', type=str, required=False,
                        help='Character to separate the fields in the CSV. By default this is a comma.')
    parser.add_argument('-d','--delimeter', default=';', metavar='<delim>', dest="delimiter", type=str, required=False,
                        help='Character to delimit multi value fields. By default this is a semi-colon.')

    args = parser.parse_args()

    print("Input file: {}".format(args.input_file))
    print("Output file: {}".format(args.output_file))
    print("Field Seperator: {}".format(args.field_sep))
    print("Delimiter: {}".format(args.delimiter))

    # First pass obtains the attributes inside the LDIF
    attributes = get_ldif_attributes(args.input_file)

    print("Discovered Attributes: {}".format(attributes))

    # Second pass generates the actual CSV
    generate_csv(attributes, args.input_file, args.output_file, args.field_sep, args.delimiter)


# Main entry point of program
if __name__ == '__main__':
    main()
