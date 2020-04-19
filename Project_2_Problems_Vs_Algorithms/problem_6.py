def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == []:
        return (None,None)

    #min=ints[0]
    #max=ints[0]
    for val in ints:
        if val < min:
           min = val
        if val > max:
            max = val
    #print([min,max])
    return tuple([min,max]) 

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l1=list(range(1,1000))
random.shuffle(l1)
print ("Pass" if ((min(l1), max(l1)) == get_min_max(l1)) else "Fail")

l2=list(range(-1000,1000))
random.shuffle(l2)
print ("Pass" if ((min(l2), max(l2)) == get_min_max(l2)) else "Fail")

l3=[5]
random.shuffle(l3)
print ("Pass" if ((min(l3), max(l3)) == get_min_max(l3)) else "Fail")

l4=[]
random.shuffle(l4)
print ("Pass" if ((None,None)) == get_min_max(l4) else "Fail")

