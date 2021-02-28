#CCC 2020: J3
#Problem: Art
#Pranjal Nayak

n = int(input())

x = []
y = []

for i in range(n):
    xpoint , ypoint = input().split(',')
    x.append(int(xpoint))
    y.append(int(ypoint))

print(f"{min(x)-1},{min(y)-1}")
print(f"{max(x)+1},{max(y)+1}")
