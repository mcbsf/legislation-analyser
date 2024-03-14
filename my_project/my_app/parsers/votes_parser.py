import csv
from my_app.models import Vote


class VotesParser:
    def __init__(self):
        self.votes = {}

    def parse_csv(self, votes_data_file):

        self.votes = {}
        self.votes = {}
        with open(votes_data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)  # Assuming header row for column names
            for row in reader:
                self.create_vote(row)
        return self.votes

    def create_vote(self, data):
        vote = Vote(**data)
        self.votes[vote.id] = vote
    
    def get_votes(self):
        return self.votes
