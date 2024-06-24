import random 
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
youStr = input("Enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
you = youDict[youStr]

reverseDict = {1:"Snake",-1:"Water",0:"Gun"}
print(f"You chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if (computer==you):
  print("its a Draw")
elif(computer == -1 and you == 1):
  print("You Win")

elif(computer == -1 and you == 0):
  print("You Lose")

elif(computer == 1 and you == -1):
  print("You Lose")
  
elif(computer == 0 and you == -1):
  print("You Win")  

elif(computer == 0 and you == 1):
  print("You Lose")  

else:
  print("Something Went Wrong")





