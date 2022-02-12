'''Notes- make sure everything prints table when submit'''
#task 1- format the data
import os, pickle, statistics
os.chdir('C:\\Users\\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python')
def main():
    file = open('final_proj_data.dat', 'rb')
    while True:
        try:
            e = pickle.load(file)
        except EOFError:
            file.close()
            break
    #table = formating(e)
    #s = stats(e)
    #formatStats(table, s)
    mileRows(e)
    
def formating(f):
    d = []
    temp = []
    for x in range(len(f)):
        if f[x] == '':
            d.append(temp)
            temp = []
        elif x == len(f)-1:
            d.append(temp)
            temp = []
        else:
            temp.append(f[x])
    dirtTrack = d[2]
    turfTrack = d[3]
    intro = d[0][0] + '\n' + d[0][1] + '\n' + d[0][2] + '\n'+ d[0][3] + '\n' + '\n'
    table = intro + dirtTrack[0] + '\n'
    dirtTrack[1] = dirtTrack[1].strip()
    t = dirtTrack[1].split('\t')
    col = t[0].center(30) + t[1].center(20) +t[2].center(15)+t[3].center(15)+t[4].center(15)+t[5].center(25)+t[6].center(20) + '\n'
    table = table + col
    z = 2
    while z < len(dirtTrack):
        dirtTrack[z] = dirtTrack[z].strip()
        i = dirtTrack[z].split('\t')
        row = i[0].ljust(30) + i[1].ljust(20) + i[2].rjust(15) + i[3].rjust(15) + i[4].rjust(15) + i[5].ljust(25) + i[6].rjust(20) + '\n'
        table = table + row
        z = z +1
    table = table + '\n' + turfTrack[0] + '\n'
    turfTrack[1] = turfTrack[1].strip()
    t = turfTrack[1].split('\t')
    col = t[0].center(30) + t[1].center(20) +t[2].center(15)+t[3].center(15)+t[4].center(15)+t[5].center(25)+t[6].center(20) + '\n'
    table = table + col
    z = 2
    while z < len(turfTrack):
        turfTrack[z] = turfTrack[z].strip()
        i = turfTrack[z].split('\t')
        row = i[0].ljust(30) + i[1].ljust(20) + i[2].rjust(15) + i[3].rjust(15) + i[4].rjust(15) + i[5].ljust(25) + i[6].rjust(20) + '\n'
        table = table + row
        z = z +1
    print(table)
    return table
#task 2
def stats(e):
    d = []
    temp = []
    for x in range(len(e)):
        if e[x] == '':
            d.append(temp)
            temp = []
        elif x == len(e)-1:
            d.append(temp)
            temp = []
        else:
            temp.append(e[x])
    dirtTrack = d[2]
    turfTrack = d[3]
    # Dirt Track stats
    dirtAge = []
    dirtWeight = []
    z =2
    while z < len(dirtTrack):
        d = dirtTrack[z].split('\t')
        dirtAge.append(int(d[2]))
        dirtWeight.append(int(d[3]))
        z=z+1
    modeDA = statistics.mode(dirtAge)
    medianDA = statistics.median(dirtAge)
    meanDA = round(statistics.mean(dirtAge),1)
    modeDW = statistics.mode(dirtWeight)
    medianDW = statistics.median(dirtWeight)
    meanDW = round(statistics.mean(dirtWeight), 1)
    resultDA = [modeDA, medianDA, meanDA]
    resultDW = [modeDW, medianDW, meanDW]
    #Turf Track Stats
    turfAge = []
    turfWeight=[]
    j = 2
    while j < len(turfTrack):
        d = turfTrack[j].split('\t')
        turfAge.append(int(d[2]))
        turfWeight.append(int(d[3]))
        j=j+1
    modeTA = statistics.mode(turfAge)
    medianTA = statistics.median(turfAge)
    meanTA = round(statistics.mean(turfAge), 1)
    modeTW = statistics.mode(turfWeight)
    medianTW = statistics.median(turfWeight)
    meanTW = round(statistics.mean(turfWeight), 1)
    results = [[modeDA, medianDA, meanDA], [modeDW, medianDW, meanDW], [modeTA, medianTA, meanTA], [modeTW, medianTW, meanTW]]
    return results
