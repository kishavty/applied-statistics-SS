f = open("age_at_mar.txt", "r")
data = f.read()
l=[]
def func():
    for i in range(len(data)):
        if data[i] == ",":
            l.append(data[i+1])
            l.append(data[i+2])
    li = [''.join(l[i:i+2]) for i in range(0, len(l), 2)]
    return li

sample = func()

with open("staty.txt", "w") as f:
    for i in sample:
        f.write(i)
        f.write(",")
