from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import os

# Elliptic curve parameters for secp256k1
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

def generate_ecc_private_key():
    """Generate a secure ECC private key using a hash value."""
    # Generate a random value
    random_bytes = os.urandom(32)
    
    # Hash the random value using SHA-256
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(random_bytes)
    hashed_bytes = digest.finalize()
    
    # Convert the hash to an integer
    private_key_int = int.from_bytes(hashed_bytes, byteorder='big') % n
    
    return private_key_int

# Test the key generation
if __name__ == "__main__":
    K = generate_ecc_private_key()
    print(f"Private Key (K): {K}")
