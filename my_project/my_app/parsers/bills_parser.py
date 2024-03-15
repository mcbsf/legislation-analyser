import csv
import io
from ..models import Bill

class BillsParser:
    def __init__(self):
        self.bills = {}

    def parse_csv(self, bills_file):
        self.bills = {}
        decoded_file = bills_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        lines = 0
        for row in csv.reader(io_string, delimiter=',', quotechar='|'):
            print(row)
            if lines>0:
                self.create_bill(row)
            lines+=1
        return self.bills

    def create_bill(self, data):
        bill = Bill(*data)  # Unpack data using keyword arguments
        self.bills[bill.id] = bill
