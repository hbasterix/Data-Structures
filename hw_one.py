import numpy as np
import math
def is_anagram(s:str,t:str)->bool:
    myMatrix = []
    s=s.upper()
    t=t.upper()

    strOne =""
    strTwo = ""
    strThr =""
    strFr = ""

    for  ch in s:
        if ch not in strThr:
            strThr += ch
    print(strThr)

    for  ch in t:
        if ch not in strFr:
            strFr += ch
    print(strFr)

    for ch in strThr:
        if ch.isalpha():
            strOne += ch

    
    for ch in strFr:
        if ch.isalpha():
            strTwo += ch

    print(strOne)
    print(strTwo)

    for chOne in strOne:
        for chTwo in strTwo:
            if(chOne == chTwo):
                myMatrix.append(1)
            else:
                myMatrix.append(0)

    # Convert to NumPy array
    np_array = np.array(myMatrix)
    print(np_array)
    # Calculate side length for square matrix
    list_length = len(strOne)  
    ''' 
        if math.isqrt(list_length) ** 2 != list_length:
        raise ValueError("The list length is not a perfect square, cannot form a square matrix.")
            list_length = len(myMatrix)
            
    side_length = int(math.sqrt(list_length))
    '''



    # Reshape into a square matrix
    square_matrix = np_array.reshape(list_length, list_length)
    print(square_matrix)
    a = abs(np.linalg.det(square_matrix))
    return a

result = is_anagram("rat","car")
print(result)