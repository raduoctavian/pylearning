click = False

Like = 0

click = True

if click == True:
    Like += 1
    click = False

print(Like)

Temperature = 20
Thermo = 15

print(Thermo)

if Temperature <= 15:
    print("It's too cold")
    Thermo += 5

print(Thermo)

if Temperature >= 20:
    print("It's too hot")
    Thermo -= 3

print(Thermo)

Time = "Morning"
Sleepy = False
Pajamas = "Unknown"
InBed = True
print(Pajamas)

if Time == "Night": #and Sleepy == True:
    Pajamas = "On"
elif Time == "Morning" and InBed == False:
    Pajamas = "On"
else:
    print("I'm in else statement")
    Pajamas = "On"

print(Pajamas)