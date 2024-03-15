import csv
import io
from my_app.models import Vote


class VotesParser:
    def __init__(self):
        self.votes = {}

    def parse_csv(self, votes_file):

        self.votes = {}
        decoded_file = votes_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        lines = 0
        for row in csv.reader(io_string, delimiter=',', quotechar='|'):
            print(row)
            if lines>0:
                self.create_vote(row)
            lines+=1
        return self.votes

    def create_vote(self, data):
        vote = Vote(*data)
        self.votes[vote.id] = vote
    
    def get_votes(self):
        return self.votes
