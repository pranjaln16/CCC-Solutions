#CCC 2021: J3
#Problem: Secret Instructions
#Pranjal Nayak

array1 = []
array2 = []
idk = ""

while True:
  x = input()
  if x == "99999":
    break 

  else:
    array1.append(x)

for ok in range(len(array1)):
    a = array1[ok]
    array3 = []
    array4 = []
    array2 = list(map(str, a))

    array3.append(str(array2[0]))
    array3.append(str(array2[1]))
    array4.append(str(array2[2]))
    array4.append(str(array2[3]))
    array4.append(str(array2[4]))

    if ((int(array3[0]) == 0) and (int(array3[0]) == 0)):
      print(idk + " " + array4[0] + array4[1] + array4[2])

    elif ((int(array3[0]) + int(array3[1])) % 2 == 0):
      print("right " + array4[0] + array4[1] + array4[2])
      idk = "right"

    elif ((int(array3[0]) + int(array3[1])) % 2 != 0):
      print("left " + array4[0] + array4[1] + array4[2])
      idk = "left"

    else:
      break
