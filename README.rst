Introduction
----------
- Python module to get Nepse Price and other info. 
- Easy to install and Simple to use.
- Thanks to nepalstock.com for the data. 
- Works on python 2.7+ and python 3
- All the date are in AD

To install
$ python setup.py install


Dependencies
----------

* BeautifulSoup4
* requests


Usage
----------

>>> from nepserate import ScrapeRate
>>> rs = ScrapeRate()

>>> rs.getRate("ADBL") # 'ADBL' is the symbol of the orgranization for more reger to docs/SymbolList.rst
{'high': u'Rs. 514', 'previous_close': u'Rs. 506', 'percent_change': u'-0.20', 'net_change': u'Rs.-1', 'last_traded_date': '2014-10-22', 'ADBL': 'Agricultural Development Bank Ltd', 'last_traded_price': '505', 'low': u'Rs. 495'}

Also you can request to the data of previous date 

>>> rs.getRate("ADBL", "2013-12-10")
{'previous_close': u'396', 'amount': u'11,496,761', 'min_price': u'391', 'total_share': u'28,690', 'date': '2013-12-10', 'number_of_transaction': u'192', 'closing_price': u'400', 'difference_rs': u'4', 'ADBL': 'Agricultural Development Bank Ltd', 'max_price': u'405'}


Reference
----------
- Symbol list of the Banks and Organization (https://github.com/acsudeep/nepserate/blob/master/docs/SymbolList.rst)


Problem
---------
Tweet me [@acsudeep](http://twitter.com/acsudeep)
