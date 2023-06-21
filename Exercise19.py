def total(a,b,c):
    sum = a + b + c
    return sum

math = int(input("Please input mark for Math : "))
eng = int(input("Please input mark for English : "))
physic = int(input("Please input mark for Physic : "))

all_mark = total(math,eng,physic)
print(all_mark)