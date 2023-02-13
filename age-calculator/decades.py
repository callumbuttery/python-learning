age = int(input('How old are you?\n'))

#// allows us to divide and pull out the whole number
#e.g. 50 / 10 = 5.0
#e.g. 50 // 10 = 5
decades = age // 10

years = age % 10
print("You are " + str(decades) + " decades and " + str(years) + " years old")