import ascii
import random
import string

letters = int(input("how many letters do u want in your password: "))
symbols = int(input("how many symbols do u want in your password: "))
numbers = int(input("how many numbers do u want in your password: "))

all_numbers = ["1","2","3","4","5","6","7","8","9","0"]

all_letters = (list(string.ascii_uppercase))
all_symbols = (list(string.printable)[-38:-26])

pass_numbers = []
pass_letters = []
pass_symbols = []


#######
for x in range(numbers) :
  pass_numbers.append(all_numbers[random.randint(0,9)])
  #111111pass_numbers.append(random.choice(all_numbers))

######
print(pass_numbers)

for x in range(letters) :
  pass_letters.append(all_letters[random.randint(0, 26)])
  #111111pass_numbers.append(random.choice(all_numbers))

#####
print(pass_letters)

for x in range(symbols) :
  pass_symbols.append(all_symbols[random.randint(0,10)])
  #111111pass_numbers.append(random.choice(all_numbers))


print(pass_symbols)

print("****************")

password = (pass_numbers + pass_letters + pass_symbols)
print(password)

random.shuffle(password)

print(password)


final_pass = "".join(password)
print("****************")
print(final_pass)