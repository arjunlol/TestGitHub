# testing out github
import csv

MY_FILE = "sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

    opened_file = open(raw_file)

    #Read CSV file'
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    #Setup an empty list
    parsed_data = []

    #Skip over the first line of the file for the headers
    fields = csv_data.next()

    #iterate over each row of csv, zip together field
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    #Close CSV file
    opened_file.close()
    return parsed_data

#
# def main():
#     #call parse function give it necessary parameters
#     new_data = parse(MY_FILE, ",")
#
#     #data output
#     print(new_data)
#
