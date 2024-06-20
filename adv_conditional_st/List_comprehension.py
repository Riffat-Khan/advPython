List = [34, 5, 23, 8]
double = [x*2 for x in List]
print(double)


List = [char for char in [34, 5, 23, 8]]
print(List)


even = [x for x in [34, 5, 23, 8] if x%2==0]
print(even)


largest = [[j+1 for j in range(0,4)] for i in range(0,4) ]
print(largest)


EvenOdd = ["even" if i%2==0 else "odd"  for i in List]
print(EvenOdd)

multiple5 = [num for num in range(100) if num %5==0]
print(multiple5)

twoD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [[i[j]for i in twoD] for j in range(len(twoD[0]))]
print(transpose)


names = ["riffat" , "nyla" , "rohan" ]
marks = [76 , 65, 98]

name_marks = [[names, marks] for names , marks in zip(names , marks) ]
print(name_marks)

lengths = [len(char) for char in names]
print(lengths)
