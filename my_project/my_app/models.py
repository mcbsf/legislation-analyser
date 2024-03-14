from django.db import models

# Create your models here.

class Bill():
    def __init__(self, id, title, sponsor_id) -> None:
        self.id = id
        self.title = title
        self.sponsor_id = sponsor_id

class Legislator():
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

class Vote():
    def __init__(self, id, bill_id) -> None:
        self.id = id
        self.bill_id = bill_id

class VoteResult():
    def __init__(self, id, legislator_id, vote_id, vote_type) -> None:
        self.id = id
        self.legislator_id = legislator_id
        self.vote_id = vote_id
        self.vote_type = vote_type