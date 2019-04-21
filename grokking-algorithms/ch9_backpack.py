

sizes = [1,2,3,4,5,6]
items = {
    "water": [3, 10],   # [size, value]
    "book": [1, 3],
    "food": [2, 9],
    "jacket": [2, 5],
    "camera": [1, 6]
}

def choose_best(items, sizes):
    table = { item: [0 for i in sizes] for item in items.keys() }
    sets = { item: [[] for i in sizes] for item in items.keys() }
    prev_item = None
    prev_params = [0 for i in sizes]
    for item, params in table.items():
        item_size = items[item][0]
        item_value = items[item][1]
        for i in sizes: # keep in mind that first elem is 1
            rest_space = i - item_size
            prev_value = prev_params[rest_space - 1] if rest_space > 0 else 0
            value = prev_value + item_value
            if rest_space >= 0 and value > prev_params[i - 1]:
                table[item][i - 1] = value
                sets[item][i - 1].append(item)
                prev_sets = sets.get(prev_item)[rest_space - 1] if prev_item is not None and rest_space > 0 else []
                sets[item][i - 1].extend(prev_sets) 
            else:
                table[item][i - 1] = prev_params[i - 1]
                prev_sets = sets.get(prev_item)[i - 1] if prev_item is not None else []
                sets[item][i - 1].extend(prev_sets) 
        prev_item = item
        prev_params = table[item]
    return sets[prev_item][len(sizes)-1], prev_params[len(sizes)-1]

if __name__ == "__main__":
    backpack, value = choose_best(items, sizes)
    print("Items in backpack: {0} | Overall value: {1}".format(backpack, value))