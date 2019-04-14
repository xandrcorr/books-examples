import time
import random

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    base = int(len(lst)/2)
    prv, nxt = [], []
    for i in range(len(lst)):
        if i == base:
            continue
        if lst[i] <= lst[base]:
            prv.append(lst[i])
        else:
            nxt.append(lst[i])
    return quick_sort(prv) + [lst[base]] + quick_sort(nxt)

if __name__ == "__main__":
    start = time.time()
    # input_list = [10,2,4,8,5,2,6,1,6,12,0]
    input_list = random.sample(range(10000), 10000)
    output_list = quick_sort(input_list)
    print("Execution_time: {}".format(time.time()-start))
    # print(output_list)