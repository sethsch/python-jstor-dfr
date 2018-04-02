from bs4 import BeautifulSoup
import glob
import re
import json

total_freq = {}

for xml in glob.iglob('data/metadata/*.xml'):
    with open(xml) as f:
        bs = BeautifulSoup(f, "lxml-xml")
        
    pub_year = bs.year
    year = int(str(pub_year)[6:10])
    
    total_freq[year] = total_freq.get(year, {})

    
    txt = xml.replace("metadata", "ngram1").replace(".xml", "-ngram1.txt")
    
    
    
    with open(txt) as t:
        for line in t:
            sub = re.split("\s+", line)
            word = sub[0]
            count = int(sub[1])
            
        if total_freq[year].get(word, 0) == 0:
            total_freq[year][word] = 0

        total_freq[year][word] += count

    
file = open("count.json", "w")
    
with file:
    json.dump(total_freq, file)