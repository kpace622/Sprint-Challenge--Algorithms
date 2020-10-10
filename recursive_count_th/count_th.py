'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''



def count_th(word, count=0, idx_one=0, idx_two=1):

    # Turn the word into a list
    arr = list(word)

    # Declare starting indexes to inspect the list
    # # Keep count of how many times 'th' appears

    # Base Case, If you get to the end of the list stop the recursion
    if idx_two + 1 > len(arr):
        return count

    # If the two indexes fulfill this requirement increment the count and then recall the function using + 1 on both indexes 
    if arr[idx_one] == 't' and arr[idx_two] == 'h':
        count += 1
        idx_one += 1
        idx_two += 1
        return count_th(word, count, idx_one, idx_two)

    # Otherwise continue moving through the array, incrementing the indexes
    else: 
        idx_one += 1
        idx_two += 1
        return count_th(word, count, idx_one, idx_two)
