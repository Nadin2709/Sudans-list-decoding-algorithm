import decoder
import encoder
import random
import utilities
import galois

def add_noise(codeword, e, field_order= utilities.p):
    """ Function to add random noise to the codeword.
    'e' specifies how many symbols in the codeword will be flipped. """

    noisy_codeword = codeword[:]  # Copy the original codeword
    error_positions = random.sample(range(len(codeword)), e)  # Randomly select error positions
    GF257 = galois.GF(field_order)

    for pos in error_positions:
        noise = GF257(random.randint(1, field_order - 1))  # Ensure noise is in GF(257)
        noisy_codeword[pos] = noisy_codeword[pos] + noise  # Add noise (both are in GF(257))
    
    return noisy_codeword


def run(message, n, k, e, eval_pts):
    print(f"Message: {message}\nNumber of evaluation points= {n}\nNumber of errors= {e}\n")
    
    codeword = encoder.encoder(message, eval_pts)
    print(f"Encoded message: {[int(element) for element in codeword]}")
    
    corrupted_codeword = add_noise(codeword, e)
    print(f"Noisy codeword: {[int(element) for element in corrupted_codeword]}")

    possible_meessages = decoder.decoder(corrupted_codeword, n, k, e, eval_pts)
    print("List of possible decoded message")
    
    i = 1
    for possible_message in possible_meessages:
        print(f"{i}) {possible_message}")
        i += 1
    
    if message in possible_meessages: 
        print("SUCCESS: the decoded list contains the original message")
    else:
        print("FAILED: The decoded list does not contain the original message")
    print()