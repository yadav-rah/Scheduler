import datetime

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
'October', 'November', 'December']

#Supercript List
endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']

days_in_mon = [31,28,31,30,31,30,31,31,30,31,30,31]

code = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

#GETTING PRESENT DATE,MONTH && YEAR
c_year = datetime.date.today().strftime("%Y")
c_month = datetime.date.today().strftime("%m")
c_date = datetime.date.today().strftime("%d")
dd = int(c_date)
mm = int(c_month)
yy = int(c_year)
ordinal = c_date + endings[dd-1]

print("Today's Date : " + months[mm-1] + " " + ordinal + ", "+ c_year + " " + datetime.date.today().strftime("%A"))

#INPUTS FROM THE USER NO OF DAYS & MONTHS IN FUTURE
nod_f = int(input("Enter Number Of Future Days : "))
f_mon = int(input("Enter Number Of Future Months : "))

#INPUTS FROM THE USER NO OF DAYS & MONTHS IN PAST
nod_p = int(input("Enter Number Of Past Days : "))
p_mon = int(input("Enter Number Of Past Months : "))

#DATE VARIABLES FOR PAST AND FUTURE
p_d = dd
p_m = mm
p_y = yy
f_d = dd
f_m = mm
f_y = yy

#CALCULATING PAST DATE
y2s = 0
if p_mon > 12:
    y2s = p_mon//12
    m2s = p_mon%12
    while m2s > 0:
        if p_m > 0:
            p_m -= 1
            m2s -= 1
        if p_m < 1:
            p_m = 12
            y2s += 1

p_y -= y2s

count = 0
while count < nod_p:
    p_d -= 1
    if p_d < 1:
        p_m -= 1
        p_d = days_in_mon[p_m-1]
    if p_m < 1:
        p_m = 12
        p_y -= 1
        if ((p_y % 4 == 0 & p_y % 100 != 0) | p_y % 400 == 0):
            days_in_mon[1] = 29
        else:
            days_in_mon[1] = 28
    count += 1

d = p_d
m = p_m
dod = (p_y + p_y/4 - p_y/100 + p_y/400 + code[p_m-1] + p_d) % 7;
dod=round(dod)
if dod == 0 or dod ==7:
    day = 'Sunday'
elif dod == 1:
    day = 'Monday'
elif dod == 2:
    day = 'Tuesday'
elif dod == 3:
    day = 'Wednesday'
elif dod == 4:
    day = 'Thursday'
elif dod == 5:
    day = 'Friday'
elif dod == 6:
    day = 'Saturday'

month_name = months[p_m-1]
ordinal = str(p_d) + endings[p_d-1]
print ('The Past Date is :' + month_name + ' ' + ordinal + ', ' + str(p_y) + ' ' + day)

#CALCULATING FUTURE DATE
if f_mon <= 12:
    f_m += f_mon
    y2a = 0
elif f_mon > 12:
    y2a = f_mon//12
    m2a = f_mon%12
    f_m += m2a

if f_m > 12:
    y2a += 1
    f_m -= 12
f_y += y2a

count = 0
while count < nod_f:
    f_d += 1
    if f_d > days_in_mon[f_m-1]:
        f_d = 1
        f_m += 1
    if f_m > 12:
        f_m = 1
        f_y += 1
        if ((f_y % 4 == 0 & f_y % 100 != 0) | f_y % 400 == 0):
            days_in_mon[1] = 29
        else:
            days_in_mon[1] = 28
    count += 1

#GETTING THE DAY ON THAT DATE USING "Sakamoto's methods"
d = f_d
m = f_m
dod = (f_y + f_y/4 - f_y/100 + f_y/400 + code[f_m-1] + f_d) % 7;
dod=round(dod)
if dod == 0 or dod==7:
    day = 'Sunday'
elif dod == 1:
    day = 'Monday'
elif dod == 2:
    day = 'Tuesday'
elif dod == 3:
    day = 'Wednesday'
elif dod == 4:
    day = 'Thursday'
elif dod == 5:
    day = 'Friday'
elif dod == 6:
    day = 'Saturday'

month_name = months[f_m-1]
ordinal = str(f_d) + endings[f_d-1]
print ('The Future Date is :' + month_name + ' ' + ordinal + ', ' + str(f_y) + ' ' + day)
