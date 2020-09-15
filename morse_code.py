def morse_code(target):
    # numbers
    morse_nums = [ '-----', '.----', '..---', '...--', '....-',
                '.....', '-....', '--...', '---..', '----.' ]
    nums = [num for num in range(0, 10)]
    
    # letters
    morse_letters = [ '.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
                    '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
                    '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
                    '-..-', '-.--', '--..' ]
    letters = []
    for alpha in range(ord('A'), ord('Z')+1):
        letters.append(chr(alpha))

    nums_dict= {}
    alphas_dict= {}
    for number in nums:
        nums_dict[number]= morse_nums[number]
    up = 0
    for char in letters:
        alphas_dict[char]= morse_letters[up]
        up += 1
    
    target_element = []
    for one in target:
        if one.isnumeric():
            target_element.append(nums_dict[int(one)])
        elif one.isalpha():
            target_element.append(alphas_dict[str(one.upper())])
        elif one.isspace():
            target_element.append('/')
        elif one == ',':
            target_element.append(',')

    result = (' ').join(target_element)    
    return result