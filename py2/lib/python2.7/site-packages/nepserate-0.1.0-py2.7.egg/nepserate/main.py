# nepserate
# Author : Sudeep Acharya <sudeep611@gmail.com>
import urllib3
import re

# Main class that handles everything.
class ScrapeRate():
    """ This class is responsible for scraping the rate from the website.
    Methods:
        getPrice(key) - get the today's rate of requested organization
    """
    def __init__(self):
        # This is base url of the page to scarp
        self.baseUrl = "http://www.nepalstock.com/companydetail.php?StockSymbol=" 
        # compile the regex pattern
        self.pattern = re.compile("-->(.+?)</td>")

    def getRate(self, key):
        """This function returns the list of date and rate."""
        try:
            pass
            url = self.baseUrl + str(key)
            http = urllib3.PoolManager()
            r = http.request('GET', url)
            rate = re.findall(self.pattern, r.data.decode("utf-8"))
            return rate
        except Exception as e:
            print(e.args)
            # print "Something Went Wrong! in getRate of ScrapeRate."
            