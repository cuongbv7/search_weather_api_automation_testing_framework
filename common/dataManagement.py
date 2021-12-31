from csv import reader
from robot.api.deco import keyword


@keyword("GET DATA FROM CSV")
def get_data_from_csv(file_path):
    with open(file_path, 'r') as read_obj:
        csvReader = list(reader(read_obj))
        csvReader.pop(0)
    return csvReader

