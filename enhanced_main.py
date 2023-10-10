import random
import string

# ASCII Art and User Interface
print("Welcome to the")
print(r"""
  ____             ____                                          _    
 |  _ \ __ _ _ __ |  _ \ ___  ___ ___  _ __ ___  _ __ ___   __ _| | __
 | |_) / _` | '_ \| |_) / _ \/ __/ _ \| '_ ` _ \| '_ ` _ \ / _` | |/ /
 |  __/ (_| | |_) |  __/  __/ (_| (_) | | | | | | | | | | | (_| |   < 
 |_|   \__,_| .__/|_|   \___|\___\___/|_| |_| |_|_| |_| |_|\__, |_|\_\
            |_|                                           |___/      
""")
print("The secure password generator!\n")

# User input
try:
    nr_letters = int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
except ValueError:
    print("Oops! That was not a valid number. Try again...")
    exit()

# Character pools
letters = string.ascii_letters
numbers = string.digits
symbols = '!#$%&()*+'

# Generate characters for the password using list comprehensions
selected_letters = [random.choice(letters) for _ in range(nr_letters)]
selected_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
selected_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

# Combine all the selected characters
password_characters = selected_letters + selected_symbols + selected_numbers

# Shuffle the characters to ensure randomness
random.shuffle(password_characters)

# Convert the list of characters into a string
password = ''.join(password_characters)

# Displaying the password creatively
print("\nGenerating a strong password for you...\n")
print(f"Here is your password:\n{'*' * len(password)}")
print(f"{password}")
print(f"{'*' * len(password)}\n")
print("Make sure to store your password securely!\n")

print(r"""
      _____                  _      
     |  __ \                | |     
     | |__) |_ _ _   _  __ _| | ___ 
     |  ___/ _` | | | |/ _` | |/ _ \
     | |  | (_| | |_| | (_| | |  __/
     |_|   \__,_|\__,_|\__, |_|\___|
                        __/ |       
                       |___/        
""")

print("Thank you for using PyPassword Generator! Stay Secure 🛡️")
