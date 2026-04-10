from collections import Counter

y_pred = [0 ,0, 1, 1, 1]

count = Counter(y_pred)
print("Class Counts:",count)

majority_class = count.most_common(1)[0][0]
print("Maximum class:", majority_class)