logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def encode(message):
    shift = None
    while True:
        try:
            shift = int(input("Type the shift number from 1 to 20: "))
        except:
            print("Wrong input!")
            continue
        finally:
            if 0 < shift <= 20:
                break
            else:
                print("Wrong input!")
                continue
    encrypted = ""
    for letter in message:
        encrypted = encrypted + chr(ord(letter)+shift)
    print(f"Here is your encrypted text: {encrypted}")
    print("***************************************")

def decode(message):
    shift=None
    while True:
        try:
            shift = int(input("Type the shift number from 1 to 20: "))
        except:
            print("Wrong input!")
            continue
        finally:
            if 0 < shift <= 20:
                break
            else:
                print("Wrong input!")
                continue
    decrypted = ""
    for letter in message:
        decrypted = decrypted + chr(ord(letter)-shift)
    print(f"Here is your decrypted text: {decrypted}")
    print("***************************************")

def launcher():
    print(logo)
    decision = None
    message = None
    while True:
        try:
            decision = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: "))
        except:
            print("Wrong input!")
            continue
        finally:
            if decision not in ("encode","decode"):
                print("Wrong input!")
                continue
            else:
                break
    if decision == "encode":
        message = input("Type your message: ")
        decision = encode(message)
    if decision == "decode":
        message = input("Type your encrypted message: ")
        decision = decode(message)
    while True:
        try:
            response = str(input("Type 'yes' if you want to go again. Otherwise type 'no'"))
        except:
            print("Wrong input!")
            continue
        finally:
            if response.upper() == "YES":
                launcher()
            else: break

if __name__ == "__main__":
    launcher()