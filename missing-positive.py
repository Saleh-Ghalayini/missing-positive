def first_missing_positive(numbers):
    
    #these will be used to store the positive numbers greater than zero and to find the first missing number
    positive_numbers = []
    missing = 1

    for i in range(len(numbers)):

        #if the number is greater than zero it will be appended to the positive numbers list
        if(numbers[i] > 0):
            positive_numbers.append(numbers[i])
    #sorting the positive numbers chosen from the original numbers list
    positive_numbers.sort()

    for i in range(len(positive_numbers)):
        
        #checking if the number in the list is equal to the missing if it is that means that its contained to the list
        #so we increment missing by one to checking the next number
        if(positive_numbers[i] == missing):
            missing += 1
    
    #returning the first missing positive number
    return missing
#sending values to the function
print(first_missing_positive([0, 3,2, 5, 7, 4, -1, 1]))