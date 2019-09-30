import datetime, math

month = None

# Find out the day of the month in International Fixed Calendar
todays_date = datetime.date.today()

first_date = datetime.date(todays_date.year, 1, 1)

date_difference = todays_date - first_date

day_of_year = date_difference.days + 1

month_count = (day_of_year / 28) - (day_of_year // 28)

step_two = month_count * 28

day_of_month = math.ceil(step_two)


def month_namer(date_differential):
	global month
	month_num = date_differential // 28

	# print(month_num)

	if month_num == 0:
		month = "January"
	elif month_num == 1:
		month = "February"
	elif month_num == 2:
		month = "March"
	elif month_num == 3:
		month = "April"
	elif month_num == 4:
		month = "May"
	elif month_num == 5:
		month = "June"
	elif month_num == 6:
		month = "Sol"
	elif month_num == 7:
		month = "July"
	elif month_num == 8:
		month = "August"
	elif month_num == 9:
		month = "September"
	elif month_num == 10:
		month = "October"
	elif month_num == 11:
		month = "November"
	elif month_num == 12:
		month = "December"
	else:
		month = "Year Days"

month_namer(date_difference.days)

print("Today is " + month + " " + str(day_of_month))


# print(todays_date)
# print(first_date)
# print(date_difference)
# print(day_of_year)
# print(month_count)
# print(step_two)
# print(day_of_month)
# print(month)