from client_key_generation import generate_rsa_keys, send_public_key_to_ca
from ca_certificate_generation import load_ca_private_key, generate_certificate
from client_communication import exchange_certificates

# Main function
def main():
    # Step 1: Client RSA Key Generation
    client1_public_key, _ = generate_rsa_keys()
    client2_public_key, _ = generate_rsa_keys()

    # Step 2: Sending Public Keys to CA
    send_public_key_to_ca(client1_public_key)
    send_public_key_to_ca(client2_public_key)

    # Step 3: CA Certificate Generation
    ca_private_key = load_ca_private_key()
    client1_certificate = generate_certificate(ca_private_key, client1_public_key, "Client1")
    client2_certificate = generate_certificate(ca_private_key, client2_public_key, "Client2")

    # Step 4: Client Communication
    exchange_certificates(client1_certificate, client2_certificate)
    exchange_certificates(client2_certificate, client1_certificate)

if __name__ == "__main__":
    main()
