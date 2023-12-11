import pandas as pd
import matplotlib.pyplot as plt

# Function to read and process data
def read_and_process_data(filename):
    # Read the data from the CSV file
    df = pd.read_csv(r'C:\Users\USER\Documents\WORK\ME\Shiva\NEW\World Per capita electricity consumption.csv')

    # Create two dataframes: one with years as columns and one with countries as columns
    df_years = df.pivot(index='Entity', columns='Year', values='Per capita electricity (kWh)').reset_index()
    df_countries = df.pivot(index='Year', columns='Entity', values='Per capita electricity (kWh)').reset_index()

    # Clean the transposed dataframe
    df_years.columns.name = None
    df_countries.columns.name = None

    print("Column Names:")
    print(df_years.columns)

    return df_years, df_countries

# Function to explore statistical properties
def explore_statistics(df, indicator_row_header):
    # Select a few countries for analysis
    selected_countries = ['Afghanistan', 'Albania', 'Algeria', 'Argentina', 'Australia']

    # Filter the dataframe for selected countries
    selected_data = df[df['Entity'].isin(selected_countries)]

    # Extract relevant rows for statistical analysis
    selected_data = selected_data[selected_data['Entity'].isin([indicator_row_header] + selected_countries)]

    # Transpose the data to have years as columns
    selected_data = selected_data.set_index('Entity').T

    # Summary statistics using .describe()
    describe_stats = selected_data.describe()

    # Additional statistical methods
    # Method 1: Median
    median_stats = selected_data.median()

    # Method 2: Standard Deviation
    std_stats = selected_data.std()

    # Plot the data
    selected_data.plot(kind='bar', figsize=(10, 6))
    plt.title(f'{indicator_row_header} for Selected Countries')
    plt.xlabel('Year')
    plt.ylabel(f'{indicator_row_header}')
    plt.legend(title='Country')
    plt.show()

    return describe_stats, median_stats, std_stats

# Select the indicator columns you are interested in
indicators = ['Per capita electricity (kWh)']

# Replace 'your_file_path' with the actual path to your CSV file
filename = 'C:/Users/USER/Documents/WORK/ME/Shiva/NEW/World Per capita electricity consumption.csv'
df_years, df_countries = read_and_process_data(filename)

# Call the function and display the results
describe_stats, median_stats, std_stats = explore_statistics(df_years, indicators)

# Display the results
print("Summary Statistics using .describe():")
print(describe_stats)

print("\nMedian Statistics:")
print(median_stats)

print("\nStandard Deviation Statistics:")
print(std_stats)
