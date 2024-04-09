# Print a dictionary in table format in Python

my_dict = {
    1: ['alice', 29],
    2: ['bobbyhadz', 30],
    3: ['carl', 31],
}

headers = ['ID', 'Name', 'Age']

print(f'{headers[0]: <10}{headers[1]: <15}{headers[2]}')

# ID        Name           Age
# 1         alice          29
# 2         bobbyhadz      30
# 3         carl           31
for key, value in my_dict.items():
    print(f'{key: <10}{value[0]: <15}{value[1]}')