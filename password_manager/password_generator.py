import random

sym = ['!' , '"' , '#' , '$' , '%' , '&' , "'" , '(' , ')' , '*' , '+' , ',' , '-' , '.' , '/' , 
       ':' , ';' , '?' , '@' , '[' , ']' , '^' , '_' , '`' , '{' , '|' , '}' , '~']
num = list(range(0, 10))
upper_letter = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
lower_letter = [chr(i) for i in range(ord('a'), ord('z') + 1)]
letter = upper_letter + lower_letter

ls = []
ls.append(num)
ls.append(letter)
ls.append(sym)

print("Welcome to the PyPassword Generator")
length = int(input("Password Length: "))
letters = int(input("Letter count: "))
symbols = int(input("Symbol count: "))
numbers = int(input("Number count: "))

cnt = 0
password = ""
for i in range(length):
    while length > cnt:
        x = random.randint(0, len(ls) - 1)
        y = random.randint(0, len(ls[x]) - 1)
        if ls[x][y] in sym:
            if symbols > 0:
                symbols -= 1
                cnt += 1
            else:
                continue
        elif ls[x][y] in num:
            if numbers > 0:
                numbers -= 1
                cnt += 1
            else:
                continue
        elif ls[x][y] in letter:
            if letters > 0:
                letters -= 1
                cnt += 1
                random.shuffle(letter)
            else:
                continue
        else:
            print("Value Error")
        password += str(ls[x][y])
print(f"Password: {password}")
