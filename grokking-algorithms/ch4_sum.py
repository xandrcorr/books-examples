def elem_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum(lst[1:])

if __name__ == "__main__":
    input_list = [1,4,9]
    output = elem_sum(input_list)
    print(output)