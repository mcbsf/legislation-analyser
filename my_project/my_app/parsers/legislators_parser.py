import csv
import io
from my_app.models import Legislator

class LegislatorsParser:
    def __init__(self):
        self.legislators = {}

    def parse_csv(self, csv_data):
        self.legislators = {}
        decoded_file = csv_data.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        lines = 0
        for row in csv.reader(io_string, delimiter=',', quotechar='|'):
            print(row)
            if lines>0:
                self.create_legislator(row)
            lines+=1
        return self.legislators

    def create_legislator(self, data):
        legislator = Legislator(*data)
        self.legislators[legislator.id] = legislator

    def get_legislators(self):
        return self.legislators