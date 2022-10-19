from art import *
from game_data import data
import random

print(logo)

random_num = random.randint(0,50)
# print(data[random_num])
print(f" compare {data[random_num]['name']}, a {data[random_num]['description']}, from {data[random_num]['country']}")
a = data[random_num]['follower_count']
print(a)


print(vs)


random_num2 = random.randint(0,50)
# print(data[random_num])
print(f"  {data[random_num2]['name']}, a {data[random_num2]['description']}, from {data[random_num2]['country']}")
b = data[random_num2]['follower_count']
print(b)

if a > b:
  print("I win")
else:
  print("u win")