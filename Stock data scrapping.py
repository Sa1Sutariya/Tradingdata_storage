from main import TvDatafeed,Interval #https://github.com/StreamAlpha/tvdatafeed
from mega import Mega # https://pypi.org/project/mega.py/
import pandas as pd
from datetime import datetime,date
mega = Mega()

today = date.today()

Filename = f'{today}.xlsx'
 
# print(datetime.today().strftime("%A"))
if 'saturday' == datetime.today().strftime("%A").lower():
	print('Today not bid')
elif 'sunday' == datetime.today().strftime("%A").lower():
	print('Today not bid')
else:			
	# mega ID Pass
	email = 'jeyav78908@vpsrec.com'
	password = "Akki@123"

	# mega login
	m = mega.login(email, password)

	# Tradingview Username and Pass
	username = 'xcmbvcxmvx'
	password = 'Akki@123'

	# initialize tradingview
	tv = TvDatafeed(username=username,password=password)
	# # tv = TvDatafeed()
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

	# To datafraeme to CSV file
	# nifty_index_data.to_csv('file1.csv')
	# print(in_1_minute)

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

	# upload file
	file = m.upload(Filename)
	m.get_upload_link(file)

	print('Done')
