import time
import random

def selection_sort(lst):
    new_list = []
    # min_val = l[min_idx]
    for i in range(len(lst)):
        min_idx = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[min_idx]:
                min_idx = i
        new_list.append(lst.pop(min_idx))
    return new_list


if __name__ == "__main__":
    # input_list = [10,2,4,8,5,2,6,1,6,12,0]
    input_list = random.sample(range(10000), 10000)
    start = time.time()
    output_list = selection_sort(input_list)
    print("Execution_time: {}".format(time.time()-start))
    # print(output_list)
