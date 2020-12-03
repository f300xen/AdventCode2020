def find_pair(array, target):
    answers = set()
    for number in array:
        if number in answers:
            return [number, target - number]
        else:
            answers.add(target - number)

numbers = set()

with open('input.txt', 'r') as reader:
    for line in reader:
        numbers.add(int(line))

print(find_pair(numbers, 2020))
