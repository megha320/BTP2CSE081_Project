# Majority Voting Function
def majority_vote(votes):
    count0 = 0
    count1 = 0

    for v in votes:
        if v == 0:
            count0 += 1
        else:
            count1 += 1

    if count1 > count0:
        return 1
    else:
        return 0


# Predictions from 5 models
model1 = [1, 0, 1, 1, 0]  # SVM
model2 = [0, 0, 1, 0, 1]  # KNN
model3 = [1, 1, 1, 1, 0]  # Random Forest
model4 = [1, 0, 1, 0, 1]  # Logistic Regression
model5 = [0, 0, 1, 1, 1]  # Naive Bayes

# Number of samples
n = len(model1)

print("Final Majority Predictions:")

# Loop through each sample
for i in range(n):
    votes = [
        model1[i],
        model2[i],
        model3[i],
        model4[i],
        model5[i]
    ]

    result = majority_vote(votes)
    print("Sample", i+1, ":", result)
