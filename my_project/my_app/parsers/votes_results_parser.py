import csv
import io
from my_app.models import VoteResult
from ..parsers.bills_parser import BillsParser

class VotesResultsParser:
    def __init__(self):
        self.votes_results = {}

    def parse_csv(self, votes_results_file):
        self.votes_results = {}
        decoded_file = votes_results_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        lines = 0
        for row in csv.reader(io_string, delimiter=',', quotechar='|'):
            print(row)
            if lines>0:
                self.create_vote_result(row)
            lines+=1
        return self.votes_results

    def create_vote_result(self, data):
        vote_result = VoteResult(*data)
        self.votes_results[vote_result.id] = vote_result

    def get_vote_results(self):
        return self.votes_results
