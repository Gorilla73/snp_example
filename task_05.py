import datetime

def date_in_future(integer):

    if type(integer) != int:
        return datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    res_date = datetime.datetime.now() + datetime.timedelta(days=2)
    return res_date.strftime('%d-%m-%Y %H:%M:%S')

print(date_in_future([])) # => текущая дата
print(date_in_future(2)) # => текущая дата + 2 дня
