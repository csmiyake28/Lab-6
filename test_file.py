def decode(encoded_password):
    pass
    decoded_pass = ""
    for char in encoded_password:
        char = int(char) - 3
        decoded_pass += str(char)

    return decoded_pass

print(decode('45678888'))