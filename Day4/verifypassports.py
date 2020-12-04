import re

def valid_passport(s):
    required = set(("ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"))
    met = set()
    fields = s.replace(" ", "\n").split("\n")
    for things in fields:
        met.add(things[:3])
    return met >= required

def verify_data(s):
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    fields = s.replace(" ", "\n").split("\n")
    for things in fields:
        field = things[:3]
        data = things[4:]
        if field == "byr":
            if int(data) < 1920 or int(data) > 2002:
                return False
        if field == "iyr":
            if int(data) < 2010 or int(data) > 2020:
                return False
        if field == "eyr":
            if int(data) < 2020 or int(data) > 2030:
                return False
        if field == "hgt":
            if data[-2:] == "cm":
                if int(data[:-2]) < 150 or int(data[:-2]) > 193:
                    return False
            elif data[-2:] == "in":
                if int(data[:-2]) < 59 or int(data[:-2]) > 76:
                    return False
            else:
                return False
        if field == "hcl":
            if len(data) != 7:
                return False
            elif not int(data[1:], 16):
                return False
            elif data[0] != '#':
                return False
        if field == "ecl":
            if data not in eye_colors:
                return False
        if field == "pid":
            if len(data) != 9:
                return False
            elif not data.isdigit():
                return False
    return True

def read_batch(batch):
    valid = 0
    passports = batch.split("\n\n")
    for things in passports:
        if valid_passport(things):
            if verify_data(things):
                valid = valid + 1
    return valid

batch = ""

with open('input.txt', 'r') as reader:
    batch = reader.read()

print(read_batch(batch))
