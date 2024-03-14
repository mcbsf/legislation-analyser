import csv
from my_app.models import VoteResult
from my_app.parsers.votes_results_parser import VotesResultsParser

class VotesResultsRepository:
    def __init__(self, path):
        self.votes_results = VotesResultsParser().parse_csv(path)