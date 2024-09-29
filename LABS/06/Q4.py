import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [85, 90, 75, 88],
    'attempts': [1, 2, 1, 2]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

new_index = ["A", "B", "C", "D"]

df.index = new_index

print("\nModified DataFrame:")
print(df)
