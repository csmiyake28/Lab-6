#def encoder
#Caio #Mike

# this is the encode function:
def encode(password):
    encoded_pass = ''
    #takes in each character
    for char in password:
        #adds three to the pass word
        char = int(char) + 3
        encoded_pass += str(char)
    # returns modified pass word
    return encoded_pass

#Placeholder for team member
#This is the decode function
def decode(encoded_password):
    decoded_pass = ""
    for char in encoded_password:
        char = int(char) - 3 #Subtracts 3 characters from entered digits
        decoded_pass += str(char)
        #Returns new pass


    return decoded_pass



Continue = True
#While loop
while Continue:
    print('\nMenu \n------------- \
            \n1. Encode  \
            \n2. Decode \
            \n3. Quit \n')

    option = int(input('Please enter an option: '))

    if option == 1:
        password = input('Enter your password to encode: ')
        # here you encode your password and store it!
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')


        pass
    if option ==2:
        original_pass = decode(encoded_password) #Sets original_pass to decoded version of the encoded password
        print(f'The encoded password is {encoded_password}, and the original password is {original_pass}.') #string allows looped function
        pass
    if option == 3:
        Continue = False #Stops loop











