import random

def shownum():
  print(str(number[0])+str(number[1])+str(number[2])+str(number[3]))

number = []
mega = 0
mind = 0

while True:
    y = random.randint(0,9)
    if y not in number:
      number.append(y)
    if len(number) == 4:
      break

print("Welcome to M E G A M I N D\n")
print("I have randomly generated a 4 digit number, but none of the digits are identical, can you guess my number?\nOh, by the way, for every 'Mega' you have it means you have a digit correct, but in the wrong place, and every 'Mind' you have means you have a right number in the right place\nE.g:\nGenerated number: 4379\nPlayer guess = 1396\nThe player would get 1 Mega and 1 Mind for having the 3 in the right place and having the 9 guessed correctly")

guess = str(input("\nWhat is your 4-digit guess?\n"))
for i in range(4):
  if guess[i] in number and guess[i] != number[i]:
    mega = mega + 1
  print(guess[i])
for i in range(4):
  if guess[i] in number and guess[i] == number[i]:
    mind = mind + 1
  print(guess[i])
print(mega)
print(mind)
shownum()
