from itertools import product
def solution(equation):
    left_side, right_side = equation.split('=')
    left_parts = left_side.split('+')
    def generate_numbers(pattern):
        indexes = [i for i, char in enumerate(pattern) if char == '?']
        results = []
        for replacement in product('0123456789', repeat=len(indexes)):
            num_list = list(pattern)
            for idx, repl in zip(indexes, replacement):
                num_list[idx] = repl
            if num_list[0] != '0' or len(num_list) == 1:
                results.append(int(''.join(num_list)))
        return results
    valid_count = 0
    for a in generate_numbers(left_parts[0]):
        for b in generate_numbers(left_parts[1]):
            for c in generate_numbers(right_side):
                if a + b == c:
                    valid_count += 1
    return valid_count
equation = "1?7+24?=4?5"
print(f'Количество возможных решений:  {solution(equation)}')