import numpy as np
import matplotlib.pyplot as plt

# Initial parameters
initial_price = 17.85  # Current lithium price
mean_change = 0.04  # Mean of the normal distribution
std_dev = 0.25  # Standard deviation
years = 10  # Forecasting period in years
num_simulations = 10000  # Number of Monte Carlo simulations

# Parameters for boom years
boom_mean_change = 0.6  # Mean increase during a boom year
boom_std_dev = 0.4  # Standard deviation during a boom year
boom_chance = 0.15  # Chance of a boom year (15%)

# Parameters for tank years
tank_mean_change = -0.08  # Mean decrease during a tank year (-8%)
tank_std_dev = 0.25  # Standard deviation during a tank year (25%)
tank_chance = 0.15  # Chance of a tank year (15%)

# Function to simulate the price path with boom and tank year consideration and a maximum of two for each
def simulate_price_path_with_boom_and_tank():
    prices = [initial_price]
    consecutive_decreases = 0
    boom_years_count = 0
    tank_years_count = 0

    for _ in range(years):
        # Decide if it's a boom year, a tank year, or a normal year
        is_boom_year = np.random.rand() < boom_chance if boom_years_count < 2 else False
        is_tank_year = np.random.rand() < tank_chance if tank_years_count < 2 else False

        if is_boom_year:
            boom_years_count += 1
        if is_tank_year:
            tank_years_count += 1

        # Adjust mean if there were two consecutive decreases (for normal years)
        adjusted_mean = mean_change if consecutive_decreases < 2 else mean_change + 0.05
        if is_boom_year:
            mean, std_deviation = boom_mean_change, boom_std_dev
        elif is_tank_year:
            mean, std_deviation = tank_mean_change, tank_std_dev
        else:
            mean, std_deviation = adjusted_mean, std_dev

        change = np.random.normal(mean, std_deviation)
        new_price = prices[-1] * (1 + change)

        if change < 0:
            consecutive_decreases += 1
        else:
            consecutive_decreases = 0

        prices.append(new_price)

    return prices

# Running the simulations
simulated_paths_with_boom_and_tank = np.array([simulate_price_path_with_boom_and_tank() for _ in range(num_simulations)])

# Calculating forecasts
average_prices_with_boom_and_tank = simulated_paths_with_boom_and_tank.mean(axis=0)
conservative_forecast_with_boom_and_tank = np.percentile(simulated_paths_with_boom_and_tank, 10, axis=0)
percentile_25th_with_boom_and_tank = np.percentile(simulated_paths_with_boom_and_tank, 25, axis=0)
percentile_75th_with_boom_and_tank = np.percentile(simulated_paths_with_boom_and_tank, 75, axis=0)
optimistic_forecast_with_boom_and_tank = np.percentile(simulated_paths_with_boom_and_tank, 90, axis=0)

# Plotting the results
plt.figure(figsize=(12, 7))
for path in simulated_paths_with_boom_and_tank[:100]:
    plt.plot(path, color='lightgrey', alpha=0.5)

plt.plot(average_prices_with_boom_and_tank, color='red', label='Average Price (50th Percentile)')
plt.plot(conservative_forecast_with_boom_and_tank, color='blue', linestyle='--', label='Conservative Forecast (10th Percentile)')
plt.plot(percentile_25th_with_boom_and_tank, color='purple', linestyle='--', label='25th Percentile')
plt.plot(percentile_75th_with_boom_and_tank, color='orange', linestyle='--', label='75th Percentile')
plt.plot(optimistic_forecast_with_boom_and_tank, color='green', linestyle='--', label='Optimistic Forecast (90th Percentile)')

plt.title('Monte Carlo Simulation of Lithium Prices Over 10 Years (Boom & Tank Assumption)')
plt.xlabel('Years')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()
