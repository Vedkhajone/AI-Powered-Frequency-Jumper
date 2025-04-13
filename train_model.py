import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load CSV
df = pd.read_csv('data/wifi_data.csv')

# Calculate channel congestion
channel_counts = df['Channel'].value_counts().to_dict()
df['Congestion'] = df['Channel'].map(channel_counts)

# 🟡 TEMP: Add manual label (1 = Good, 0 = Bad)
# 👉 You can change this later with actual network testing
df['Label'] = df['RSSI'].apply(lambda x: 1 if x > -60 else 0)

# Features and labels
X = df[['RSSI', 'Channel', 'Congestion']]
y = df['Label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Test
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
joblib.dump(model, 'model/wifi_model.pkl')
print("✅ Model saved to wifi_model.pkl")
