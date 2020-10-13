def checkEmpty(input, pattern): 
      
    if len(input) == 0: 
        return False
    
    index = input.find(pattern)
    if (index == (-1)): 
        return False

    # slice input string in two parts and concatenate 
    input = input[0:index] + input[index + len(pattern):]

    if len(input):
        return True
        
    checkEmpty(input, pattern)


if __name__ == "__main__": 
    input = 'GEEGEEKSKS'
    pattern ='GES'
    # pattern ='GEEKS'
    print(checkEmpty(input, pattern))