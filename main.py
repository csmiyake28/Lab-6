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
def decode(encoded_password):
    pass



Continue = True
#While loop
while Continue:
    print('Menu \n------------- \
            \n1. Encode  \
            \n2. Decode \
            \n3. Quit ')

    option = int(input('Please enter an option: '))

    if option == 1:
        password = input('Enter your password to encode: ')
        # here you encode your password and store it!
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')


        pass
    if option ==2:
        pass
    if option == 3:
        Continue = False











