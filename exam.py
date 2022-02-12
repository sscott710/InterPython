#problem 1
def main():
    file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\S21_exam2_prob1_data.txt')
    fileRead = file.read()
    file.close()
    fileRead = fileRead.strip()
    fileRead = fileRead.split('\n')
    count = 0
    data = []
    temp = []
    for x in range(len(fileRead)):
        if count < 8:
            temp.append(fileRead[x])
            count+=1
        else:
            data.append(temp)
            temp = []
            count =0
    #print out
    for x in range(len(data)):
        for y in range(len(data[x])):
            print(str(data[x][y]).rjust(10), end = " ")
            if y + 1 == len(data[x]):
                print('\n')
            
          
        
#main()
#problem 2
def prob2():
    file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\S21_exam2_prob2_text.txt')
    fileRead = file.read()
    file.close()
    fileRead = fileRead.strip()
    fileRead = fileRead.split('\n')
    dog = []
    cat = []
    for x in range(len(fileRead)):
        if 'Dogs'in str(fileRead[x]):
            dog.append(fileRead[x])
        elif 'dogs'in str(fileRead[x]):
            dog.append(fileRead[x])
        elif 'Cats' in str(fileRead[x]):
            cat.append(fileRead[x])
        elif 'cats'in str(fileRead[x]):
            cat.append(fileRead[x])
    newTxt = ''
    newTxt = 'Facts about Dogs' + '\n'
    for x in range(len(dog)):
        newTxt = newTxt + str(dog[x]) + '\n'
    newTxt = newTxt+ '\n\n' + 'Facts about Cats' + '\n'
    for x in range(len(cat)):
        newTxt = newTxt +(str(cat[x])) + '\n'
    print(newTxt)
    posD = newTxt.find('Dogs')
    posC = newTxt.find('Cats')
    print('The word Dogs first appears at index', posD, 'The word Cats first appears at index', posC)
    file = open('C:\\Users\\savan\\Documents\\2021 Spring Semester\\CSCI-200 Prog w Python\\S21_exam2_prob2_text.txt', 'w')
    file.write(str(newTxt))
    file.close
    
prob2()
            