def formatStats(t, r):
    dastats = r[0]
    dwstats = r[1]
    tastats = r[2]
    twstats = r[3]
    ds = '\n' + 'Horse Ages: mode '+ str(dastats[0])+', median '+ str(dastats[1])+ ', average '+ str(dastats[2]) + '\n' +'Horse Weights: mode '+ str(dwstats[0])+', median '+ str(dwstats[1])+ ', average '+ str(dwstats[2]) + '\n'
    ts = '\n' + 'Horse Ages: mode '+ str(tastats[0])+', median '+ str(tastats[1])+ ', average '+ str(tastats[2]) + '\n' +'Horse Weights: mode '+ str(twstats[0])+', median '+ str(twstats[1])+ ', average '+ str(twstats[2]) + '\n'
    tempTable = t.splitlines()
    sTable = ''
    for x in range(len(tempTable)):
        if 'Dirt Track' in tempTable[x]:
            sTable = sTable + tempTable[x] + '\n' + ds + '\n'
        elif 'Turf Track' in tempTable[x]:
            sTable = sTable + tempTable[x] + '\n' + ts + '\n'
        elif 'Distance' in tempTable[x]:
            sTable = sTable + tempTable[x] + '\n\n'
        else:
            sTable = sTable + tempTable[x] + '\n'
    #task 3
    print(sTable)
    f = open('final_proj_tableWithStats.dat', 'wb')
    pickle.dump(sTable, f)

#task 4
def mileRows(e):
    d = []
    temp = []
    for x in range(len(e)):
        if e[x] == '':
            d.append(temp)
            temp = []
        elif x == len(e)-1:
            d.append(temp)
            temp = []
        else:
            temp.append(e[x])
    dirtTrack = d[2]
    turfTrack = d[3]
    header = dirtTrack[1].split('\t')
    table = 'Track Type '.center(15) + header[0].center(15) + header[1].center(15) + header[2].center(15) + header[3].center(15) + header[4].center(15) + header[5].center(15) + header[6].center(15) + '\n'
    for x in range(len(dirtTrack)):
        temp = dirtTrack[x].split('\t')
        if 'Two Miles' in temp[0]:
            table = table + 'Dirt'.ljust(15) + temp[0].ljust(15) + temp[1].ljust(15) + temp[2].rjust(15) + temp[3].rjust(15) + temp[4].rjust(15) + temp[5].ljust(15) + temp[6].rjust(15) + '\n'
        elif 'One Mile' in temp[0]:
            table = table + 'Dirt'.ljust(15) + temp[0].ljust(15) + temp[1].ljust(15) + temp[2].rjust(15) + temp[3].rjust(15) + temp[4].rjust(15) + temp[5].ljust(15) + temp[6].rjust(15) + '\n'
    for x in range(len(turfTrack)):
        temp = turfTrack[x].split('\t')
        if 'Two Miles' in temp[0]:
            table = table + 'Turf'.ljust(15) + temp[0].ljust(15) + temp[1].ljust(15) + temp[2].rjust(15) + temp[3].rjust(15) + temp[4].rjust(15) + temp[5].ljust(15) + temp[6].rjust(15) + '\n'
        elif ' One Mile' == temp[0]:
            table = table + 'Turf'.ljust(15) + temp[0].ljust(15) + temp[1].ljust(15) + temp[2].rjust(15) + temp[3].rjust(15) + temp[4].rjust(15) + temp[5].ljust(15) + (temp[6] + ' ').rjust(15) + '\n'
    print(table)
    f = open('final_proj_mileRows.dat', 'wb')
    pickle.dump(table, f)

main()
