import itertools

count = 0
for i in itertools.cycle("ABC"):
    print(i,end ="")
    count+=1
    if count >= 10: break

print("\n")

List = ["welcome" , "to" , "the" ,  "show"] 

index = 0
for string in itertools.cycle(List):
    print(string , end = " ")
    index+=1
    if index >=30: break
    elif index%4==0: print("\n")

