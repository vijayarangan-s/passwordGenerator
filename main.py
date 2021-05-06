import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#',"$",'%','^','&','(',')',"*"]

print("welcome to password generator")
nr_letter = int(input("How many letters would you in your pwd"))
nr_number = int(input("How many numbers would you in your pwd"))
nr_symbol = int(input("How many symbols would you in your pwd"))

#Easy Method
pwd = ""
for ch in range(1, nr_letter+1):
  pwd += random.choice(letters)

for n in range(1, nr_number+1):
  pwd += random.choice(numbers)

for s in range(1, nr_symbol):
  pwd += random.choice(symbols)

print(pwd)

#hard method
pwd_list = []
for ch in range(1, nr_letter+1):
  pwd_list.append(random.choice(letters))

for n in range(1, nr_number+1):
  pwd_list.append(random.choice(numbers))

for s in range(1, nr_symbol):
  pwd_list.append(random.choice(symbols))

random.shuffle(pwd_list)
password = "".join(pwd_list)

print(password)
 