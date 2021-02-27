#CCC 2021: J2
#Problem: Silent Auction
#Pranjal Nayak

a = int(input())

bidder = []
money = []

for i in range(a):
    person = input()
    bid = int(input())

    bidder.append(person)
    money.append(bid)


winner = ""
largest_bid = 0

for x in range(a):

    if largest_bid < money[x]:
        largest_bid = money[x]
        winner = bidder[x]

print(winner)
