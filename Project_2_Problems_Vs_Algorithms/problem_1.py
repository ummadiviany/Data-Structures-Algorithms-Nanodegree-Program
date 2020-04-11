def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or number < 0:
        return 0
    if number ==0 or number == 1:
        return number
    
    val=number//2

    less = False
  #  c=0
    while(val>0):
        #print(val)
        if val * val == number:
            return val
        
        elif val * val > number :
            
            if less == False:
                val //=2
            else:
                break

        else:
            val +=1
            less=True
        

   #     c+=1

    #print("No of iterations:"+str(c))
    return val-1


    

    #return (int(number**0.5))

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (10 == sqrt(100)) else "Fail")
print ("Pass" if  (0 == sqrt(None)) else "Fail")
