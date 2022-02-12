import os, pickle, statistics
os.chdir('C:\\Users\\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python')
def main():
    file = open('PP08_prob1_data.dat', 'rb')
    while True:
        try:
            e = pickle.load(file)
        except EOFError:
            file.close()
            break
    data = filtering(e)
    avgIncome = stats(data)    
def filtering(d):
    y = []
    s = list(filter(check, d))
    for x in s:
        y.append(x)
    return y
def check(r):
    if float(r[2]) > 55.0:
        return r
def stats(data):
    avgIn = []
    for x in range(len(data)):
        temp = []
        temp.append(data[x][0])
        avg = round(float(data[x][2]) / float(data[x][1]), 4)
        temp.append(avg)
        avgIn.append(temp)
    file = open('PP08_prob1_data_avgIncome.dat', 'wb')
    pickle.dump(avgIn, file)
    
main()
