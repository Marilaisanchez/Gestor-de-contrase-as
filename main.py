import random as r , string as s

elements = s.ascii_letters + s.ascii_lowercase + s.ascii_uppercase + s.punctuation + s.digits
password = ""
longitud = int(input("¿Qué tan larga será la contraseña?"))

for i in range(longitud):
    password += r.choice(elements)

print(password)