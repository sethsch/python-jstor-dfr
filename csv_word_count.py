from bs4 import BeautifulSoup
import glob
import re
import csv

total_freq = {}
all_words = set()

for xml in glob.iglob('data/metadata/*.xml'):
    with open(xml) as f:
        bs = BeautifulSoup(f, "lxml-xml")
        
    pub_year = bs.year
    year = int(str(pub_year)[6:10])
    
    total_freq[year] = total_freq.get(year, {})
    
    print(p)    
    
    txt = xml.replace("metadata", "ngram1").replace(".xml", "-ngram1.txt")
    
    
    
    with open(txt) as t:
        for line in t:
            sub = re.split("\s+", line)
            word = sub[0]
            count = int(sub[1])
            all_words.add(word)
            
        if total_freq[year].get(word, 0) == 0:
            total_freq[year][word] = 0

        total_freq[year][word] += count

for key in total_freq:
    dic = total_freq[key]
    for word in all_words:
        if dic.get(word, 0) == 0:
            dic[word] = 0
    
    dic["PUB-YEAR"] = key


    
file = open("count.csv", "w")
    
with file:
    fields = list(all_words)
    fields.append("PUB-YEAR")
        
    writer = csv.DictWriter(file, fieldnames=fields)
        
    writer.writeheader()
        
    for total_freq in total_freq.values():
        writer.writerow(total_freq)
            