#problem 1- fixed
def main1():
    file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\S21_PP06_prob1_data.txt', 'r')
    readFile = file.read()
    file.close()
    table = makeTable(readFile)
    print(table)   
    
def makeTable(readFile):
    readFile = readFile.strip()
    readFile = readFile.split('\n')
    m=2
    table=''
    topRow = readFile[0].split('\t')
    trow = str(topRow[0]).center(20)+ str(topRow[1]).center(20)+ str(topRow[2]).center(20) + '\n'
    table = table + trow
    while m < len(readFile):
        estr = readFile[m].split()
        x = estr[0]
        y = estr[1] #1
        z = estr[2]
        arow = str(x).rjust(17)+ str(y).rjust(23)+ str(z).rjust(15) + '\n'
        table = table + arow
        m+=1
    return table

#problem 2
def main():
    file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\S21_PP06_prob2_text.txt', 'r')
    readFile = file.read()
    file.close()
    modifyTxt() #created new file-- change to OG file before submission
    identifyComment()

def modifyTxt(): #good
    file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\S21_PP06_prob2_text.txt', 'r')
    readFile = file.read()
    file.close()
    tdic = {'data scientist': 'data science professional', 'data analyst': 'data science professional', 'Data scientist': 'Data science professional', 'Data analyst': 'Data science professional' }
    for x in tdic:
            readFile = readFile.replace(x, tdic[x])
    tf = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\S21_PP06_prob2_text.txt', 'w')
    tf.write(readFile)
    tf.close()
def identifyComment():
    file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\S21_PP06_prob2A_text.txt', 'r')
    readFile = file.read()
    file.close()
    f = readFile.strip()
    f = readFile.split('.') 
    comments =[]
    for x in range(len(f)):
        if 'ranked' in f[x]:
            comments.append(f[x])
        if 'called' in f[x]:
            comments.append(f[x])
    comments[2] = comments[2].replace('"', '')
    for x in range(len(comments)):
        comments[x] = comments[x].replace('\n', '')
        print('comment', x+1, '"'+str(comments[x])+' "')
    upskill = ''
    for x in range(len(f)):
        if 'upskill' in f[x]:
            upskill = f[x]
    upskill = upskill.split(',')
    print('You should upskill to data science because' + str(upskill[1]))

            
       
            
        
main()
    


        
