import pandas as pd  # pip install pandas
import matplotlib.pyplot as plt  # matplotlib
from sklearn.model_selection import train_test_split  # scikit-learn
from sklearn.linear_model import LinearRegression

# Sample data
data = {
    'speed': [45, 50, 55, 60, 65, 75, 85, 95],
    'risk': [55, 60, 65, 70, 78, 80, 81, 82]
}

# Create a DataFrame
df = pd.DataFrame(data)
df.to_csv("drive.csv", index=False)

# Convert columns to numeric values
df['speed'] = pd.to_numeric(df['speed'])
df['risk'] = pd.to_numeric(df['risk'])


# Separate features and target variable
X = df[['speed']]
Y = df['risk']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, train_size=0.7, random_state=2)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions across the full range of speeds for a smoother line
X_range = pd.DataFrame({'speed': range(min(X['speed']), max(X['speed']) + 1)})
y_range_pred = model.predict(X_range)

# Plotting
plt.scatter(X['speed'], Y, color='red', marker='*',
            label='Data points')  # Scatter plot of data points
plt.plot(X_range['speed'], y_range_pred, color='blue',
         label='Regression line')  # Regression line

# Add labels, title, and legend
plt.xlabel('Speed of Car')
plt.ylabel('Risk on driving')
plt.title('Car driving speed risk')
plt.legend()

# Show the plot
plt.show()
