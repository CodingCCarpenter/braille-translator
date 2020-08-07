"""TESTS 1 & 4 PASS with CODE:

    # steps to solution
    # 1 - define characters
        # a - convert string to list
        # b - create a dictionary with alphabet
    # 2 - identify capital letters or casing  
    # 3 - insert capitalization mark 000001 where needed
    # 4 - account for spaces
    # 5 - convert letters to braille sequences

def solution(s):
    ''' 
    function that takes a string parameter 
    and produces a string of 1s and 0s 
    representing the Braille equivalent
    '''
    
    # Initialize string to hold converted characters
    braille_list = []
    
    # Defining braille values using a dictionary
    braille = {
        'caps': '000001',
        ' ': '000000',
        'a': '100000',
        'b': '110000',
        'c': '100100',
        'd': '100110',
        'e': '100010',
        'f': '110100',
        'g': '110110',
        'h': '110010',
        'i': '010100',
        'j': '010110',
        'k': '101000',
        'l': '111000',
        'm': '101100',
        'n': '101110',
        'o': '101010',
        'p': '111100',
        'q': '111110',
        'r': '111010',
        's': '011100',
        't': '011110',
        'u': '101001',
        'v': '111001',
        'w': '010111',
        'x': '101101',
        'y': '101111',
        'z': '101011'
    }

    # Converting string to iterable list
    s_list = list(s)
    
    # iterating over s_list and converting
    for letter in s_list:
        
        #check case of character and append cap mark
        if letter.isupper():
            braille_list.append(braille['caps'] + braille[letter.lower()])
        else:
            braille_list.append(braille[letter])
    
    # join into single string and return
    return ''.join(braille_list)
"""

def solution(s):
    ''' 
    function that takes a string parameter 
    and produces a string of 1s and 0s 
    representing the Braille equivalent
    '''
    
    # Initialize string to hold converted characters
    braille_list = []
    
    # Defining braille values using a dictionary
    braille = {
        'caps': '000001',
        ' ': '000000',
        'a': '100000',
        'b': '110000',
        'c': '100100',
        'd': '100110',
        'e': '100010',
        'f': '110100',
        'g': '110110',
        'h': '110010',
        'i': '010100',
        'j': '010110',
        'k': '101000',
        'l': '111000',
        'm': '101100',
        'n': '101110',
        'o': '101010',
        'p': '111100',
        'q': '111110',
        'r': '111010',
        's': '011100',
        't': '011110',
        'u': '101001',
        'v': '111001',
        'w': '010111',
        'x': '101101',
        'y': '101111',
        'z': '101011'
    }

    # Converting string to iterable list
    s_list = list(s)
    
    # iterating over s_list and converting
    for letter in s_list:
        
        #check case of character and append cap mark
        if letter.isupper():
            braille_list.append(braille['caps'] + braille[letter.lower()])
        else:
            braille_list.append(braille[letter])
    
    # join into single string and return
    return ''.join(braille_list)

# test calls
print(solution('code'))
print(solution('Code'))
print(solution('CoDe'))
print(solution('CODE'))
print(solution('CO DE'))


