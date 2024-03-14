import csv
from my_app.models import VoteResult
from ..parsers.bills_parser import BillsParser

class VotesResultsParser:
    def __init__(self):
        self.votes_results = {}

    def parse_csv(self, votes_results_data_file):
        self.votes_results = {}
        with open(votes_results_data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)  # Assuming header row for column names
            for row in reader:
                self.create_vote_result(row)
        return self.votes_results

    def create_vote_result(self, data):
        vote_result = VoteResult(**data)
        self.votes_results[vote_result.id] = vote_result

    def get_vote_results(self):
        return self.votes_results
