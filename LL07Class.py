#problem 1
import json
def main():
    '''Get the input and print JSON data.'''
    j = input('enter the data: ')
    jkv = jsonTodict(j)
    jk = jkv[0]
    jv = jkv[1]
    print(str(jk)+' \n', str(jv))

def jsonTodict(j):
    '''parse JSON text into Python lists'''
    dj = json.loads(j)
    k = list(dj.keys())
    v = list(dj.values())
    jkv = dictTojson(k, v)
    return jkv

def dictTojson(k, v):
    '''Parse Python lists to JSON arrays.'''
    jk = json.dumps (k)
    jv = json.dumps (v)
    return jk, jv

#if __name__ == '__main__':
    #main()
#problem 2
#import json above
# use module variable (a module-level variable) json1 for input data
json1 = '{"champion":{"year":1972, "player": "Rod Carew", "club": "Minnesota", "mean": 0.318}}'
def main2():
    '''Get the input and output JSON data.'''
    jkv = jsonToPy(json1)#a module variable can be used anywhere in the module.
    jk = jkv[0]
    jvk = jkv[1]
    jvv = jkv[2]
    print(' ' + str(jk) + '\n', str(jvk)+'\n',str(jvv))
def jsonToPy(j):
    '''parse JSON data into Python lists'''
    jstr = str(j)
    d = json.loads(jstr)
    k = list(d.keys())
    v = list(d.values())
    vk = list(v[0].keys())
    vv = list(v[0].values())
    jkv = pyTojson(k, vk, vv)
    return jkv
def pyTojson(x1, x2, x3 =None):
    '''parse Python lists into JSON data'''
    jk = json.dumps(x1)
    jvk = json.dumps(x2)
    jvv = json.dumps(x3)
    return jk, jvk, jvv
#main2()

#problem 3
# Using a module variable named data
data = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13','14', '15', '16', '17', '18', '19', '20', '30', '40', '50', '60', '70', '80', '90']
def main3():
    '''get the data and print the numbers'''
    numlist = get_numlist(int, data)
    print(numlist)
def get_numlist(int, data):
    '''convert the data items into numbers'''
    nlist = map(int, data)
    numlist = list(nlist) #get the content of nlist
    return numlist
# or
'''def main3():
    data = strToInt([ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13','14', '15', '16', '17', '18', '19', '20', '30', '40', '50', '60', '70', '80', '90'])
    print(data)
def strToInt(data):
    dataInt = []
    for i in data:
        dataInt.append(int(i))
    return dataInt'''
main3()
