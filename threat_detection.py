import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# AI-Based Cyber Threat Detection
# Dataset: UNSW-NB15


# Load datasets
train_data = pd.read_csv("UNSW_NB15_training-set.csv")
test_data = pd.read_csv("UNSW_NB15_testing-set.csv")

# Select basic features
X_train = train_data[['dur', 'sbytes', 'dbytes']]
y_train = train_data['label']

X_test = test_data[['dur', 'sbytes', 'dbytes']]
y_test = test_data['label']

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict threats
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)

# Test sample traffic
sample = [[1.5, 250, 100]]
result = model.predict(sample)

if result[0] == 1:
    print("⚠️ Cyber Attack Detected")
else:
    print("✅ Normal Traffic")