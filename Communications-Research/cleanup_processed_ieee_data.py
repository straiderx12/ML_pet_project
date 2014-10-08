import json
import os 

def main():
    # main function
    yearsi = range(2002,2013)
    
    #input_files = ['iswcs','ew','wowmom','wcnc','vtc_spring','vtc_fall','icc',
    #               'globecom','pimrc','jsac','tvt','twc','letters']
    input_files = ['jsac']
    
    for file in input_files:
        for yeari in yearsi:
            year = str(yeari)
            input_file = 'processed-data/' + file + '_' + year + '.json'
            output_file = 'processed-data/' + file + '_c_' + year + '.json'
            
            cleanup_data(input_file,output_file)

def cleanup_data(input_file,output_file):
    data = json.loads(open(input_file).read())
    
    for paper in data:
        title = paper['title']
        doi = paper['doi']
        year = paper['year']
        citations = paper['citations']
        
        if citations < 0:
            print '\nTitle: ' + title
            print 'DOI: ' + doi
            print 'Year: ' + year
            
            # Makes data entry a lot easier by copying GS link to clipboard
            # (works only on the Mac)
            query = 'http://scholar.google.co.uk/scholar?q='
            if len(doi) != 0:
                query = query + doi
            else:
                query = query + title
            query = query + '&btnG=&hl=en&as_sdt=0%2C5'
            os.system("echo '%s' | pbcopy" % query)
            
            citation_i = 0
            while True:
                citation_s = raw_input('Enter citations for paper: ')
                if integer(citation_s):
                    citation_i = int(citation_s)
                    if citation_i == 0:
                        citation_i = -2
                    break
            
            paper['citations'] = citation_i
    
    with open(output_file,'w') as f:
        json.dump(data,f)

def integer(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()