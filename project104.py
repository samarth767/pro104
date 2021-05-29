import csv
from collections import Counter
with open("pro.csv") as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
totalentrys=len(filedata)
totalweight=0
sorteddata=[]
for i in filedata:
    totalweight+=float(i[2])
    sorteddata.append(float(i[2]))
sorteddata.sort()

def getmean(totalweight,totalentrys):
    mean=totalweight/totalentrys
    print(mean)

def getmedian(totalentrys,sorteddata):
    if totalentrys%2==0:
        m1=float(sorteddata[totalentrys//2])
        m2=float(sorteddata[totalentrys//2 - 1])
        median=(m1+m2)/2
    else:
        median=float(sorteddata[totalentrys//2])
    print(median)
def getmode(sorteddata):
    data=Counter(sorteddata)
    modedict={
        "75-85":0,
        "85-95":0,
        "95-105":0,
        "105-115":0,
        "115-125":0,
        "125-135":0,
        "135-145":0,
        "145-155":0,
        "155-165":0,
        "165-175":0
    }
    for weight,occurence in data.items():
        if 75<weight<85:
            modedict["75-85"]+=occurence
        elif 85<weight<95:
             modedict["85-95"]+=occurence
        elif 95<weight<105:
             modedict["95-105"]+=occurence
        elif 105<weight<115:
             modedict["105-115"]+=occurence
        elif 115<weight<125:
             modedict["115-125"]+=occurence      
        elif 125<weight<135:
             modedict["125-135"]+=occurence
        elif 135<weight<145:
             modedict["135-145"]+=occurence  
        elif 145<weight<155:
             modedict["145-155"]+=occurence
        elif 155<weight<165:
             modedict["155-165"]+=occurence     
        elif 165<weight<175:
             modedict["165-175"]+=occurence
    mode_range,mode_occurence=0,0
    for range,occurence in modedict.items():
       if occurence>mode_occurence:
           mode_range,mode_occurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
    mode=float((mode_range[0]+mode_range[1])/2) 
    print(mode)

getmean(totalweight,totalentrys)
getmedian(totalentrys,sorteddata)
getmode(sorteddata)