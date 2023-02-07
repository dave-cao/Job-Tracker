import csv
import io


def handle_csv(file):
    """File is a filestorage object from html input"""

    file_data = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    reader = csv.DictReader(file_data)

    return reader
