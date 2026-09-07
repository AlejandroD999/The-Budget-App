from datetime import datetime, date
import calendar

def get_year_range():
    today = date.today()
    years = []
   
    for i in range(2000, int(today.year) + 1):
        years.append(i)

    return years

# Pass month year and day\
'''
format = ""
if not month or year or day:
    adjust format

date with values

'''
def string_to_date(date_str, date_format="%Y-%m-%d"):  
    
    datetime_obj = datetime.strptime(date_str, date_format) 
    date_obj = datetime_obj.date() 

    return date_obj

class ExpensesChart:
    def __init__(self, expenses, date_range: list):
        '''
        date_range: [start_date (obj), end_date (obj)]
        '''
        
        self.expenses = expenses
        self.date_range = date_range

            
        # Dict: holds 'date: amount' of data, it is the result of filtered_data
        self.filtered_data = {}
     
        # Output
        self.labels = [] 
        self.data = []


    def get_labels(self):
        # Turn date_range into labels
        pass

    def filter_data(self):
        # Get matching expenses based on date and turn into filtered_data 
        pass 

