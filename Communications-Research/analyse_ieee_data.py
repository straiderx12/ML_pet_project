from pandas import Series, DataFrame
import pandas as pd
import numpy as np

def main():
    # Load IEEE data
    ieee_data = load_ieee_data()
    
    # Analyse the IEEE data
    analyse_publications(ieee_data)
    analyse_countries(ieee_data)
    
def load_ieee_data():
    # Conferences
    ew = pd.read_json('final-data/ew.json')
    globecom = pd.read_json('final-data/globecom.json')
    icc = pd.read_json('final-data/icc.json')
    iswcs = pd.read_json('final-data/iswcs.json')
    pimrc = pd.read_json('final-data/pimrc.json')
    vtc_fall = pd.read_json('final-data/vtc_fall.json')
    vtc_spring = pd.read_json('final-data/vtc_spring.json')
    wcnc = pd.read_json('final-data/wcnc.json')
    wowmom = pd.read_json('final-data/wowmom.json')
    
    # Journals
    jsac = pd.read_json('final-data/jsac.json')
    letters = pd.read_json('final-data/letters.json')
    tvt = pd.read_json('final-data/tvt.json')
    twc = pd.read_json('final-data/twc.json')
    
    # Add additional columns
    add_code_type_columns(ew,'ew','conference')
    add_code_type_columns(globecom,'globecom','conference')
    add_code_type_columns(icc,'icc','conference')
    add_code_type_columns(iswcs,'iswcs','conference')
    add_code_type_columns(pimrc,'pimrc','conference')
    add_code_type_columns(vtc_fall,'vtc_fall','conference')
    add_code_type_columns(vtc_spring,'vtc_spring','conference')
    add_code_type_columns(wcnc,'wcnc','conference')
    add_code_type_columns(wowmom,'wowmom','conference')
    add_code_type_columns(jsac,'jsac','journal')
    add_code_type_columns(letters,'letters','journal')
    add_code_type_columns(tvt,'tvt','journal')
    add_code_type_columns(twc,'twc','journal')
    
    # Consolidate all data into one data frame
    ieee_data = pd.concat([ew,globecom,icc,iswcs,pimrc,
                           vtc_fall,vtc_spring,wcnc,wowmom,
                           jsac,letters,tvt,twc])
    
    return ieee_data

def add_code_type_columns(df,code,type):
    df['code'] = code
    df['type'] = type

def analyse_publications(ieee_data):
    pubs_by_yr_code = ieee_data.groupby(['code','year'])['citations'].count().unstack()
    citations_by_yr_code = ieee_data.groupby(['code','year'])['citations'].sum().unstack()
    quality_by_yr_code = citations_by_yr_code / pubs_by_yr_code
    print 'Number of Publications grouped by Code and Year'
    print '-----------------------------------------------'
    print pubs_by_yr_code
    print '\n'
    print 'Quality of Publications grouped by Code and Year'
    print '------------------------------------------------'
    print quality_by_yr_code
    print '\n'

def analyse_countries(ieee_data):
    pubs_by_country = ieee_data.groupby('country')['citations'].count()
    citations_by_country = ieee_data.groupby('country')['citations'].sum()
    quality_by_country = citations_by_country / pubs_by_country
    
    pubs_by_country.sort(ascending=False)
    quality_by_country.sort(ascending=False)
        
    print 'Number of Publications grouped by Code and Country'
    print '--------------------------------------------------'
    print pubs_by_country[0:50]
    print '\n'
    print 'Quality of Publications grouped by Code and Country'
    print '---------------------------------------------------'
    print quality_by_country[0:50]
    print '\n'

if __name__ == "__main__":
    main()