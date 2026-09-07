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
        self.data = [0 for _ in range(0, 12)]
        
        self.make_labels()
        self.filter_data()
    
    def make_labels(self):
        # Turn date_range into labels
        for i in range(0, 12):
            self.labels.append(calendar.month_name[i+1])

    def filter_data(self):
        # Get matching expenses based on date and turn into filtered_data 
        for expense in self.expenses:
            if self.date_range[0] <= expense.date <= self.date_range[1]:
                self.filtered_data[expense.date.month] = expense.amount 
                self.data[expense.date.month - 1] += expense.amount
        

    # Test purposes only
    def status(self):
        print(self.expenses)
        print("-------")
        print("Date Range:", self.date_range)
        print("Filtered Data:", self.filtered_data)
        print("Labels:\n", self.labels)
        print("Data:\n", self.data)

        return

    def get_data(self):
        return {"labels": self.labels, "data": self.data}
