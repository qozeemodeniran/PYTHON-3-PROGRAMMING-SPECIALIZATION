def tripple(value):
    return 3 * value

def trippleNum(a_list):
    new_seq = map(tripple, a_list)
    return list(new_seq)

def quadrupleNum(a_list):
    new_seq = map(lambda value: 4 * value, a_list)
    return list(new_seq)

numbers = [2, 3, 1]

triple_num = trippleNum(numbers)
print(triple_num)
print()

quadruple_num = quadrupleNum(numbers)
print(quadruple_num)
