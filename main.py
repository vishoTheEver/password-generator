#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = [letters, numbers, symbols]
user_coded_letters = []
user_coded_symbols = []
user_coded_numbers = []
for n1 in range(0, nr_letters):
  target_letters = letters[random.randint(0, len(letters) - 1)]
  user_coded_letters.append(target_letters)
  # print(user_coded_letters)
for n2 in range(0, nr_symbols):
  target_symbols = symbols[random.randint(0, len(symbols) - 1)]
  user_coded_symbols.append(target_symbols)
  # print(user_coded_symbols)
for n3 in range(0, nr_numbers):
  target_numbers = numbers[random.randint(0, len(numbers) - 1)]
  user_coded_numbers.append(target_numbers)
  # print(user_coded_numbers)

target_password = user_coded_letters + user_coded_symbols + user_coded_numbers
# print(target_password)
random_password_listed = []

for n4 in range(0, len(target_password)):
  target_password_items = target_password[random.randint(0, len(target_password) - 1)]
  random_password_listed.append(target_password_items)
  # print(random_password_listed)

target_password_2 = []
for n5 in range(0, len(target_password)):
  super_target_password = target_password[random.randint(0, len(target_password) - 1)]
  target_password_2.append(super_target_password)
  # print(target_password_2)

n = 0
word = ""
for n6 in range(0, len(target_password)):
  n = n + 1
  word = word + target_password_2[n - 1]
print(f"Here is your password: {word}")
