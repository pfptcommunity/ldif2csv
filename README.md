# LDIF to CSV Conversion Tool

This tool converts LDIF files to CSV format and allows for changing delimiters and separators. 

### Requirements:

* Python 3.9+
 
### Installing the Package
You can install the API library using the following command. 
```
pip install git+https://github.com/pfptcommunity/ldif2csv.git
```

### Usage

```
usage: ldif2csv [-h] -i <filename> -o <filename> [-s <sep>] [-d <delim>]

Tool to convert LDIF to CSV

options:
  -h, --help                          show this help message and exit
  -i <filename>, --input <filename>   LDIF to read as input.
  -o <filename>, --output <filename>  CSV file to create as output.
  -s <sep>, --separator <sep>         Character to separate the fields in the CSV. By default this is a comma.
  -d <delim>, --delimeter <delim>     Character to delimit multi value fields. By default this is a semi-colon.
```