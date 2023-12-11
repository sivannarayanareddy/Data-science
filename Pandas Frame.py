import pandas as pd

def read_and_process_data(filename):
    # Read the data from the CSV file
    df = pd.read_csv(r'C:/Users/USER/Documents/WORK/ME/Shiva/NEW/World Per capita electricity consumption.csv')

    # Create two dataframes: one with years as columns and one with countries as columns
    df_years = df.pivot(index='Entity', columns='Year', values='Per capita electricity (kWh)').reset_index()
    df_countries = df.pivot(index='Year', columns='Entity', values='Per capita electricity (kWh)').reset_index()

    # Clean the transposed dataframe
    df_years.columns.name = None
    df_countries.columns.name = None

    return df_years, df_countries

# Replace 'your_file_path' with the actual path to your CSV file
filename = r'C:/Users/USER/Documents/WORK/ME/Shiva/NEW/World Per capita electricity consumption.csv'
df_years, df_countries = read_and_process_data(filename)

# Display the resulting dataframes
print("Dataframe with years as columns:")
print(df_years.head())

print("\nDataframe with countries as columns:")
print(df_countries.head())
