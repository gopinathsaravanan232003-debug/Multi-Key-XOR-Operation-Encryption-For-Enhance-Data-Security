import os

# Assume the ECC private key is K
def xnor(a, K):
    """Perform XNOR operation between a and k."""
    return ~(a ^ K) & 0xFF  # 0xFF is used to limit the result to 8 bits (similar to a byte)

def trinomial_encrypt(plaintext, a, b, c, d, K):
    """Encrypt plaintext using the modified trinomial equation and XNOR-modified coefficients."""
    encrypted = []
    for char in plaintext:
        x = ord(char)  # Convert character to ASCII
 
        # Modify coefficients using the ECC private key (k) with XNOR
        a_inv = xnor(a, K)
        b_inv = xnor(b, K)
        c_inv = xnor(c, K)
       
        # Apply the trinomial equation with the modified coefficients
        trinomial_value = (a_inv * (x ** 3) + b_inv * (x ** 2) + c_inv * x + d) 

        # Add the encrypted value to the list
        encrypted.append(trinomial_value)

    return encrypted



    
       
