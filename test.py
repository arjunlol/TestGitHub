# testing out github
import csv

MY_FILE = "sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

    opened_file = open(raw_file)

    #Read CSV file'
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    #Build a data structure to return parsed_data
    #Close CSV file


    return parsed_data




