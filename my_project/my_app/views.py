from django.shortcuts import render
from django.http import HttpResponse

from .parsers.votes_parser import VotesParser
from .analysers.bills_analyser import BillsAnalyser
from .analysers.legislator_analyser import LegislatorAnalyser
from .parsers.bills_parser import BillsParser 
from .parsers.legislators_parser import LegislatorsParser 
from .parsers.votes_results_parser import VotesResultsParser

def index(request):

    return render(request, "my_app/index.html")

def analyse_files(request):
    bills_file_path = request.FILES['bills_file']
    votes_file_path = request.FILES['votes_file']
    legislators_file_path = request.FILES['legislators_file']
    votes_results_file_path = request.FILES['votes_results_file']
    legislators_parser = LegislatorsParser()
    legislators_dict = legislators_parser.parse_csv(legislators_file_path)
    votes_results_parser = VotesResultsParser()
    votes_results_dict = votes_results_parser.parse_csv(votes_results_file_path)
    
    legislator_analyser = LegislatorAnalyser(legislators_dict, votes_results_dict)
    legislator_analyser.split_votes_count_by_vote_type()
    legislator_analyser.get_legislators_name()
    print("\n\n VOTE COUNTS \n\n")
    legislator_analysis = legislator_analyser.parse_legislators_dict_to_list()
    print("\n_______________________________________________________\n")


    bills_parser = BillsParser()
    bills_dict = bills_parser.parse_csv(bills_file_path)
    print(bills_dict)


    votes_parser = VotesParser()
    votes_dict = votes_parser.parse_csv(votes_file_path)
    print(votes_dict)

    bills_analyser = BillsAnalyser(bills_dict, votes_dict, votes_results_dict, legislators_dict)
    bills_analysis = bills_analyser.get_analyzed_data()
    print("\n\n ----> RESULT OF ANALYSIS\n\n")
    print(bills_analysis)
    context = {
        'bills_analysis': bills_analysis,
        'legislators_analysis': legislator_analysis
    }
    return render(request, "my_app/analysis.html", context)