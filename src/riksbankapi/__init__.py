from __future__ import print_function

from zeep import Client
import os

wsdl = os.environ.get('RIKSBANKWSDL','https://swea.riksbank.se/sweaWS/wsdl/sweaWS_ssl.wsdl')

client = Client(wsdl)
from datetime import datetime, date, timedelta

foreign_rates_groupid=int(os.environ.get('RATESGROUP',"11"))

def ratesgroup():
    result = client.service.getInterestAndExchangeGroupNames(languageid="en")
    return result


def currencyrates():
    """
    print a sh-friendly set of variables representing todays currency rates for $EXCHANGERATES which is a semicolon-
    separated list of currencyexchange names from riksbanken.se using daily avg aggregation
    :return: none
    """
    #print(ratesgroup()) 
    rates = os.environ.get("EXCHANGERATES",'SEKEURPMI;SEKUSDPMI')
    series = [dict(groupid=foreign_rates_groupid, seriesid=id) for id in rates.split(';')]
    #print(series)
    query = dict(languageid='en',
                 min=False,
                 max=True,
                 ultimo=False,
                 aggregateMethod='D',
                 avg=True,
                 dateto=date.today(),
                 datefrom=date.today() - timedelta(days=7),
                 searchGroupSeries=series)
    result = client.service.getInterestAndExchangeRates(searchRequestParameters=query)
    #print(result)
    def avg(s):
       return sum(filter(lambda x: x is not None, [x['value'] for x in s['resultrows']]))/len(s['resultrows']) 

    print (";".join(["{}={}".format(str(s['seriesid']).strip(),avg(s)) for s in result['groups'][0]['series']]))
