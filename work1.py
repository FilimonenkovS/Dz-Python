name = "Serezha"
familiya = "Filimonenkov"
data = "2003"

s = name + "_" + familiya  + "_" + data

print(s)

name, familiya = familiya, name
m = int(data)
data = str(m + 60)

s = name + "_" + familiya  + "_" + data

print(s)
