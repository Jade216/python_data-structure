def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
#    result = {}
#    count = 0
#    for char in phrase:
#        if char not in result:
#            count += 1
#            result[char] = count

#    return result

# why the above is not correct???
    

    result = {}
    for char in phrase:
        result[char] = result.get(char, 0) + 1

    return result