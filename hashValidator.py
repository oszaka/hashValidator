import hashlib
import os


def calculate_md5(file_path):
    hash_md5 = hashlib.md5()

    try:
        with open(file_path, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                hash_md5.update(block)
        return hash_md5.hexdigest()
    except FileNotFoundError:
        return None


def verify_integrity(file, file_hash):
    current_hash = calculate_md5(file)

    if current_hash is None:
        return False

    if current_hash == file_hash:
        return True
    else:
        return False


def main():
    path = "/Users/ojimenez/Documents/CODE/hashValidator/testFile.txt"
    original_hash = "339ce598224fd97385a58eff8a6676d4"

    print(verify_integrity(path, original_hash))


if __name__ == "__main__":
    main()
