'''
Author: Byung Ho Lee
Date: 12/27/2013
'''
from timeit import default_timer

fin = open('book.txt')

dic = {}


start = default_timer()

for line in fin:
   line = line.rstrip('\n') #remove '\n' on the rightside.
   temp = line.split(); #return type is list
   for item in temp:
        item = item.strip()
        item = item.lstrip('\"')
        item = item.rstrip('\"')
        item = item.lstrip('\,')
        item = item.rstrip('\,')
        item = item.lstrip('\.')
        item = item.rstrip('\.')
        item = item.lstrip('\_')
        item = item.rstrip('\_')
        if item in dic:
            dic[item] = dic[item] + 1
        else:
            dic[item] = 1

for item in dic:
    print str(item) + " : " + str(dic.get(item))

end = default_timer()

print "elapsed time: " + str(end - start)


fin.close()
