from copy import deepcopy
from copy import deepcopy
import csv


class LegislatorAnalyser:
    def __init__(self, legislators, vote_results):
        self.legislators = legislators  
        self.votes_results = vote_results

    def merge_with_legislator_names(self, vote_counts_by_legislator_id):
        self.vote_counts_by_legislator = {}
        print(vote_counts_by_legislator_id)
        for legislator_id, legislator in self.legislators.items():
            print("analyzing")
            print(legislator_id)
            legislator_vote_counts = vote_counts_by_legislator_id.get(legislator_id)
            if legislator_vote_counts:
                legislator.num_supported_bills = legislator_vote_counts['num_supported_bills']
                legislator.num_opposed_bills = legislator_vote_counts['num_opposed_bills']
            else:
                legislator.num_supported_bills = 0
                legislator.num_opposed_bills = 0
        #self.vote_counts_by_legislator = list(self.vote_counts_by_legislator.values())  # Convert back to list

    def get_vote_counts_by_legislator_id(self):
        vote_counts_by_legislator_id = {}
        for vote_results_id, vote_results in self.votes_results.items():
            legislator_id = vote_results.legislator_id
            vote_type = vote_results.vote_type
            if vote_results.legislator_id not in vote_counts_by_legislator_id:
                vote_counts_by_legislator_id[legislator_id] = {"num_supported_bills": 0, "num_opposed_bills": 0}
            if vote_type == '1':
                vote_counts_by_legislator_id[legislator_id]["num_supported_bills"] += 1
            elif vote_type == '2':
                vote_counts_by_legislator_id[legislator_id]["num_opposed_bills"] += 1
        return vote_counts_by_legislator_id
    
    def parse_legislators_dict_to_list(self):
        self.legislators = list(self.legislators.values())
        print()
        print(self.legislators)
        return self.legislators



# Usage Example (assuming you have legislator and vote_result dictionaries)
