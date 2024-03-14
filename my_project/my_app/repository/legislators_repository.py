import csv
from my_app.models import Legislator
from my_app.parsers.legislators_parser import LegislatorsParser

class LegislatorRepository:
    def __init__(self, path):
        self.legislators = LegislatorsParser().parse_csv(path)