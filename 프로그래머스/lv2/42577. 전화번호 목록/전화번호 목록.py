def has_prefix(phone_number, prefix):
    return phone_number.startswith(prefix)

def solution(phoneBook):
    phoneBook.sort()

    for i in range(len(phoneBook) - 1):
        if has_prefix(phoneBook[i + 1], phoneBook[i]):
            return False

    return True
