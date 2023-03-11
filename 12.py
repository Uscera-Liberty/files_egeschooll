f = open('24.txt')
mxs = ''
while f.readline() :
    x = f.readline()
    print(x)
    k = ''
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            k += x[i]
        else:
            k = k + str(x[i]) + str(x.count(x[i]))
            if mxs == '':
                mxs = k
            elif (int(mxs[-1]) < x.count(x[i])) or  len(mxs) <= len(k):
                mxs = k
                print(mxs)
            k = ''
print(mxs)
