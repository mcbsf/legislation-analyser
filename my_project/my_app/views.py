from django.shortcuts import render
from django.http import HttpResponse

from .parsers.votes_parser import VotesParser
from .analysers.bills_analyser import BillsAnalyser
from .analysers.legislator_analyser import LegislatorAnalyser
from .parsers.bills_parser import BillsParser 
from .parsers.legislators_parser import LegislatorsParser 
from .parsers.votes_results_parser import VotesResultsParser

def index(request):

    legislators_parser = LegislatorsParser()
    legislators_dict = legislators_parser.parse_csv("my_app/inputs/legislators.csv")
    print(legislators_dict)

    votes_results_parser = VotesResultsParser()
    votes_results_dict = votes_results_parser.parse_csv("my_app/inputs/vote_results.csv")
    print(votes_results_dict)
    
    legislator_analyser = LegislatorAnalyser(legislators_dict, votes_results_dict)
    legislator_analyser.split_votes_count_by_vote_type()
    legislator_analyser.get_legislators_name()
    print("\n\n VOTE COUNTS \n\n")
    legislator_analyser.parse_legislators_dict_to_list()
    print("\n_______________________________________________________\n")


    bills_parser = BillsParser()
    bills_dict = bills_parser.parse_csv("my_app/inputs/bills.csv")
    print(bills_dict)


    votes_parser = VotesParser()
    votes_dict = votes_parser.parse_csv("my_app/inputs/votes.csv")
    print(votes_dict)

    bills_analyser = BillsAnalyser(bills_dict, votes_dict, votes_results_dict, legislators_dict)
    data = bills_analyser.get_analyzed_data()
    print("\n\n ----> RESULT OF ANALYSIS\n\n")
    print(data)
    return HttpResponse("Hello World")
