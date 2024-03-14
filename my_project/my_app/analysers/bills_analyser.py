from copy import deepcopy


class BillsAnalyser:
    def __init__(self, bills_dict, votes_dict, votes_results_dict, legislators_dict):
        self.bills_dict = bills_dict
        self.votes_dict = votes_dict
        self.votes_results_dict = votes_results_dict
        self.legislators_dict = legislators_dict

    def aggregate_data(self):
        print("\n\n\n STARTED AGGREGATION \n\n\n")
        for bill_id, bill in self.bills_dict.items():

            bill.supporter_count = 0
            bill.opposer_count = 0
            bill.sponsor_name = "Unkown"
            print("\n --->analyzing: \n\n ", bill.__dict__)
            if bill.sponsor_id in self.legislators_dict:
                print()

                sponsor = self.legislators_dict.get(bill.sponsor_id)  
                bill.sponsor_name = sponsor.name if sponsor else "Unkown"
            self.calculate_bill_vote_results(bill)

    def get_vote_results(self, bill, vote_id):
        for vote_result_id, vote_result in self.votes_results_dict.items():
            if vote_result.vote_id == vote_id:
                vote_type = vote_result.vote_type
                if vote_type == "1":
                    bill.supporter_count += 1
                elif vote_type == "2":
                    bill.opposer_count += 1

    def calculate_bill_vote_results(self, bill):
        """ print("\n\n --> analyzing bill:", bill.id, "\n")
        print(bill.__dict__)
        print() """
        for vote_id, vote in self.votes_dict.items():
            if vote.bill_id == bill.id:
                self.get_vote_results(bill, vote.id)
            

    def format_output(self):
        return [bill.__dict__ for bill_id, bill in self.bills_dict.items()]

    def get_analyzed_data(self):
        self.aggregate_data()
        bills_list = self.format_output()
        return bills_list

# Example usage (assuming you have the data dictionaries)

# Now you can use or write the analyzed_bills data (list of dictionaries) as needed


class BillsAnalyser2:
    #clean code warning, generic name 'Analyser' usually implies more than 1 purpose. possible refactor
    def __init__(self, votes_df, bills_df, vote_results_df, legislator_df) -> None:
        self.votes_df = deepcopy(votes_df)
        self.vote_results_df = deepcopy(vote_results_df) 
        self.bills_df = deepcopy(bills_df) 
        self.legislator_df = deepcopy(legislator_df) 
    
    def parse_columns_to_match_pandas_merge(self):
        self.votes_df = self.votes_df.rename(
            columns={'id': 'vote_id'}
        )
        self.bills_df = self.bills_df.rename(
            columns={
                'id': 'bill_id',
                'sponsor_id': 'legislator_id'
            }
        )

        self.bills_df = self.bills_df.rename(
            columns={'id': 'bill_id'}
        )

        self.legislator_df = self.legislator_df.rename(
            columns={'id': 'legislator_id'}
        )

    def get_votes_by_bill(self):
        self.votes_df = self.votes_df.merge(self.vote_results_df[['id','vote_id','vote_type']], on='vote_id', how='left')
        self.bills_df = self.bills_df.merge(self.votes_df, on='bill_id', how='left')
        self.bills_df = self.bills_df.merge(self.legislator_df, on='legislator_id', how='left').fillna('Unknown')

    def split_votes_count_by_vote_type(self):
        self.bills_df['count'] = 1
        self.bills_df = self.bills_df.pivot_table(index=['bill_id', 'title', 'name'], columns='vote_type', values='count', aggfunc='sum')
        self.bills_df.columns = ['supporter_count', 'opposer_count']
        self.bills_df = self.bills_df.reset_index()

    def write_csv(self):
        self.bills_df.to_csv('output/bills-support-oppose-count.csv', index = False)

    def get_sponsor_name(self):
        self.bills_df = self.bills_df.merge(self.legislator_df, on='legislator_id', how='left')

    def parse_column_names_to_expected_output(self):
        self.bills_df = self.bills_df.rename(
            columns = {
                'bill_id': 'id',
                'name': 'primary_sponsor'
            }
        )
    
    def order_columns_to_expected_output(self):
        self.bills_df = self.bills_df[['id', 'title',  'supporter_count', 'opposer_count', 'primary_sponsor']]