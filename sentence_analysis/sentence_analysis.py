import string

sentence = input("Please enter the sentence: ")
strpunc = string.punctuation
punctu = 0
upper = 0
lower = 0


#Lenght of the sentence without spaces and number of spaces
sen_leng = len(sentence)
spaces = sentence.count(" ")
real_lenght = sen_leng - spaces

#punctuations characters
for i in sentence:
    if i in strpunc:
        punctu += 1


#Count of uppercases
for i in sentence:
    if i.isupper() == True:
        upper += 1

#Count of lowercases
for i in sentence:
    if i.isupper() == False:
        lower += 1
lowerup = lower - spaces - punctu


print("Upper case: ", upper)
print("Lower case: ", lowerup)
print("Punctuation: ", punctu)
print("Total chars: ", real_lenght)


