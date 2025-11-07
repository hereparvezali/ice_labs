import pandas as pd
import statistics as st
# Create the initial DataFrame
data = {
    'Name': ['Mitu', 'Shahadat', 'Masud', 'Sourov', 'Mahi', 'Sumaiya'],
    'Age': [23, 23, 24, 22, 22, 20],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'F'],
    'Marks': [80, 83, 'NaN', 90, 92, 'NaN']
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('my_dataset.csv', index=False)
print("Dataset saved to 'my_dataset.csv'")

# Reload the DataFrame from the CSV file
df = pd.read_csv('my_dataset.csv')
print("Dataset reloaded from 'my_dataset.csv'")
print(df)


print("\nMean:", df['Marks'].mean())
print("Median:", df['Marks'].median())
# mode() returns a Series, take the first element
print("Mode:", df['Marks'].mode()[0])
print("Standard Deviation:", df['Marks'].std())
print("Variance:", df['Marks'].var())
