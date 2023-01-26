ecoli = open("./data/ecoli_data.txt")
line1 = ecoli.readline()
line2 = ecoli.readline()
line3 = ecoli.readline()
for x in [line1, line2, line3]:
    name, c1, c2, c3, c4, c5, c6, c7, c8 = x.strip().split()
    print(name, type(name))
    for y in [c1, c2, c3, c4, c5, c6, c7]:
        y = float(y)
        print(y,type(y))
    print(c8, type(c8))
one= open("./data/second.txt", "w")

print(ecoli, file=one)
second = open(file="./data/second.txt", encoding="UTF-8")
print(second.read())
print(open("./data/ecoli_data.txt").read())
ecoli.close()

def my_function():
    print("hello world")
    return 1

def addition(val1, val2):
    result = val1 + val2
    return result

sum1=addition(100, 200)
print(sum1)
sum1 = addition(100, 200)
sum2 = addition(500, -700)
total = addition(sum1, sum2)
print(total)

newfile=ecoli.readlines()[0:10]

for z in xrange(10):
    line+"z"=ecoli.readline()
    get_next_line 

from sys import argv
script, the_file = argv

def get_next_line(file):
    l1=file.readline().strip().split()
    l2=file.readline().strip().split()
    l3=file.readline().strip().split()
    l4=file.readline().strip().split()
    l5=file.readline().strip().split()
    l6=file.readline().strip().split()
    l7=file.readline().strip().split()
    l8=file.readline().strip().split()
    l9=file.readline().strip().split()
    l10=file.readline().strip().split()
    return l1, l2, l3, l4, l5, l6, l7, l8, l9, l10

l1, l2, l3, l4, l5, l6, l7, l8, l9, l10 = get_next_line(ecoli)

rowvals = get_next_line(ecoli)   
sum2 = 0
for p in range(10):
    sum2 += float(rowvals[p][1])
print(sum2)


def sum_data(input1):
    summary=[]
    for q in range(1,8):
        temp = 0 
        for p in range(10):
            temp += float(input1[p][q])
        summary.append(temp)
    return summary

sum_data(get_next_line(ecoli))
