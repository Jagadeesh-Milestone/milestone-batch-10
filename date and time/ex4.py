#time delta:

from datetime import datetime,timedelta

today=datetime.now()
print('today datetime is:',str(today))

date_after_3_years=today+timedelta(days=1095)
date_after_3_days=today+timedelta(days=3)
print('date after three years:',str(date_after_3_years))
print('date after three days:',str(date_after_3_days))