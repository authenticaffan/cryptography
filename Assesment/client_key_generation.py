from Crypto.PublicKey import RSA

def send_public_key_to_ca(public_key):
    # Placeholder function to simulate sending public keys to CA
    print("Sending Public Key to CA:", public_key)

def generate_rsa_keys():
    # Generate RSA key pair
    key = RSA.generate(2048)
    # Extract public and private keys
    public_key = key.publickey().export_key()
    private_key = key.export_key()
    return public_key, private_key

# Example usage
client1_public_key, client1_private_key = generate_rsa_keys()
client2_public_key, client2_private_key = generate_rsa_keys()

print("Client 1 Public Key:", client1_public_key)
print("Client 1 Private Key:", client1_private_key)
print("Client 2 Public Key:", client2_public_key)
print("Client 2 Private Key:", client2_private_key)
