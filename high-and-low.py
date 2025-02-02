# Kata 7kyu
# Info:
## All numbers are valid Int32, no need to validate them.
## There will always be at least one number in the input string.
## Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers):
    listNumber = []
    for i in numbers.split(" "):
        listNumber.append(int(i))
    return str(max(listNumber)) + " " + str(min(listNumber))

# Casos Test
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
# return "5 1"
#high_and_low("1 2 -3 4 5")
# return "5 -3"
#high_and_low("1 9 3 4 -5")
# return "9 -5"
