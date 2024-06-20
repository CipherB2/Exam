def bag(items, max_weight):
    T = [[0] * (max_weight + 1) for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for w in range(1, max_weight + 1):
            item_weight, item_value = items[i - 1]
            if item_weight <= w:
              # Берем предмет в рюкзак, если он увеличивает его стоимость
                if T[i - 1][w - item_weight] + item_value > T[i - 1][w]:
                    T[i][w] = T[i - 1][w - item_weight] + item_value
                else:
                    T[i][w] = T[i - 1][w]
            else:
                T[i][w] = T[i - 1][w]
    return T[-1][-1]
# Список предметов: (вес, стоимость)
items = [(2, 2), (4, 8), (1, 10), (7, 3), (3, 4), (8, 10), (5, 7), (10, 6), (9, 5), (6, 1)]
weight_bag = 20
max_value = bag(items, weight_bag)
print(f"Максимально возможная стоимость: {max_value}")
