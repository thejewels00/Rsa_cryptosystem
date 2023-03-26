
def message_to_int(message):
    return [ord(c) for c in message]


def encrypt(message, e, n):
    int_list = message_to_int(message)
    encrypted_int_list = [pow(c, e, n) for c in int_list]
    return encrypted_int_list

n = 2773
e = 17

message = input("Your Message : ")
encrypted_int_list = encrypt(message, e, n) 
print(encrypted_int_list)