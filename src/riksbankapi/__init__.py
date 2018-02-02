from __future__ import print_function

from zeep import Client
import os

wsdl = os.environ.get('RIKSBANKWSDL','https://swea.riksbank.se/sweaWS/wsdl/sweaWS_ssl.wsdl')

client = Client(wsdl)
from datetime import datetime

foreign_rates_groupid=int(os.environ.get('RATESGROUP',"130"))


def currencyrates():
    """
    print a sh-friendly set of variables representing todays currency rates for $EXCHANGERATES which is a semicolon-
    separated list of currencyexchange names from riksbanken.se using daily avg aggregation
    :return: none
    """
    rates = os.environ.get("EXCHANGERATES",'SEKEURPMI;SEKUSDPMI')
    series = [dict(groupid=foreign_rates_groupid, seriesid=id) for id in rates.split(';')]
    query = dict(languageid='en',
                 min=True,
                 max=True,
                 ultimo=True,
                 aggregateMethod='D',
                 avg=True,
                 datefrom=datetime.now(),
                 dateto=datetime.now(),
                 searchGroupSeries=series)
    result = client.service.getInterestAndExchangeRates(searchRequestParameters=query)
    print (";".join(["{}={}".format(str(s['seriesid']).strip(),s['resultrows'][0]['value']) for s in result['groups'][0]['series']]))