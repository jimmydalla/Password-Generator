import random
digits = ['0','1','2','3','4','5','6','7','8','9']
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = []

for i in lowercase:
  uppercase.append(i.upper())

special_characters = ['[','@','_','!','#','$','%','^','&','*','(',')','?','/','|','}','{','~',':',']']
password = int(input("Enter the required length of the password: "))
password_empty = []

if password<=8:
  print("Please choose the right length")
elif password>=20:
  print("Please choose the right length")
else:
 while len(password_empty)<password:
  num = random.choice(digits)
  password_empty.append(num)
  
  low = random.choice(lowercase)
  password_empty.append(low)
  
  upper = random.choice(uppercase)
  password_empty.append(upper)

  special = random.choice(special_characters)
  password_empty.append(special)

new_password = ''.join(password_empty)
print(new_password[0:password])