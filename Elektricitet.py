import datetime 

date_now = datetime.datetime(2025,9,1)
date_then = datetime.datetime(2025,10,1)

date_diff = (date_now - date_then).days

start_year = input("Enter the starting year: ")
start_month = input("Enter the starting month: ")
start_day = input("Enter the starting day: ")

end_year = input("Enter the ending year: ")
end_month = input("Enter the ending month: ")
end_day = input("Enter the ending day: ")

start_year = int(start_year)
start_month = int(start_month)
start_day = int(start_day)

end_year = int(end_year)
end_month = int(end_month)
end_day = int(end_day)

start_date = datetime.datetime(start_year, start_month, start_day)
end_date = datetime.datetime(end_year, end_month, end_day)

date_diff = (end_date - start_date).days

meter_start = input("Enter the meters starting number")
meter_end = input("Enter the meters ending number")
day_price = input("Enter the daily fee")
kwh_price = input("Enter the starting price")

meter_start = int(meter_start)
meter_end = int(meter_end)
day_price = int(day_price)
kwh_price = int(kwh_price)

meter_diff = meter_end - meter_start

total_price = (date_diff * day_price + meter_diff * kwh_price) * 1.25
print(total_price)