import matplotlib.pyplot as plt

# Filter data for selected countries
selected_countries = ['US', 'Italy', 'Brazil']
selected_data = merged_data[merged_data['Country/Region'].isin(selected_countries)]

# Compute monthly number of confirmed cases and average monthly temperature
monthly_confirmed_cases = selected_data.groupby(['Country/Region', pd.Grouper(key='Date', freq='M')])['Confirmed'].max().reset_index()
monthly_temperature = selected_data.groupby(['Country/Region', pd.Grouper(key='date', freq='M')])['avg_temp_celsius'].mean().reset_index()

# Merge monthly data
monthly_data = pd.merge(monthly_confirmed_cases, monthly_temperature, on=['Country/Region', 'date'])

# Plot graph
fig, ax = plt.subplots()
for country in selected_countries:
    country_data = monthly_data[monthly_data['Country/Region'] == country]
    ax.plot(country_data['avg_temp_celsius'], country_data['Confirmed'], label=country)
ax.set_xlabel('Average monthly temperature (°C)')
ax.set_ylabel('Monthly confirmed cases')
ax.legend()
plt.show()
