import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','^','&','*','(',')','+','?']
numbers = ['0','1','2','3','4','5','6','7','8','9']

num_letters = int(input("Enter number of letters required in password? \n"))
num_symbols = int(input("Enter number of symbols required in password? \n"))
num_numbers = int(input("Enter number of numbers required in password? \n"))

pswd_list = []
password = ''
for i in range(1,num_letters+1):
    a = random.choice(letters)
    pswd_list.append(a)
for i in range(1,num_symbols+1):
    a = random.choice(symbols)
    pswd_list.append(a)
for i in range(1,num_numbers+1):
    a = random.choice(numbers)
    pswd_list.append(a)

print("Generated password list : ",pswd_list)
random.shuffle(pswd_list)
print("Shuffled password list : ",pswd_list)
for i in pswd_list:
    password += i
print("Final password : ",password)