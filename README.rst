Introduction
----------
Python module to get the Nepse Price rate of the last traded date. It is easy to install and simple to use.

Thanks to [nepalstock](http://www.nepalstock.com) for the data. 

Supported: python 2.7+, python 3

Usage
----------
Install

$ python setup.py install


Example

>>> from nepserate import ScrapeRate
>>> rs = ScrapteRate()
>>> rs.getRate("ADBL") # returns the list of last traded date and rate of Agriculture Development Bank Limited
['2014-10-23', '505']
>>> rs.getRate("ADBL")[0] # This returns last traded date
'2014-10-23'
>>> rs.getRate("ADBL")[1] # This returns the Last traded price
'505'

For full symbol list and supported organizations visit [Listed Companies](http://www.nepalstock.com/listedcompany.php)

Problem
---------
Tweet me [@acsudeep](http://twitter.com/acsudeep)
