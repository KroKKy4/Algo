# 99865278

def decoder(compressed: str) -> str:
    if len(compressed) == 0:
        return ''

    stack = []
    current_num: int = 0
    current_instr: str = ''

    for char in compressed:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char.isalpha():
            current_instr += char
        elif char == '[':
            stack.append((current_num, current_instr))
            current_num, current_instr = 0, ''
        elif char == ']':
            num, last_instr = stack.pop()
            current_instr = last_instr + current_instr * num

    return current_instr


def read_data():
    input_code: str = input()
    return input_code


def main():
    compressed = read_data()
    print(decoder(compressed))


if __name__ == '__main__':
    main()
