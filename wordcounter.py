'''
Author: Byung Ho Lee
Date: 12/27/2013
GITHUB TESTING!!
'''
from timeit import default_timer

fin = open('book.txt')

dic = {}

#find the most common letter 
def showhighest():
    key = ""
    highest = dic.values()[0]; #value of 'first' element
    for item in dic:
        if(dic[item] > highest):
            highest = dic[item]
            key = item
    print "key = " + key + ", value = " + str(highest)

#for time measuring
def currentTime():
    return default_timer()

#
def buildDictionary():
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
#
def printDictionary():
    for item in dic:
        print str(item) + " : " + str(dic.get(item))
#
def process():
    buildDictionary()
    printDictionary()


startTime = currentTime()
process()
endTime = currentTime()

print "elapsed time: " + str(endTime - startTime)
showhighest()

fin.close()
