import csv
from ..models import Bill

class BillsParser:
    def __init__(self):
        self.bills = {}

    def parse_csv(self, bills_file_path):
        self.bills = {}
        with open(bills_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)  # Assuming header row for column names
            for row in reader:
                self.create_bill(row)
        return self.bills

    def create_bill(self, data):
        bill = Bill(**data)  # Unpack data using keyword arguments
        self.bills[bill.id] = bill
