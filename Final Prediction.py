from collections import Counter

y_pred = [1, 0, 1, 1, 1]

count = Counter(y_pred)
print("Class Counts:",count)

majority_class = count.most_common(1)[0][0]
print("Maximum class:", majority_class)

from sklearn.metrics import accuracy_score

y_true = [1, 0, 0, 1, 1]   
y_pred = [1, 0, 1, 1, 1]   

accuracy = accuracy_score(y_true, y_pred)
print("Accuracy:", accuracy)