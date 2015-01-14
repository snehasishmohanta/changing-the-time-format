"""
i am having some date format like below and i need to change the date format 
I/P:-
[Dec 17 19:00:00] ,  trakjkfsa,
[Dec 17 19:00:00] ,  door,
[Dec 17 19:00:00] ,  sweater,
[Dec 17 19:00:00] ,  sweater,
[Dec 17 19:00:00] ,  sweater,


O/P:-
19:00:00 ,  trakjkfsa,
19:00:00 ,  door,
19:00:00 ,  sweater,
19:00:00 ,  sweater,
19:00:00 ,  sweater,

"""

import re
import datetime

with open("json.txt") as text:
        for line in text:
                date = re.findall("\[([^]]+)\]", line)
                
                for i in date:
                        line = line.strip("\n")
                        do = datetime.datetime.strptime(i,'%Y %d %H:%M:%S')
                        line = line.replace("[%s]"%i, "%s"%(do.strftime("%H:%M:%S ")) )
                        print line
"""
if the format look like below then we need to change it little
I/P:-
2014-12-17 08:00:00.156 , 3d floor mats for linea , FALSE
2014-12-17 08:00:00.205 , muscle tech whey 5lbs , TRUE
2014-12-17 08:00:00.229 , cap , FALSE
2014-12-17 08:00:00.614 , crawling singing baby , FALSE
2014-12-17 08:00:01.217 , power bank , FALSE
2014-12-17 08:00:01.233 , book my show , FALSE
2014-12-17 08:00:01.336 , pull up bar , TRUE
2014-12-17 08:00:01.384 , ganoderma , FALSE

O/P:-
08:00:00 , 3d floor mats for linea , FALSE
08:00:00. , muscle tech whey 5lbs , TRUE
08:00:00 , cap , FALSE
08:00:00 , crawling singing baby , FALSE
08:00:01 , power bank , FALSE
08:00:01 , book my show , FALSE
08:00:01 , pull up bar , TRUE
08:00:01 , ganoderma , FALSE
"""
import re
import datetime

with open("json.txt") as text:
        for line in text:
                
                date = re.findall("\d+\-+\d+\-+\d+\s+\d+\:+\d+\:+\d+\.+\d+",line)
                for i in date:
                        line = line.strip("\n")
                        do = datetime.datetime.strptime(i,'%Y-%m-%d %H:%M:%S.%f')
                        line = line.replace("%s"%i, "%s"%(do.strftime("%H:%M:%S ")) )
                        print line



