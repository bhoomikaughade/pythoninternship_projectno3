import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
   
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase_letters))
    if use_numbers:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))
    
   
    remaining_length = length - len(password)
    password.extend(random.choice(all_characters) for _ in range(remaining_length))

   
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Random Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 4:
                print("Password length must be at least 4 characters.")
                continue

            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

            if not (use_uppercase or use_numbers or use_symbols):
                print("You must select at least one character type (uppercase, numbers, or symbols).")
                continue

            password = generate_password(length, use_uppercase, use_numbers, use_symbols)
            print(f"\nYour generated password is: {password}")

            generate_another = input("\nGenerate another password? (y/n): ").lower()
            if generate_another != 'y':
                break

        except ValueError:
            print("Invalid input. Please enter a valid number for the password length.")

    print("Thank you for using the Random Password Generator!")

if __name__ == "__main__":
    main()


main()
