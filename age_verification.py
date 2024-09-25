#User give his age by using user input function
# If age from 0-17:"You are a child"
#If age from 18-36:"You are young"
#If age from 37-45:"You are still young!"
#If age from 46-above:"You are an old man"

age=6

if age>=46:
    print("You are an old man")
elif age>=37 and age<=45:
    print("You are still young!")
elif age>=18 and age<=36:
    print("You are young!")
else:
    print("You are a child!")


