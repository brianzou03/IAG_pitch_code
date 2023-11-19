import numpy as np
import matplotlib.pyplot as plt

# Parameters for the Monte Carlo simulation
years = 10
days_per_year = 252
total_days = years * days_per_year
initial_investment = 10000  # Initial investment value
num_simulations = 1000  # Number of simulation runs

# Assumed annual return and volatility (standard deviation) of the S&P 500
annual_return = 0.07  # 7% average annual return
volatility = 0.15  # 15% standard deviation

# Monte Carlo simulation
np.random.seed(0)
simulation_results = np.zeros((total_days, num_simulations))

# Initial investment value for each simulation
simulation_results[0, :] = initial_investment

# Simulate the returns for each day
for t in range(1, total_days):
    random_shocks = np.random.normal(0, 1, num_simulations)
    daily_returns = (1 + annual_return / days_per_year) + (volatility / np.sqrt(days_per_year)) * random_shocks
    simulation_results[t, :] = simulation_results[t - 1, :] * daily_returns

# Calculating the percentiles for each day
percentiles = np.percentile(simulation_results, [10, 25, 50, 75, 90], axis=1)

# Converting days to years for the x-axis
years = np.arange(0, 10, 10/total_days)

# Plotting the results
plt.figure(figsize=(15, 8))

# Plotting each percentile
plt.plot(years, percentiles[0], label='10th Percentile (Conservative)')
plt.plot(years, percentiles[1], label='25th Percentile')
plt.plot(years, percentiles[2], label='50th Percentile (Average)')
plt.plot(years, percentiles[3], label='75th Percentile')
plt.plot(years, percentiles[4], label='90th Percentile (Optimistic)')

# Adding titles and labels
plt.title('Monte Carlo Simulation of S&P 500 Over 10 Years (Percentiles)')
plt.xlabel('Years')
plt.ylabel('Portfolio Value')
plt.legend()
plt.grid(True)
plt.show()
