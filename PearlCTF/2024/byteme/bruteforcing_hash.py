import hashlib
import itertools
import multiprocessing

# Target MD5 hash
target_hash = "9ce86143889d80b01586f8a819d20f0c"

# Known prefix
prefix = "pearl{"

# Brute-force characters
brute = "abcdefghijklmnopqrstuvwxyz0123456789_"

def hash_password(password):
    """Hash a password and check if it matches the target hash."""
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    if hashed_password == target_hash:
        print("Password found:", password)
        return password
    return None

def brute_force(characters):
    """Brute-force passwords with the given characters."""
    for combination in itertools.product(characters, repeat=6):
        password = prefix + ''.join(combination)
        if hash_password(password):
            return password

if __name__ == "__main__":
    print("Start bruteforcing...")
    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    # Perform brute-force concurrently
    result = pool.map(brute_force, [brute] * multiprocessing.cpu_count())

    # Close the pool to release resources
    pool.close()
    pool.join()

    # Check if any process found the password
    for res in result:
        if res:
            break
