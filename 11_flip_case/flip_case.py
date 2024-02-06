def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    if to_swap.islower():
        return phrase.replace(to_swap, to_swap.upper())

    elif to_swap.isupper():
        return phrase.replace(to_swap, to_swap.lower())