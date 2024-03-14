import csv
from my_app.models import Legislator

class LegislatorsParser:
    def __init__(self):
        self.legislators = {}

    def parse_csv(self, legislators_data_file):
        self.legislators = {}
        with open(legislators_data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)  # Assuming header row for column names
            for row in reader:
                self.create_legislator(row)
        return self.legislators

    def create_legislator(self, data):
        legislator = Legislator(**data)
        self.legislators[legislator.id] = legislator


    def get_legislators(self):
        return self.legislators