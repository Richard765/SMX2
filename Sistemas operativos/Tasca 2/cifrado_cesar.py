import argparse
import pdb

def crypt_message(message):
    # Transform message to uppercase
    message = message.upper()
    print("Crypt Message ", message)
    ascii_lista = [ord(caracter) for caracter in message]
    print("Message with ASCII code: ", ascii_lista)  
    sol=[]
    for i in ascii_lista: 
        sol.append(i+3)
    print("Crypted text: ", sol)
    crypted = [chr(codigo) for codigo in sol]
    final_crypted = ''.join(crypted)
    print("Crypted :", final_crypted)

def decrypt_message(message):
    # Transform message to uppercase
    message = message.upper()
    print("Decrypt Message ", message)
    ascii_lista = [ord(caracter) for caracter in message]
    print("Message with ASCII code: ", ascii_lista)  
    sol=[]
    for i in ascii_lista: 
        sol.append(i-3)
    print("Crypted text: ", sol)
    crypted = [chr(codigo) for codigo in sol]
    final_crypted = ''.join(crypted)
    print("Crypted :", final_crypted)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help="cript message")
    parser.add_argument("-d", help="decript message")
    args = parser.parse_args()

   #pdb.set_trace()

    # Crypt message
    if args.c:
        crypt_message(args.c)

    # Decrypt message
    if args.d:
        decrypt_message(args.d)
    
