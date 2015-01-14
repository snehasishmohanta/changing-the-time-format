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


