import random
import os

rock = """                 _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
"""
paper = """ _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|       """
scissors = """_           ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\."""

cpu_options = ["rock", "paper", "scissors"]
cpu = random.choice(cpu_options) 

print(cpu)
you =""

while you != "q":
  print(" ")
  you = input("type 'p' for paper, 's' for scissors, 'r' for rock or 'q' to QUIT: ")
  os.system('clear')
  print("proba")
  cpu_options = ["rock", "paper", "scissors"]
  cpu = random.choice(cpu_options) 

  
  if you == "r":
    print(f"your choice is: \n {rock}")
  elif you == "p":
    print(f"your choice is:  \n {paper}")
  elif you == "s":
    print(f"your choice is:  \n {scissors}")

  print(" ")
  print("VS")
  print(" ")
    
  if cpu == "rock":
    print(" ")
    print(f"cpu choice is :  \n {rock}")
  elif cpu == "paper":
    print(" ")
    print(f"cpu choice is :  \n {paper}")
  elif cpu == "scissors":
    print(" ")
    print(f"cpu choice is :  \n {scissors}")
  print(" ")  
  print("################################################################### ")
  print(" ")
  if you == "r" and cpu == "paper":
    print("*****CPU WINS*****")
  elif you == "s" and cpu =="paper":
    print("*****YOU WIN*****")
  elif you == "p" and cpu =="paper":
    print("*****DRAW*****")
  
  if you == "r" and cpu == "rock":
    print("*****DRAW*****")
  elif you == "s" and cpu =="rock":
    print("*****CPU WINS*****")
  elif you == "p" and cpu =="rock":
    print("*****YOU WIN*****")
  
  if you == "r" and cpu == "scissors":
    print("*****YOU WIN*****")
  elif you == "s" and cpu =="scissors":
    print("*****DRAW*****")
  elif you == "p" and cpu =="scissors":
    print("*****CPU WINS*****")

  print(" ")  
  print("################################################################### ")