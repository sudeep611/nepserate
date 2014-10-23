Introduction
----------
Python module to get the Nepse Price of the last traded date. It is easy to install and simple to use.

Thanks to [nepalstock](http://www.nepalstock.com) for the rate. 

It supports python 2.7+ and python 3 as well.

Usage
----------
To install
$ python setup.py install

Using

>>> from nepserate import ScrapeRate
>>> rs = ScrapteRate()
>>> rs.getRate("ADBL") # Here the ADBL is the symbol of company
This return the list of last traded date and rate.
For example ['2014-10-23', '505']


>>> rs.getRate("ADBL")[0] # This returns last traded date
>>> rs.getRate("ADBL")[1] # This returns the Last traded price

For full symbol list and supported organizations visit [Listed Companies](http://www.nepalstock.com/listedcompany.php)

Problem
---------
Tweet me [@acsudeep](http://twitter.com/acsudeep)
