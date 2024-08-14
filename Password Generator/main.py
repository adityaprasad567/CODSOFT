import string
import random

if __name__ == '__main__':
    Password_length = int(input("Enter the desired length of the password: "))
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    s = []
    s.extend(list(uppercase_letters))
    s.extend(list(lowercase_letters))
    s.extend(list(digits))
    s.extend(list(special_characters))
    
print("Your Desired Password is : ")

print("".join(random.sample(s, Password_length)))
    
    # If want to save this password in text format we use:
    
with open("password.txt", "w") as f:
    f.write("Your Desired Password is : " + "".join(random.sample(s, Password_length)))
    print("Password saved in password.txt")
