# #import required libraries
# import streamlit as zt
# from datetime import datetime 
# from zoneinfo import ZoneInfo

# # List of available timezones
# TIME_ZONES = [

#     "UTC",
#     "Asia/Karachi",
#     "America/New_York",
#     "Europe/London",
#     "Asia/Tokyo",
#     "Australia/Sydney",
#     "America/Los_Angeles",
#     "Europe/Berlin",
#     "Asia/Dubai",
#     "Asia/Kolkata"

# ]

# # create a title for the app
# zt.title("Time Zone App")

# # create a multiselect widget for selecting timezones
# selected_timezone = zt.multiselect("Select Timezones", TIME_ZONES, default= ["UTC", "Asia/Karachi"])


# zt.subheader("Selected Timezones")

# # using for Loop:
# for tz in selected_timezone: # tz stands for timezone

#                                             #string format time | it's a clock timing code
#     current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d | %I %H:%M:%S %p") 
#     zt.write(f"**{tz}** : {current_time} ")

# zt.subheader("Convert Time Between Timezones")

# current_time = zt.time_input("Current Time", value=datetime.now().time())

# from_tz = zt.selectbox("From Timezone", TIME_ZONES, index=0)

# to_tz = zt.selectbox("To Timezone", TIME_ZONES, index=1)

# if zt.button("Convert Time"):
#     dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
#     converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d | %I %H:%M:%S %p")

#     zt.success(f"Converted Time in {to_tz}: {converted_time}")



# Import required libraries
import streamlit as zt
from datetime import datetime, date
from zoneinfo import ZoneInfo

# List of available timezones
TIME_ZONES = [
    "UTC", 
    "Asia/Karachi", 
    "America/New_York", 
    "Europe/London",
    "Asia/Tokyo", 
    "Australia/Sydney", 
    "America/Los_Angeles",
    "Europe/Berlin", 
    "Asia/Dubai", 
    "Asia/Kolkata"
]

# Create a title for the app
zt.title("Time Zone App")

# Create a multiselect widget for selecting timezones
selected_timezone = zt.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

zt.subheader("Selected Timezones")

# Using a loop to display current times
for tz in selected_timezone:                
                                            #string format time | it's a clock timing code
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d | %I:%M:%S %p")

    zt.write(f"**{tz}** : {current_time} ")

zt.subheader("Convert Time Between Timezones")

# Select time input (current time without timezone)
current_time = zt.time_input("Current Time", value=datetime.now().time())

from_tz = zt.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = zt.selectbox("To Timezone", TIME_ZONES, index=1)

if zt.button("Convert Time"):
    
    dt = datetime.combine(date.today(), current_time).replace(tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d | %I:%M:%S %p")

    zt.success(f"Converted Time in {to_tz}: {converted_time}")
