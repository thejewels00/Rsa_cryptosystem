


def int_to_message(int_list):
    return "".join([chr(i) for i in int_list])



def decrypt(encrypted_int_list, d, n):
    decrypted_int_list = [pow(c, d, n) for c in encrypted_int_list]
    return int_to_message(decrypted_int_list)


n = 2773
e = 17

d = int(input("Your key  :D : "))
print(d)

encrypted_int_list = input("Press ur list : ")
encrypted_int_list = encrypted_int_list.strip("[] ")

str_list = encrypted_int_list.split(',')


int_list = [int(x) for x in str_list]

decrypted_message = decrypt(int_list, d, n)



print(decrypted_message)