def meets_policy(string):
    params = string.split(" ")
    minmax = list(map(int, params[0].split("-")))
    character = params[1][0]
    password = params[2]

    count = password.count(character)

    return count >= minmax[0] and count <= minmax[1]

def count_valid(array):
    valid = 0
    for string in array:
        if meets_policy(string):
            valid = valid + 1
    return valid

passwords = set()

with open('input.txt', 'r') as reader:
    for line in reader:
        passwords.add(line)#[:-2])

print(count_valid(passwords))
