import os
# download era5 data climate data

os.chdir("../src/")
import era5
os.chdir("../examples/")


# ERA5
# enter coordinates
latitude = 9.830153
longitude = -83.616358

# set start and end date (end date will be included
# in the time period for which data is downloaded)
start_date, end_date = '2017-12-31', '2018-12-31'  # time in UTC choose start date one day before time of interest
# for position east of 0° meridian for covering all hours of interest

# set variable set to download

variable = "pvlib"
target_file = 'ERA5_pvlib_2018.nc'

ds = era5.get_era5_data_from_datespan_and_position(
    variable=variable,
    start_date=start_date, end_date=end_date,
    latitude=latitude, longitude=longitude,
    target_file=target_file)


# plot irradiance
# import matplotlib.pyplot as plt
# weather_df.loc[:, ['BHI', 'DHI']].plot(title='Irradiance')
# plt.xlabel('Time')
# plt.ylabel('Irradiance in $W/m^2$')

# Alternative: Load existing existing climate data file
# import pandas as pd
# solar_hegelbach = pd.read_csv(r"apv_hegelbach_raw.csv")