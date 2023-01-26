ecoli = open("./data/ecoli_data.txt").read()
line1 = ecoli.readline().strip()
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