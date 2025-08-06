from key_generation import generate_ecc_private_key
from input import get_user_input
from encryption import trinomial_encrypt
from decryption import trinomial_decrypt

def main():
    # Step 1: Get user input (plaintext)
    plaintext = get_user_input()

    K = generate_ecc_private_key()
    print(f"Private Key (K): {K}")
   

    # Step 3: Perform trinomial encryption
    a = int(input("Enter the value"))
    b = int(input("Enter the value")) 
    c = int(input("Enter the value"))
    d =int(input("Enter the value"))# Example values for coefficients
    encrypted_text = trinomial_encrypt(plaintext, a, b, c, d, K)
    print(f"Encrypted Text: {encrypted_text}")

    a = int(input("Enter the value"))
    b = int(input("Enter the value")) 
    c = int(input("Enter the value"))
    d = int(input("Enter the value"))
    decrypted_message = trinomial_decrypt(encrypted_text, a, b, c, d, K)  # Use encrypted_text for decryption
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
