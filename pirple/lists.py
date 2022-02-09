TestList = ["Element1", "Element2", "Element3"]

Scores = [70, 85, 67.5, 90, 80]
print(Scores)
print("List ended above")
print(Scores[0])

print("The next is value for index -1")

print(Scores[-1])#last index position
print(Scores[0:2]) #start at index position 0
#up to but not including index position 2

print(Scores[2:]) # up to the end 


Scores[0] = 75
print(Scores[0])

Scores[1] = "I'm text"

print("This is all the list")
print(Scores[0:]) #print all the list
print("Deleting 2nd and 3rd list elements")
print("Remaining list is below")
Scores[1:3] = []#delete elements from index position 1 
#up to but not including the 3rd index position
print(Scores[0:]) #print all the list


OtherScores = [70, 85, 67.5, 90, 80]
print("Other scores are")
print(OtherScores)

OtherScores[0] = [] # delete 1st index element
print(OtherScores[0]) # see 1st index element
print(OtherScores[0:]) # see all the list
OtherScores[0:1] = [] # delete 1st index element
print(OtherScores[0:]) #see all the list

OtherScores[0] = 2
print(OtherScores[0])

OtherScores[0] = ["None","blaBla"]
print(OtherScores[0])
print(OtherScores[0][1])

print(OtherScores[0:])
OtherScores.pop(0)
print(OtherScores[0])
print(OtherScores[0:])

OtherScores.append(99)
print(OtherScores)