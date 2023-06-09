import json
import os

def main():
    # main function
    yearsi = range(2002,2013)
    
    input_files = [('iswcs','conference'),('ew','conference'),('wowmom','conference'),
                   ('wcnc','conference'),('vtc_spring','conference'),('vtc_fall','conference'),
                   ('icc','conference'),('globecom','conference'),('pimrc','conference'),
                   ('jsac','journal'),('tvt','journal'),('twc','journal'),
                   ('letters','letters')]
    
    for (file,type) in input_files:
        for yeari in yearsi:
            year = str(yeari)
            input_file = 'cleanedup-data/' + file + '_c_' + year + '.json'
            output_file = 'validated-data/' + file + '_v_' + year + '.json'
            
            validate_data(input_file,type,output_file)

def validate_data(input_file,type,output_file):
    data = json.loads(open(input_file).read())
    v_data = json.loads(open(output_file).read())
    
    for paper in data:
        title = paper['title']
        doi = paper['doi']
        year = paper['year']
        citations = paper['citations']
        authors = paper['authors']
        
        if len(authors) <= 0:
            continue
        
        if citations == 0 or citations > 40:
            if citations > 40 and type == 'journal':
                continue
            
            print '\nTitle: ' + title
            print 'DOI: ' + doi
            print 'Year: ' + year
            print 'Citations: ' + str(citations)
            
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
                    break
            
            paper['citations'] = citation_i
        elif citations == -2:
            paper['citations'] = 0
    
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