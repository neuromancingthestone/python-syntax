def print_upper_words(list, must_start_with):
    """Takes a list of strings and prints them out in upper case"""    
    for words in list:
        for letter in must_start_with:
            if(words[0] == letter):
                print(words.upper())
