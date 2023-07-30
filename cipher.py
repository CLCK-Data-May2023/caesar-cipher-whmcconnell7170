sentence = input("Enter Sentence: ")
letters = 'abcdefghijklmnopqrstuvwxyz'
alphabet = []

for i in letters:
    alphabet.append(i)
#print(alphabet)

shifted_letters = {}
for i in range(len(letters)):
    shifted_letters[letters[i]] = letters[(i+5) % len(letters)]

sentence_list = []
for i in sentence:
    sentence_list.append(i)

cipher = []

for i in sentence_list: #for every character in the sentence
    if i.lower() in alphabet: #if the character is in the alphabet
        cipher.append(shifted_letters[i.lower()]) #append the associated shifted letter
    else: #if the character is not in the alphabet
        cipher.append(i)
print('The encrypted sentence is:',''.join(cipher))
        
