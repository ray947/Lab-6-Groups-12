#aahan shin

def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = (int(digit) + 3) % 10 
        encoded_password += str(new_digit)
    return encoded_password

# carson salameh

def decode(password):
    output = ""
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        output += str(new_digit)
    return output



def main():
    encoded_password = ""  
    while True:
        print("\nMenu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():  
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("error")
        
        # carson salameh
        elif option == "2":
            if len(encoded_password) == 8 and password.isdigit():
                output = decode(encoded_password)
                print("Your decoded password is:",output)
            else:
                print("error")
        
        
        elif option == "3":
            break  

        else:
            print("error")

if __name__ == "__main__":
    main()
