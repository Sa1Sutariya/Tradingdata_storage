from main import TvDatafeed, Interval, News_data_Gether  # https://github.com/StreamAlpha/tvdatafeed
from mega import Mega  # https://pypi.org/project/mega.py/
import pandas as pd
from datetime import datetime, date
import os
import sys

# Initialize Mega module
mega = Mega()
print('Initilize')

# Get today's date
today = date.today()

# Create filename using today's date
Filename = f'{today}.xlsx'

# Get current path
current_path = sys.path[0]

# Check if today is Saturday or Sunday
if 'saturday' == datetime.today().strftime("%A").lower():
    print('Today not bid')
elif 'sunday' == datetime.today().strftime("%A").lower():
    print('Today not bid')
else:
	pass
	# Mega login email and password
email = '' # Write Your Mega Login Email
password = '' # Write Your Mega Login Password

# Login to Mega
m = mega.login(email, password)
print('Login Mega')

# Tradingview username and password
username = '' # Write Your Tradingview Login Username
password = '' # Write Your Tradingview Login Password

# Initialize TvDatafeed with given username and password
tv = TvDatafeed(username=username, password=password)
print('Tradingview Data scrap')

# Scrape data from Tradingview for various intervals
in_1_minute = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_1_minute,n_bars=100000)
in_3_minute = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_3_minute,n_bars=100000)
in_5_minute = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_5_minute,n_bars=100000)
in_15_minute = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_15_minute,n_bars=100000)
in_30_minute = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_30_minute,n_bars=100000)
in_45_minute = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_45_minute,n_bars=100000)
in_1_hour = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_1_hour,n_bars=100000)
in_2_hour = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_2_hour,n_bars=100000)
in_3_hour = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_3_hour,n_bars=100000)
in_4_hour = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_4_hour,n_bars=100000)
in_daily = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_daily,n_bars=100000)
in_weekly = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_weekly,n_bars=100000)
in_monthly = tv.get_hist(symbol='BANKNIFTY',exchange='NSE',interval=Interval.in_monthly,n_bars=100000)

# Print message to indicate that data collection is done
print('Data Collection Done')

# Call Main function to collect news data
News_data = News_data_Gether()

# Print message to indicate that news data collection is done
print('News Data Collection Done')
# To datafraeme to CSV file
# nifty_index_data.to_csv('file1.csv')
# print(in_1_minute)

# Write data to Excel file
with pd.ExcelWriter(Filename) as writer:

	# use to_excel function and specify the sheet_name and index
	# to store the dataframe in specified sheet
	in_1_minute.to_excel(writer, sheet_name="in_1_minute")
	in_3_minute.to_excel(writer, sheet_name="in_3_minute")
	in_5_minute.to_excel(writer, sheet_name="in_5_minute")
	in_15_minute.to_excel(writer, sheet_name="in_15_minute")
	in_30_minute.to_excel(writer, sheet_name="in_30_minute")
	in_45_minute.to_excel(writer, sheet_name="in_45_minute")
	in_1_hour.to_excel(writer, sheet_name="in_1_hour")
	in_2_hour.to_excel(writer, sheet_name="in_2_hour")
	in_3_hour.to_excel(writer, sheet_name="in_3_hour")
	in_4_hour.to_excel(writer, sheet_name="in_4_hour")
	in_daily.to_excel(writer, sheet_name="in_daily")
	in_weekly.to_excel(writer, sheet_name="in_weekly")
	in_monthly.to_excel(writer, sheet_name="in_monthly")
	News_data.to_excel(writer, sheet_name="News", index=False)

	# Print message to indicate that data collection is done
	print('Gathering all data in excel')

# upload file
file = m.upload(Filename)
m.get_upload_link(file)
print('Upload Done')

# Remove file
Remove_File = os.path.join(current_path,Filename)
os.remove(Remove_File)
print('Remove Done')

print('Done')
