class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date.split("-")[0])
        month = int(date.split("-")[1])
        day = int(date.split("-")[2])
        month_day_not_run =[31,28,31,30,31,30,31,31,30,31,30,31]
        month_day_run =[31,29,31,30,31,30,31,31,30,31,30,31]
        month_day=[]
        calc_days = 0
        if ( year % 4==0 and year%100!=0) or year%400==0 :
            month_day=month_day_run
        else:
            month_day=month_day_not_run
        for i in range(int(month)-1):
            calc_days = calc_days + month_day[i]
        calc_days = calc_days + day
        return calc_days
        
