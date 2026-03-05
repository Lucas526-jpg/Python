import string,random

contra = []

cant_string = len(string.ascii_letters)
cant_numbers = len(string.digits)
cant_punctuation = len(string.punctuation)

long = int(input("Ingresa la longitud"))

for i in range(long):
    num=random.randint(1, 3)
    if num==1:
        index=random.randint(0,cant_string-1)
        contra.append(string.ascii_letters[index])
    elif num==2:
        index=random.randint(0,cant_numbers-1)
        contra.append(string.digits[index])
    else:
        index=random.randint(0,cant_punctuation-1)
        contra.append(string.punctuation[index])
print("".join(contra))