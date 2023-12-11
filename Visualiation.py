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

    return df_years

# Function to create combined plots
def create_combined_plots(df_years, selected_countries):
    # Plot 1: Per Capita Electricity Consumption Over Time
    plt.figure(figsize=(18, 12))

    plt.subplot(2, 2, 1)
    for country in selected_countries:
        plt.plot(df_years.columns[1:], df_years[df_years['Entity'] == country].values.flatten()[1:], label=country)
    plt.title('Per Capita Electricity Consumption Over Time')
    plt.xlabel('Year')
    plt.ylabel('Per Capita Electricity Consumption (kWh)')
    plt.legend(title='Country')

    # Plot 2: Comparison of Countries
    plt.subplot(2, 2, 2)
    latest_year = df_years.columns[-1]
    latest_data = df_years[['Entity', latest_year]].set_index('Entity')
    latest_data.plot(kind='bar', legend=False)
    plt.title(f'Per Capita Electricity Consumption in {latest_year}')
    plt.xlabel('Country')
    plt.ylabel('Per Capita Electricity Consumption (kWh)')

    # Plot 3: Population Growth and Energy Consumption
    plt.subplot(2, 2, 3)
    world_population_data = df_years[df_years['Entity'] == 'World Population']
    if not world_population_data.empty:
        plt.plot(world_population_data.columns[1:], world_population_data.values.flatten()[1:], label='World Population', color='black')
        plt.title('Population Growth Over Time')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.legend(title='Population', loc='upper left')

    plt.tight_layout()
    plt.show()

# Replace 'your_file_path/World Per capita electricity consumption.csv' with the actual path to your CSV file
filename = r'C:\Users\USER\Documents\WORK\ME\Shiva\NEW\World Per capita electricity consumption.csv'
df_years = read_and_process_data(filename)

# Select the countries you are interested in for plotting
selected_countries = ['Afghanistan', 'Albania', 'Algeria', 'Argentina', 'Australia']

# Call the function to create combined plots
create_combined_plots(df_years, selected_countries)
