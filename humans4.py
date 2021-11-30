from analyse import info

data = {
    0: [[1, -1, -1], [-1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [-1, -1, 1], [1, -1, 1], [1, -1, -1], [-1, 1, -1]],
    1: [[-1, -1, 1], [-1, 1, 1], [-1, 1, -1]],
    2: [[]],
    3: [[]],
}

a = list(info(data))

print(f"          |   0   |   1   |   2   |   3   |")
print(f"Humans    | {str(a[0])[:5]} | {str(a[2])[:5]} | {str(a[4])[:5]} | {str(a[6])[:5]} |")
print(f"Computer  | {str(a[1])[:5]} | {str(a[3])[:5]} | {str(a[5])[:5]} | {str(a[7])[:5]} |")
