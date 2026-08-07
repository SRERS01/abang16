# 1. Implementation of the Extended Euclidean Algorithm
# Returns a tuple (gcd, x, y) such that a*x + b*y = gcd
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    # Update x and y using results of recursive call
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# 2. Function to compute the Modular Multiplicative Inverse
def modular_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        # If GCD is not 1, the inverse does not exist mathematically
        return None
    else:
        # Handle negative results to keep the value inside the modulus range
        return (x % m + m) % m

# 3. Main Operational Execution Block
if __name__ == "__main__":
    # Let's check a mock system configuration
    # Modulus used by the application (standard 32-bit ceiling)
    modulus_m = 2**32 
    
    # An observed token difference value from our system testing
    token_difference = 14352353
    
    print(f"[*] Analyzing mathematical inverse properties for delta: {token_difference}")
    
    # Calculate the inverse using our number theory function
    inverse_key = modular_inverse(token_difference, modulus_m)
    
    if inverse_key is not None:
        print(f"\n[!] INVERSE STATE IDENTIFIED!")
        print(f"    The modular inverse exists: {inverse_key}")
        print(f"    Verification Result: ({token_difference} * {inverse_key}) % {modulus_m} = {(token_difference * inverse_key) % modulus_m}")
        print("    Risk Level: High. Ensure the system utilizes a cryptographically secure RNG.")
    else:
        print("\n[+] System is secure against simple modular inverse solving.")
        print("    The targeted input difference shares a common factor with the modulus structure.")
