#problem 1
''' jonathan's solution
import math
import random
def main():
    var1 = [1.33,2,0,-2.33,-0.33,-2,-1.67,4.13,-1,6.33,-0.33]
    var2 = [7.00,11.33,16.00,7.33,12.00,29.70,8.00,3.00,9.67,17.33,15.33]
    var3 = [-1.010,0.221,0.991,0.383,0.539,0.170,0.107,-0.729,0.277,2.427,0.801]
    quad = quadratic(random.choice(var1), random.choice(var2), random.choice(var3))
    print('solve for x: ', quad)
def quadratic(a, b, c):
    print('a=', a, 'b=', 'c=', c)
    quad = []
    quad.append(-b + math.sqrt((b**2 - (4*a*c))/ (2*a)))
    quad.append(-b - math.sqrt((b**2 - (4*a*c))/ (2*a)))
    return quad'''
import math, random
var1 = [1.33,2,0,-2.33,-0.33,-2,-1.67,4.13,-1,6.33,-0.33]
var2 = [7.00,11.33,16.00,7.33,12.00,29.70,8.00,3.00,9.67,17.33,15.33]
var3 = [-1.010,0.221,0.991,0.383,0.539,0.170,0.107,-0.729,0.277,2.427,0.801]
def main(): #don't really need main for this problem but could use vars above
    producing(var1, var2, var3)
def producing(va, vb,vc):
    '''produce the quadratic equation.'''
    ra = random.choice(va)
    rb = random.choice(vb)
    rc = random.choice(vc)
    eq = str(ra) +'x^2 + ' + str(rb)+ 'x + ' + str(rc) + ' = 0'
    print('solve the quadratic equation', eq, 'for x. \n')
    answering(ra, rb, rc)
def answering(a, b, c):
    '''solve the equation for x.'''
    try:
        sr = math.sqrt(b*b - 4*a*c)
        x1 = round((-b + sr) / (2*a), ndigits = 4)
        x2 = round((-b - sr) / (2*a), ndigits = 4)
        answer = 'correct answer: x1 = ' + str(x1) + ' and x2 = ' + str(x2)
        print(answer)
    except:
        answer = 'please select another problem.'
        print(answer)
#main()
#problem 2
import os, pickle, statistics 
os.chdir('C:\\Users\\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python')

def problem2():
    '''Get the data'''
    f = open('L08Q2data.dat', 'rb')
    while True:
        try:
            e = pickle.load(f)
        except EOFError:
            f.close()
            break
    d = filtering(e)
    stats(d)

def filtering(data): 
    '''get the data items'''
    y = []
    s = list(filter(checking, data))
    for x in s:
        y.append(x[1])
    return y

def checking(r):
    '''check the file.'''
    return '800 Number Caller' in r

def stats(d):
    '''find and save the statistics'''
    mode = statistics.mode(d)
    median = statistics.median(d)
    mean = statistics.mean(d)
    std = round(statistics.stdev(d), 4) #stdev() produces a sample standard deviation;
                                        #ptdev() will produce the population standard deviation
    result = [mode, median, mean, std]
    f = open('L08Q2data.dat', 'wb')
    pickle.dump(result, f)
    
    
problem2()
