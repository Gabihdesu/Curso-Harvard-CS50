def swap_case(s):
    sw = ''
    for c in s:
        if c.islower():
            sw += c.upper()
        elif c.isupper():
            sw += c.lower()
    return sw

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)