'''
Created on Aug 19, 2015

@author: ChandarRaju

This class has methods to read company details from AWS database
'''

import _mysql

class Company:
    
    def __init__(self):       
        con = _mysql.connect('stockfit.ccd1gekitlko.us-west-2.rds.amazonaws.com', 'stockfit', 'stocksfit', 'StockFit')
        
        con.query("SELECT distinct cusip from stk_company")
        result = con.use_result()
        
        rows = result.fetch_row()
        
        for row in rows:
            print(row)