numbers = ([1, 1, 2, 4, 4])
def get_unique_elements(numbers):
    get_unique_elements = []

    unique_elements = set(numbers)

    for numbers in unique_elements:
        get_unique_elements.append(numbers)
    return get_unique_elements
print(get_unique_elements(numbers))


def transform_to_string(s):
    str = ""
    for str1 in s:
        str1 += str
    return str1
s = [1, True, 'Hello']
print(transform_to_string(s))
