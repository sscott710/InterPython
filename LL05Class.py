#prob 1 from L05 Class Notes
def compoundInterest():
    ''' Calculate the amount of savings in an account earning compound interest'''
    x = eval(input('enter initial balance: '))
    r = (eval(input('enter interest rate: '))/100)
    m = eval(input('enter the number of years: '))
    y =1 #set up for initial value for iterator
    while y <=m:
        x += x*r
        y += 1
    print('$' + str(round(x, ndigits =2)))

def compoundInterest2():
    ''' Calculate the amount of savings in an account earning compound interest'''
    x = eval(input('enter initial balance: '))
    r = (eval(input('enter interest rate: '))/100)
    m = eval(input('enter the number of years: '))
    for y in range(m):
        x += x*r
    print('$' + str(round(x, ndigits =2)))

# prob 2 from L05 Classs Notes
def pysearch():
    '''count the number of word Python in a txt file'''
    file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\L05_prob2_text.txt') #open() function is to access the file
    r = file.read()
    c = r.count('Python') #counting th number of appearances of the word 'Python'
    print('Python appears', str(c), ' times.')
    #how aboout lower case python, c1 = r.count('python')
    #c = c1+c
    #print('Python appears', str(c), ' times.')
    p=0
    for x in range(1, c+1):
        j = r.find('Python', p) #p is the starting index at which find() starts
        p = j+1
        print(j)

#prob 2 but with while loop
def pysearch2():
    '''count the number of word Python in a txt file'''
    file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\L05_prob2_text.txt') #open() function is to access the file
    r = file.read()
    c = r.count('Python') #counting th number of appearances of the word 'Python'
    print('Python appears', str(c), ' times.')
    p=0
    ''' jonathan's code:
    x=0
    while(x <24): #idk the max index of the string
        j = r.find('Python', p) #p is the starting index at which find() starts
        p = j+1
        print(j)
        x+=1'''
    #dr. flory's code
    x=1
    while True:
        if x>c:
            break
        j = rf.find('Python', p)
        p = j+1
        x+=1
        print(j)
        
#prob 3 from LL05
def pySearchEven():
    file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\L05_prob2_text.txt') #open() function is to access the file
    r = file.read()
    c = r.count('Python') #counting th number of appearances of the word 'Python'
    print('Python appears', str(c), ' times.')
    p=0
    ''' my code
    for x in range(1, c+1):
        j = r.find('Python', p) #p is the starting index at which find() starts
        p = j+1
        if((j%2)==0):
            print(j)'''
    #dr flory's code
    for x in range(1, c+1):
        j = r.find('Python', p) #p is the starting index at which find() starts
        p = j+1
        if(j%2 != 0):
            continue
        print(j)

pySearchEven()

