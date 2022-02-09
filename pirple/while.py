counter = 1
sum = 0
while counter<=10:
    print(counter)
    sum = sum + counter
    counter += 1

print(sum)


print("##################")

Letters = ["a","b","c","d","e","f"]

lengthLetters = len(Letters)
print(lengthLetters)

print(Letters)

index = 0
while index < len(Letters):
    print("Index number is now: ", index)
    print("String letter is", Letters[index])
    if Letters[index]=="f":
        print("Asta-i litera de 'Faraon'!")
    index += 1

print("#####################")

height = 5000
velocity = 50
time = 0

while height > 0:
    height -= velocity
    time += 1
    print("Current height is: ", height)
    print("Time is now: ", time)

