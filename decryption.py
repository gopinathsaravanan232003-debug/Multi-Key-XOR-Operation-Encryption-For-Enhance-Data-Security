def xnor(a, K):
    """Perform XNOR operation between a and k."""
    return ~(a ^ K) & 0xFF  # Ensure the result is within 8 bits

def trinomial_decrypt(encrypted_text, a, b, c, d, K):
    """Decrypt ciphertext using the reverse trinomial equation and XNOR-modified coefficients."""
    decrypted = []  # List to store decrypted characters
    
    # Modify coefficients using the ECC private key (k) with XNOR (same as in encryption)
    a_inv = xnor(a, K)
    b_inv = xnor(b, K)
    c_inv = xnor(c, K)
    

    # Iterate over each encrypted character
    for encrypted_char in encrypted_text:
        # Try every possible character (ASCII 0-255) to find the match
        for x in range(256):  # Loop through all possible ASCII values
            trinomial_value = (a_inv * (x ** 3) + b_inv * (x ** 2) + c_inv * x + d) 
            if trinomial_value == encrypted_char:
                decrypted.append(chr(x))  # Convert the matching value back to a character
                break

    return ''.join(decrypted)  # Join the decrypted characters into a single string


