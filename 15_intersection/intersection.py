def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    return list(set(l1) & set(2))

#..............................................................
#    set2 = set(l2)

#    return [val for val in l1 if val in set2]

# Why convert l2 to a set? does need to covert l1 to a set too? 
#in this case, if l1 has duplicat numbers which also match l2, will the final list contain multiple same numbers? 