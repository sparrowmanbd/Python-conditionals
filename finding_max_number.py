#list
numbers=[72,5,1000,60,500,6,800,9]

#declared a variable that holds the first value of the list
max_number=numbers[0]

#iterating over the lists by loop
for number in numbers:
    #set a condition that indicates if number variable is greater than max_number then it will 
    #assign the new value in max_number.
    if(number>max_number):
        max_number=number

print(f"The maximum number in the list is {max_number}")