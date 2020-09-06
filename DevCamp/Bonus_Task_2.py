import string 

letters = list(string.ascii_lowercase) # letters element will be stored in a list 
vowels = ["a", "e", "i", "o", "u", ' '] # vowels created in a list
words = 'hello world'
new = ''
for let in words: # iterate through 'words' variable
    if let not in vowels: # if element is not a vowel
        for i, letter in enumerate(letters): # iterate through letters
            if let == letter: # if element is the same as the ltter
                new = new + letters [i+1] # new is now letter          
    else:
        new += let # else new is new + element
print(new)
