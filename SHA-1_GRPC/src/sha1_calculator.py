import hashlib


def calculate_and_compare_sha1(filename, sha1_value):
    with open(sha1_value, 'r') as file:
        data = file.read().replace('\n', '')
        correct_sha1_val = data  # correct

    BUF_SIZE = 65536
    sha1 = hashlib.sha1()

    with open(filename, 'rb') as file:
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)

        calculated_sha1 = sha1.hexdigest()
        print(calculated_sha1)
    print(correct_sha1_val)

    if correct_sha1_val == calculated_sha1:
        return 1, correct_sha1_val, calculated_sha1
    return 0, correct_sha1_val, calculated_sha1
