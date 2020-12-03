def find_pair(array, target):
    answers = set()
    for number in array:
        if number in answers:
            return [number, target - number]
        else:
            answers.add(target - number)

def find_triplet(array, target):
    for number in array:
        pair = find_pair(array - {number}, target - number)
        if pair:
            return pair + [number]

numbers = set()

with open('input.txt', 'r') as reader:
    for line in reader:
        numbers.add(int(line))

print(find_triplet(numbers, 2020))
