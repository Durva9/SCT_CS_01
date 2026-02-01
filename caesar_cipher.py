def caesar_encrypt(text, shift):
    """Encrypt text using Caesar Cipher"""
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Shift the character and wrap around using modulo
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result


def caesar_decrypt(text, shift):
    """Decrypt text using Caesar Cipher"""
    # Decryption is just encryption with negative shift
    return caesar_encrypt(text, -shift)


def main():
    print("=" * 50)
    print("CAESAR CIPHER - ENCRYPTION & DECRYPTION")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == '1':
            message = input("\nEnter the message to encrypt: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if shift < 1 or shift > 25:
                    print("Please enter a shift value between 1 and 25.")
                    continue
                encrypted = caesar_encrypt(message, shift)
                print(f"\n✓ Encrypted message: {encrypted}")
            except ValueError:
                print("Invalid input! Please enter a number for shift value.")
        
        elif choice == '2':
            message = input("\nEnter the message to decrypt: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if shift < 1 or shift > 25:
                    print("Please enter a shift value between 1 and 25.")
                    continue
                decrypted = caesar_decrypt(message, shift)
                print(f"\n✓ Decrypted message: {decrypted}")
            except ValueError:
                print("Invalid input! Please enter a number for shift value.")
        
        elif choice == '3':
            print("\nThank you for using Caesar Cipher!")
            break
        
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()