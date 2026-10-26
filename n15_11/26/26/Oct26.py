def has_duplicate_letter(word):
    result = False
    for i in range(0, len(word)-1): #Letter one
        for j in range(i+1, len(word)): #Compare to every other letter
            if word[i] == word[j]:      #Once a letter is checked, it 
                result = True           #doesn't need to be checked again.
    return result                       #You don't need to look at previous letters!

#This function will take a word, look at each letter, look at every other letter, 
#and then tell you if it has a duplicate letter somewhere in the word.