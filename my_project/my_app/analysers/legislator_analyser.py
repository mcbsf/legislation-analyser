from copy import deepcopy
from copy import deepcopy
import csv


class LegislatorAnalyser:
    def __init__(self, legislators, vote_results):
        self.legislators = legislators  
        self.vote_results = vote_results

    def split_votes_count_by_vote_type(self):
        self.vote_counts_by_legislator = {}
        for vote_results_id, vote_results in self.vote_results.items():
            legislator_id = vote_results.legislator_id
            vote_type = vote_results.vote_type
            if legislator_id not in self.vote_counts_by_legislator:
                self.vote_counts_by_legislator[legislator_id] = {"num_supported_bills": 0, "num_opposed_bills": 0}
            if vote_type == '1':
                self.vote_counts_by_legislator[legislator_id]["num_supported_bills"] += 1
            elif vote_type == '2':
                self.vote_counts_by_legislator[legislator_id]["num_opposed_bills"] += 1
        #self.vote_counts_by_legislator = list(self.vote_counts_by_legislator.values())  # Convert back to list

    def get_legislators_name(self):
        for legislator_id, vote_counts in self.vote_counts_by_legislator.items():
            legislator = self.legislators.get(legislator_id)  # Find legislator by ID
            if legislator:
                vote_counts["name"] = legislator.name
            else:
                vote_counts["name"] = "Unknown"
    
    def parse_legislators_dict_to_list(self):
        self.vote_counts_by_legislator = list(self.vote_counts_by_legislator.values())
        print()
        print(self.vote_counts_by_legislator)
        return self.vote_counts_by_legislator



# Usage Example (assuming you have legislator and vote_result dictionaries)
