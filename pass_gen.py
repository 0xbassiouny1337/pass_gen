import secrets
import string
import pyperclip
import time
import hashlib
from colorama import init, Fore, Style

# Password history list
password_history = []

def generate_password(length, include_special_chars):
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def evaluate_strength(password):
    length_score = min(len(password) // 4, 5)
    uppercase_score = int(any(c.isupper() for c in password))
    lowercase_score = int(any(c.islower() for c in password))
    digit_score = int(any(c.isdigit() for c in password))
    special_char_score = int(any(c in string.punctuation for c in password))

    strength_score = length_score + uppercase_score + lowercase_score + digit_score + special_char_score
    return strength_score

def ask_custom_characters():
    custom_chars = input("Enter custom characters (leave empty for default set): ")
    return custom_chars

def copy_to_clipboard(password):
    pyperclip.copy(password)
    print(Fore.GREEN + "Password copied to clipboard!" + Style.RESET_ALL)

def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    print(Fore.GREEN + "Password saved to passwords.txt" + Style.RESET_ALL)

def ask_regenerate():
    regenerate = input("Do you want to regenerate a new password? (y/n) ")
    return regenerate.lower() == 'y'


def main():
    init()  # Initialize colorama

    print(Fore.CYAN + """
      ██████╗ ██╗  ██╗██████╗  █████╗ ███████╗███████╗██╗ ██████╗ ██╗   ██╗███╗   ██╗██╗   ██╗
      ██╔═████╗╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║██╔═══██╗██║   ██║████╗  ██║╚██╗ ██╔╝
      ██║██╔██║ ╚███╔╝ ██████╔╝███████║███████╗███████╗██║██║   ██║██║   ██║██╔██╗ ██║ ╚████╔╝ 
      ████╔╝██║ ██╔██╗ ██╔══██╗██╔══██║╚════██║╚════██║██║██║   ██║██║   ██║██║╚██╗██║  ╚██╔╝  
      ╚██████╔╝██╔╝ ██╗██████╔╝██║  ██║███████║███████║██║╚██████╔╝╚██████╔╝██║ ╚████║   ██║   
      ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
    """ + Style.RESET_ALL)

    name = Fore.YELLOW + "0xbassiouny" + Style.RESET_ALL
    print(f"\nWelcome, {name}!")

    while True:
        try:
            password_length = int(input("\nEnter the length of the password: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number for the password length." + Style.RESET_ALL)
            continue
        custom_chars_input = input("Do you want to use custom characters? (y/n) ")

        if custom_chars_input.lower() == 'y':
            custom_chars = ask_custom_characters()
            if custom_chars:
                characters = custom_chars
            else:
                characters = string.ascii_letters + string.digits
            include_special_chars = False
        else:
            characters = string.ascii_letters + string.digits
            special_chars_input = input("Include special characters (y/n)? ")
            include_special_chars = special_chars_input.lower() == 'y'

        password = generate_password(password_length, include_special_chars)
        print(Fore.GREEN + "\nGenerated password:", password + Style.RESET_ALL)

        strength_score = evaluate_strength(password)
        if strength_score >= 6:
            strength_level = Fore.GREEN + "Strong" + Style.RESET_ALL
        elif strength_score >= 4:
            strength_level = Fore.YELLOW + "Medium" + Style.RESET_ALL
        else:
            strength_level = Fore.RED + "Weak" + Style.RESET_ALL
        print("Password strength:", strength_level)

        copy_input = input(Fore.YELLOW + "\nDo you want to copy the password to clipboard? (y/n) " + Style.RESET_ALL)
        if copy_input.lower() == 'y':
            copy_to_clipboard(password)

        save_input = input(Fore.YELLOW + "Do you want to save the password? (y/n) " + Style.RESET_ALL)
        if save_input.lower() == 'y':
            password_history.append(password)
            save_password(password)

        regenerate = ask_regenerate()
        if not regenerate:
            break


if _name_ == "_main_":
    main()
