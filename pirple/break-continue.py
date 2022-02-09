Participants = ["Jen","Alex","Tina","Joe","Ben"]

position = 1
for name in Participants:
    if name == "Tina":
        break
    print("Current position is: ", position, "About to increment")
    position += 1

print(position)
 

for currentIndex in range(len(Participants)):
    print("Participant index is: ", currentIndex)
    #print("Participant here is: ", Participants[currentIndex])
    if Participants[currentIndex] == "Joe":
        print("I've found Joe! He is the position number",currentIndex+1)
        break
    print("Not breaked")

for number in range(10):
    if number%3 == 0:
        print(number, "is divisble by 3")
        continue
    print(number,"Is not divisible by 3")


