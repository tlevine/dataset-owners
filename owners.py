#!/usr/bin/env python
from collections import defaultdict
import sys, csv

from pluplusch import pluplusch

catalogs =[
    'https://data.colorado.gov',
    'https://data.nola.gov',
    'https://healthmeasures.aspe.hhs.gov',
    'https://data.cityofchicago.org',
    'https://data.wa.gov',
    'https://opendata.go.ke',
    'https://data.austintexas.gov',
    'https://data.cityofnewyork.us',
    'https://data.taxpayer.net',
    'https://data.cityofmadison.com',
    'https://data.slcgov.com',
    'https://data.illinois.gov',
    'https://data.somervillema.gov',
    'https://iranhumanrights.socrata.com',
    'https://data.hawaii.gov',
    'https://data.maryland.gov',
    'https://data.ny.gov',
    'https://data.mo.gov',
    'https://data.nfpa.org',
    'https://data.sunlightlabs.com',
    'https://electionsdata.kingcounty.gov',
    'https://data.undp.org',
    'https://data.energystar.gov',
    'https://explore.data.gov',
    'https://data.weatherfordtx.gov',
    'https://bronx.lehman.cuny.edu',
    'https://data.sfgov.org',
    'https://data.edmonton.ca',
    'https://data.consumerfinance.gov',
    'https://www.metrochicagodata.org',
    'https://data.kingcounty.gov',
    'https://data.baltimorecity.gov',
    'https://health.data.ny.gov',
    'http://dati.lombardia.it',
    'https://datacatalog.cookcountyil.gov',
    'https://www.opendatanyc.com',
    'https://cookcounty.socrata.com',
    'https://data.oregon.gov',
    'https://data.oaklandnet.com',
    'https://data.raleighnc.gov',
    'https://finances.worldbank.org',
    'https://data.honolulu.gov',
#   'https://opendata.socrata.com',
    'https://data.cityofboston.gov',
    'https://data.ok.gov',
    'https://data.cms.gov',
    'http://data.snostat.org',
    'https://www.halifaxopendata.ca',
    'https://data.wellingtonfl.gov',
    'https://gettingpastgo.socrata.com',
    'https://www.data.act.gov.au',
    'http://data.redmond.gov',
    'https://data.seattle.gov',
    'https://data.montgomerycountymd.gov',
    'https://data.acgov.org',
    'https://data.medicare.gov',
    'https://controllerdata.lacity.org',
    'https://data.lacity.org',
]

def datasets():
    return pluplusch(catalogs = catalogs, standardize = False)

def url(dataset):
    return dataset['catalog'] + '/d/' + dataset['id']

def owner(dataset):
    return dataset['owner']['id']

def owners(datasets):
    x = defaultdict(lambda:[])
    for dataset in datasets:
        x[owner(dataset)].append(url(dataset))
    return x

def main():
    writer = csv.writer(sys.stdout)
    writer.writerow(('owner','n.datasets','datasets'))
    for o, urls in owners(datasets()).items():
        writer.writerow((o,len(urls),'\n'.join(urls)))

if __name__ == '__main__':
    main()
