def is_palindrome_after_char_deletion(word):
    ''' 
    This function checks wether the string is palindrome or not
    args:
    word (string) : the string to be checked out
    '''
    #print(word[::-1])
    return word == word[::-1]
