import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Data
data = {
    'Quarter': ['2022 Q4', '2023 Q2'],
    'Net Sales': [235.5, 235.8],  # In millions
    'Adjusted EBITDA': [-2.6, 42.9]  # In millions
}
df = pd.DataFrame(data)

# Representing quarters as numerical values for modeling
df['Quarter_Num'] = range(1, len(df) + 1)

# Linear regression models
model_sales_lr = LinearRegression()
model_ebitda_lr = LinearRegression()

# Fitting models
model_sales_lr.fit(df[['Quarter_Num']], df['Net Sales'])
model_ebitda_lr.fit(df[['Quarter_Num']], df['Adjusted EBITDA'])

# Predicting future values for the next 10 quarters
future_quarters_extended = np.array([[3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
forecast_sales_lr_extended = model_sales_lr.predict(future_quarters_extended)
forecast_ebitda_lr_extended = model_ebitda_lr.predict(future_quarters_extended)

# Data for plot
forecast_df_lr_extended = pd.DataFrame({
    'Quarter_Num': range(3, 13),
    'Forecasted Net Sales': forecast_sales_lr_extended,
    'Forecasted Adjusted EBITDA': forecast_ebitda_lr_extended
})

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(forecast_df_lr_extended['Quarter_Num'], forecast_df_lr_extended['Forecasted Net Sales'], label='Forecasted Net Sales', marker='o')
plt.plot(forecast_df_lr_extended['Quarter_Num'], forecast_df_lr_extended['Forecasted Adjusted EBITDA'], label='Forecasted Adjusted EBITDA', marker='x')
plt.title('Forecasted Net Sales and Adjusted EBITDA for Next 10 Quarters')
plt.xlabel('Quarter Number (Starting from 2022 Q4 as 1)')
plt.ylabel('Amount in Millions')
plt.legend()
plt.grid(True)
plt.show()
