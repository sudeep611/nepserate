Introduction
----------
Python module to get the Nepse Price. It is easy to install and simple to use.
- Thanks to nepalstock.com for the data. 
- Supported: python 2.7+, python 3
- All the date are in AD

To install
$ python setup.py install


Dependencies
----------
BeautifulSoup4
requests


Usage
----------

>>> from nepserate import ScrapeRate
>>> rs = ScrapteRate()

>>> rs.getRate("ADBL") # Here the ADBL is the symbol of company
{'high': u'Rs. 514', 'previous_close': u'Rs. 506', 'percent_change': u'-0.20', 'net_change': u'Rs.-1', 'last_traded_date': '2014-10-22', 'ADBL': 'Agricultural Development Bank Ltd', 'last_traded_price': '505', 'low': u'Rs. 495'}

Also you can request to the data of previous date

>>> rs.getRate("ADBL", "2013-12-10")
{'previous_close': u'396', 'amount': u'11,496,761', 'min_price': u'391', 'total_share': u'28,690', 'date': '2013-12-10', 'number_of_transaction': u'192', 'closing_price': u'400', 'difference_rs': u'4', 'ADBL': 'Agricultural Development Bank Ltd', 'max_price': u'405'}


For full symbol list refer to the file docs/SymbolList.rst


TODO
---------
- Adding error handling
- Getting data of multiple company at a time
- Getting data of different company at a time


Problem
---------
Tweet me [@acsudeep](http://twitter.com/acsudeep)
