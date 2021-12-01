from analyse import info, histogram, histogram_multi
from humans4 import data as data4

data = {
    0: [[1, 1, -1], [1, 1, 1], [1, -1, -1], [0, 0, 0], [1, 1, 1], [-1, 1, 1], [-1, -1, 1], [-1, 1, 1], [0, 0, 0], [-1, -1, 1]],
    1: [[0, -1, -1], [0, 0, 0], [-1, 1, -1], [0, -1, 0], [-1, -1, -1], [1, -1, -1], [0, 0, 0], [-1, 1, 1], [-1, 1, -1], [1, -1, -1], [-1, 1, -1], [0, 0, 0], [0, 0, 0],
        [0, 0, 0], [0, 0, 0], [-1, -1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1], [-1, 0, 0], [-1, 1, 1], [1, -1, -1], [1, -1, -1], [-1, 0, 0], [-1, 1, 1]],
}


a = list(info(data))

print(f"          |   0   |   1   |")
print(f"Humans    | {a[0]} | {a[2]} |")
print(f"Computer  | {a[1]} | {a[3]} |")

histogram("Data 3", data)
histogram("Data 4", data4)
histogram_multi("Data Multi", data, data4)
