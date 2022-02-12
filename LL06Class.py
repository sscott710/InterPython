# problem 1
'''# my code
file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\L06_prob1_text.txt', 'r')
x = file.readlines()
for i in range(len(x)): #idk for loop to run through the list
    x[i].replace('Java', 'Python')
    x[i].replace('java', 'Python')
    x[i].replace('null', 'None')
    x[i].replace('array', 'list')'''
# dr.flory's code
def modifyTxt():
    tf = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\L06_prob1_text.txt', 'r')
    rf = tf.read()
    tf.close()
    tdic = {'Java': 'Python', 'java': 'Python', 'null': 'None', 'array': 'list' }
    for x in tdic:
            rf = rf.replace(x, tdic[x])
    else: 
        print(rf) # this only edits the object not the text file
    tf = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\L06_prob1_text.txt', 'w')
    tf.write(rf)
    tf.close()

#problem 2
def prob2():
    len('Python is interesting.') #22
    print('%26s' % 'Python is interesting.')
    #or
    a = 'Python is interesting.'
    print(a.rjust(26))


#problem 3
def prob3():
    #my code/solution
    data = str(input('enter the data: ')) #could be changed to read in a file
    dic = {',': '  '}
    for x in dic:
        data = data.replace(x, dic[x])
    else:
        print(data)
    #dr. flory's code
    print('%-5s %-6s %-1s %12s %5d %6.2f' %('Dunne', 'Sundry','K', '713-894-1238', 23235, 256.3))

#problem 4
def main():
    ''' read the data and produce the output'''
    tf = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\L06_prob4_data.txt', 'r')
    rf = tf.read() #readlines() will produce a list in which the line of the data will be an element of the list
    tf.close()
    trow = makeTable(rf)
    print(trow)
def makeTable(rf):
    '''do the calculation and formatting jobs'''
    rf = rf.strip()
    rf = rf.split('\n')
    m=0
    trow=''
    while m < len(rf):
        estr = rf[m].split('\t')
        x = int(estr[0])
        y = int(estr[1])
        x_square = x ** 2
        y_square = y ** 2
        xy = x*y
        arow = str('%-4d %-5d %10d %10d %6d' % (x, y, x_square, y_square, xy)) + '\n'
        trow = trow + arow
        m+=1
    return trow


if __name__ == '__main__':
    main()
        
    

