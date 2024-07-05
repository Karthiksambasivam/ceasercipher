def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a text using Caesar Cipher.
    
    Parameters:
    text (str): The input text to encrypt or decrypt.
    shift (int): The shift value for the cipher.
    mode (str): Mode of operation - 'encrypt' or 'decrypt'. Defaults to 'encrypt'.
    
    Returns:
    str: The encrypted or decrypted text.
    """
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    
    return result

def main():
    print("Caesar Cipher Encryption/Decryption")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    text = input("Enter the text: ").strip()
    shift = int(input("Enter the shift value: ").strip())
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected!")
        return
    
    result = caesar_cipher(text, shift, mode)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
