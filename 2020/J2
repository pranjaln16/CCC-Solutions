#CCC 2020: J2
#Problem: Epidemiology
#Pranjal Nayak

p = int(input())
n = int(input())
r = int(input())

people_infected = n
lastday_infected = n
output = 0

while people_infected <= p:
  people_infected += lastday_infected * r
  lastday_infected *= r
  output += 1

print(output)
