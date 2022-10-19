
order = input("hi what pizza do u like 's' for small 'm' for medium or 'l' for large: ")

bill = 0 


if order == "s":
  print(f"your bil is {bill+3}")
  bill +=3
elif order == "m":
  print(f"your bil is {bill+5}") 
  bill +=5
elif order == "l":
  print(f"your bil is {bill+ 8}")
  bill +=8


cheese = input("do you want cheeese for £2 extra y/n: ")
if cheese == "y":
  print(bill+2)
  bill+=2

egg = input("do you want egg for £1 extra y/n: ")
if egg == "y":
  print(bill+1)
  bill+=1

bacon = input("do you want extra bacon for £3 extra y/n: ")
if bacon == "y":
  print(bill+3)
  bill+=3
