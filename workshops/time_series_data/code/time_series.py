#Time Series Dataset from the Black Lagoon 

import pandas as pd 
import random 
import numpy as np 
import datetime 
import matplotlib.pyplot as plt


#Timeseries reference: https://pandas.pydata.org/docs/user_guide/timeseries.html 
#Timestamp reference: https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html 
#Date range: https://pandas.pydata.org/docs/reference/api/pandas.date_range.html 

#read_in_data 

sensor_1_df = pd.read_csv("sensor_1.csv")
sensor_1_df["timestamp"] = pd.to_datetime(sensor_1_df["timestamp"])
sensor_1_df['timestamp'] = sensor_1_df['timestamp'].dt.tz_localize('utc')
sensor_1_df.drop(columns=["Unnamed: 0"], inplace=True)
#print(sensor_1_df.head())

sensor_2_df = pd.read_csv("sensor_2.csv")
sensor_2_df.drop(columns=["Unnamed: 0"], inplace=True)
#print(sensor_2_df.head())

sensor_3_df = pd.read_csv("sensor_3.csv")
sensor_3_df.drop(columns=["Unnamed: 0"], inplace=True)
#print(sensor_3_df.head())

sensor_4_df = pd.read_csv("sensor_4.csv")
sensor_4_df["timestamp"] = pd.to_datetime(sensor_4_df["timestamp"])
sensor_4_df['timestamp'] = sensor_4_df['timestamp'].dt.tz_localize('utc')

sensor_4_df.drop(columns=["Unnamed: 0"], inplace=True)
#print(sensor_4_df.head())



#Step 1 - Associate a time stamp with the data that has no
#time stamp. Generally want the timestamps to all be in the 
#same format 

#Sensor 2 
start_sensor_2 = pd.Timestamp(2022, 1, 1, 1, 0, 0)
idx = pd.date_range(start_sensor_2, periods=len(sensor_2_df.index), freq="5min")
s2_readings = sensor_2_df.iloc[:, 0].values.tolist()
df_dict = {"timestamp": idx, "reading": s2_readings}
s2_df = pd.DataFrame(df_dict)
s2_df['timestamp'] = s2_df['timestamp'].dt.tz_localize('utc')


#Sensor 3 
end_sensor_3 = pd.Timestamp(2022, 12, 31, 23, 8, 0)
idx = pd.date_range(end=end_sensor_3, periods=len(sensor_3_df.index), freq="5min")
s3_readings = sensor_3_df.iloc[:, 0].values.tolist()
df_dict = {"timestamp": idx, "reading": s3_readings}
s3_df = pd.DataFrame(df_dict)


#Step 3 - make sure timezones are aligned
#Convert s3 from PRC to UTC 
s3_df["timestamp"] = s3_df["timestamp"].dt.tz_localize("PRC")
s3_df["timestamp"] = s3_df["timestamp"].dt.tz_convert("UTC")
#print(s3_df.head())


#Step 4 - check for any missing data 
#Do these one at a time 
# plt.scatter(sensor_1_df["timestamp"], sensor_1_df["reading"], color="g")
# plt.scatter(s2_df["timestamp"], s2_df["reading"], color="b")
# plt.scatter(s3_df["timestamp"], s3_df["reading"], color="r")
# plt.scatter(sensor_4_df["timestamp"], sensor_4_df["reading"], color="y")
# plt.show()
# plt.clf()

#We can see there is a big gap in sensor 4's readings. 
#We have data Jan - March and the Sept - Dec, but not a lot else 

#Step 5 - decide our time range and clip it 
#Lets decide to use Jan-March data 
start_date = pd.Timestamp(2022, 1, 1, 0, 0, 0).tz_localize(tz="UTC")
end_date = pd.Timestamp(2022, 3, 31, 23, 0, 0).tz_localize("UTC")


#Step 6 - decide our sampling interval 
#Decide hourly 
#Min, max, mean for sensors
s2_min = s2_df.resample("h", on="timestamp", origin=start_date).min()
s2_min.reset_index(inplace=True, drop=True)
s2_max = s2_df.resample("h", on="timestamp", origin=start_date).max()
s2_max.reset_index(inplace=True, drop=True)
s2_mean = s2_df.resample("h", on="timestamp", origin=start_date).mean()
s2_mean.reset_index(inplace=True)

s3_min = s3_df.resample("h", on="timestamp", origin=start_date).min()
s3_min.reset_index(inplace=True, drop=True)
s3_max = s3_df.resample("h", on="timestamp", origin=start_date).max()
s3_max.reset_index(inplace=True, drop=True)
s3_mean = s3_df.resample("h", on="timestamp", origin=start_date).mean()
s3_mean.reset_index(inplace=True)

s4_min = sensor_4_df.resample("h", on="timestamp", origin=start_date).min()
s4_min.reset_index(inplace=True, drop=True)
s4_max = sensor_4_df.resample("h", on="timestamp", origin=start_date).max()
s4_max.reset_index(inplace=True, drop=True)

s4_mean = sensor_4_df.resample("h", on="timestamp", origin=start_date).mean()
s4_mean.reset_index(inplace=True)


#NEW DF 
new_df = s4_mean.copy()
new_df = new_df.rename(columns={"reading": "s4_mean"})


merge_options = [s2_min, s2_max, s2_mean, s3_min, s3_max, s3_mean, s4_min, s4_max]
merge_names = ["s2_min", "s2_max", "s2_mean", "s3_min", "s3_max", "s3_mean", "s4_min", "s4_max"]

#for i in range(0, len(merge_options)):
for i in [2,5]:
    sub_df: object = merge_options[i]
    #Added
    sub_df.fillna(method="bfill", inplace=True)
    sub_df.fillna(method="ffill",inplace=True)
    sub_df.dropna(inplace=True)
    new_df = pd.merge_asof(new_df, sub_df, direction="nearest")
    #new_df = pd.merge(new_df, sub_df,  how="left", direction="nearest")
    new_df = new_df.rename(columns={"reading": f"{merge_names[i]}"})

#print(new_df.head())
new_df = pd.merge(new_df, sensor_1_df,  how="left")
new_df = new_df.rename(columns={"reading": f"s1_setpoint"})
print(new_df.head())
new_df.fillna(method="bfill", inplace=True)
new_df.fillna(method="ffill",inplace=True)
new_df.dropna(inplace=True)

#Filter 
new_df = new_df.loc[(new_df["timestamp"] >= start_date) & (new_df["timestamp"] <= end_date)]
print(new_df.iloc[-1])
print(new_df.head())
print(new_df.columns)
#new_df.to_csv("time_series_data_formatted.csv")