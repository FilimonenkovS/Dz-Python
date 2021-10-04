
years = int(input("Years - "))

time = years * 365 * 24 * 60
print("Minutes -", time)
print("You will see", time//5, "exponauts")


exp = int(input("Exponats - "))

print(exp * 5, "minutes")
print(exp * 5 // 60, " hours")
print(exp * 5 // 60// 24, "days")
print(exp * 5 // 60// 24 // 365, "years")
