def valid_passport(s):
    required = set(("ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"))
    met = set()
    fields = s.replace(" ", "\n").split("\n")
    for things in fields:
        met.add(things[:3])
    return met >= required

def read_batch(batch):
    valid = 0
    passports = batch.split("\n\n")
    for things in passports:
        if valid_passport(things):
            valid = valid + 1
    return valid

batch = ""

with open('input.txt', 'r') as reader:
    batch = reader.read()

print(read_batch(batch))
