# Simple tool to convert LDIF to CSV

This tool converts LDIF files to CSV format and allows for changing delimiters and separators. 

### Requirements:

* Python 3.9+
* ldif
 
### Installing the Package

You can install the tool using the following command directly from Github.

```
pip install git+https://github.com/pfptcommunity/ldif2csv.git
```

or can install the tool using pip.

```
pip install ldif2csv
```

### Usage

```
ldif2csv [-h] --input <filename> [--output <filename>] [--separator <sep>] [--delimeter <delim>]

Tool to convert LDIF to CSV

options:
  -h, --help                          show this help message and exit
  -i <filename>, --input <filename>   LDIF to read as input.
  -o <filename>, --output <filename>  CSV file to create as output.
  -s <sep>, --separator <sep>         Character to separate the fields in the CSV. By default this is a comma.
  -d <delim>, --delimeter <delim>     Character to delimit multi value fields. By default this is a semi-colon.
```
