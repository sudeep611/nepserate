# nepserate
# Author : Sudeep Acharya <sudeep611@gmail.com>
import re
from .csymbol import stockSym
import requests
from bs4 import BeautifulSoup

# Main class that handles everything.
class ScrapeRate():
    """ This class is responsible for scraping the rate from the website and returning the rate.
    Methods:
        getPrice(symbol) - get the today's rate of requested organization
    """
    def __init__(self):
        # This is base url of the page to scarp
        self.baseUrl = "http://www.nepalstock.com/companydetail.php?StockSymbol=" 
        self.prevUrl = "http://www.nepalstock.com/datanepse/previous.php"
        # compile the regex pattern
        self.pattern = re.compile("-->(.+?)</td>")
        self.stockSym = stockSym()

    def getRate(self, symbol, passedDate=None):
        """This function returns the list of date and rate."""
        if(passedDate == None):    
            try:
                content = requests.get(self.baseUrl + symbol)
                soup = BeautifulSoup(content.text)
                bigtable = str(soup.findAll('table')[4])
                scrapTable = BeautifulSoup(bigtable).findAll('table')[0]
                
                for row in scrapTable.findAll('table')[0:]:
                    for i in row.findAll('tr')[1:]:
                        result = i.findAll('td')
                        return {"last_traded_date":re.findall(self.pattern, str(result[0]))[0], 
                                    symbol:self.stockSym[symbol],
                                    "last_traded_price":re.findall(self.pattern, str(result[1]))[0], 
                                    "net_change":result[2].text, 
                                    "percent_change":result[3].text,
                                    "high":result[4].text,
                                    "low":result[5].text,
                                    "previous_close":result[6].text,
                                }
                    break   
            except Exception as e:
                print(e.args)
                # print "Something Went Wrong! in getRate of ScrapeRate."
        else:
            try:
                postDate = {'Date':passedDate}
                req = requests.post(self.prevUrl, data=postDate)
                content = req.text
                soup = BeautifulSoup(content)
                bigtable = str(soup.findAll('table')[4])
                scrapTable = BeautifulSoup(bigtable).findAll('table')[5]

                for row in scrapTable.findAll('tr')[1:]:
                    result = row.findAll('td')
                    if(result[1].a.string == self.stockSym[symbol]):
                        return { "date":str(passedDate), # date for reference purpose
                            symbol:self.stockSym[symbol],
                            "number_of_transaction":result[2].string, # No of transaction
                            "max_price":result[3].string, # max price
                            "min_price":result[4].string, # min price
                            "closing_price":result[5].string, # closing price
                            "total_share":result[6].string, # total share
                            "amount":result[7].string, # amount
                            "previous_close":result[8].string, # previous closing
                            "difference_rs":result[9].string # difference rs
                            }
            except Exception as e:
                print(e.args)                    
                