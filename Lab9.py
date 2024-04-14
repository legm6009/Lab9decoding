
def encoder(password):
    new_password = ""
    for char in password:
        char = int(char) + 3
        char = str(char)[-1]
        new_password += char
    return new_password

def decoder(password):
    temp_string = ""
    for char in password:
        char = int(char)-3
        if char < 0:
            char = char+10
        char = str(char)
        temp_string += char
    return temp_string

if __name__ == "__main__":
    password = None
    while True:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit
Please enter an option: """, end="")
        option = int(input())
        if option == 1:
            password = input("Please enter your password to encode: ")
            password = encoder(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {password}, and the original password is {decoder(password)}.")
        elif option == 3:
            break
