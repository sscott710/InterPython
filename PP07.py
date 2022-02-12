import json
#prob 1
def main():
    file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\PP07_priob1_data.txt')
    table = format(file)
    print(table)
def format(file):
    fileRead = list(map(str, file))
    dlist = []
    for x in range(len(fileRead)):
        fileRead[x] = fileRead[x].replace('\n','')
        fileRead[x] = fileRead[x].replace(' ', '\t')
        y = fileRead[x].split('\t')
        dlist.append(y)
    dlist2 = []
    for x in range(len(dlist)):
        for y in range(len(dlist[x])):
            if dlist[x][y] != '':
                dlist2.append(dlist[x][y])
    print(dlist2)
    table = ''
    count = 0
    while count < len(dlist2):
        a = dlist2[count]
        b = dlist2[count+1]
        c = dlist2[count+2]
        d = dlist2[count+3]
        arow = a.ljust(10) + b.rjust(10) + c.rjust(10) + (' ' + d).ljust(10) + '\n'
        table = table + arow
        count = count +4
    return table
    '''fileRead = fileRead.replace(' ', '\t')
    fileRead = fileRead.splitlines()
    print(fileRead)
    dlist = []
    for x in range(len(fileRead)):
        y = fileRead[x].split('\t')
        dlist.append(y)
    print(dlist)
    dlist2 = []
    for x in range(len(dlist)):
        for y in range(len(dlist[x])):
            if dlist[x][y] != '':
                dlist2.append(dlist[x][y])
    print(dlist2)
    #separate by index things - by 4 and; use map to make list of strs??
    table = ''
    count = 0
    while count < len(dlist2):
        a = dlist2[count]
        b = dlist2[count+1]
        c = dlist2[count+2]
        d = dlist2[count+3]
        arow = a.ljust(10) + b.rjust(5) + c.rjust(5) + d.ljust(10) + '\n'
        table = table + arow
        count = count +4
    return table'''
                       
    
        

                 
main()
'''#prob 2
jstr = '[[1972,"Rod Carew", "Minnesota",0.318], [1973,"Rod Carew", "Minnesota",0.35], [1985,"Wade Boggs", "Boston",0.368]]'
def main2():
    #jstr = input('enter the data: ')
    jkv =jsonToPython(jstr)
    print(jkv[0], '\n', jkv[1], '\n', jkv[2])
def jsonToPython(jstr):
    jtl = json.loads(jstr) #list of lists
    jkv =listToDict(jtl)
    return jkv
def listToDict(jtl):
    d = {"p1": {"year": 0, "player": "", "club": "", "mean": 0.0},
         "p2": {"year": 0, "player": "", "club": "", "mean": 0.0},
         "p3": {"year": 0, "player": "", "club": "", "mean": 0.0}}
    k = list(d.keys())
    keys = ["year", "player", "club", "mean"]
    for x in range(len(jtl)):
        for y in range(len(jtl[x])):
            d[k[x]][keys[y]] = jtl[x][y]
    jkv =dictToj(d)
    return jkv
def dictToj(d):
    vlist = list(d.values())
    j1 = json.dumps(vlist[0])
    j2 = json.dumps(vlist[1])
    j3 = json.dumps(vlist[2])
    return(j1, j2, j3)        
main2()'''
    
