#Here in this code, I'm asking for User Input
User_Input = input("Write your Phrase")
# The we will split the input of the User using split.()function
User_Split = User_Input.split()
#Now we will make a new Variable that is Empty.
Acronyms = ""
#Now we will create a for loop to iterate through nthe user input and take the first element of each word which will be stored in Acronyms
for i in User_Split:
    Acronyms = Acronyms +i[0].upper()
    print("Your Acronym is", (Acronyms))
