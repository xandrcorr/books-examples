def list_len(lst):
    if lst == []:
        return 0
    return 1 + list_len(lst[1:])

if __name__ == "__main__":
    input_list = [1,2,3,4,5,6,7,11,0]
    output = list_len(input_list)
    print(output)