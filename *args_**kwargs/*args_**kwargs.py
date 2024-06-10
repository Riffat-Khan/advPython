def number(*num):
    print(num , type(num) )
    for num in num: print(num+num)

number((4,6),(4,78))


def data(**info):
    print(info)

data(anil=40 , akash=45, zain=13)

def sum(**Age):
    sum = 0
    for x in Age.values():
        sum+=x
    print(sum)


sum(anil=40 , akash=45, zain=13)