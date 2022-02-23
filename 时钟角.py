class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        hour_angle = 360/60
        minutes_in_hour = minutes/5
        minutes_rito = minutes/60
        hour_location = hour*5 + minutes_rito*5
        max_tmp = 0
        diff_hour_minut = 0
        angle_clock = 0
        if hour_location>minutes:
            diff_hour_minut = hour_location -minutes
        else :
            diff_hour_minut = minutes-hour_location
        angle_clock = diff_hour_minut*hour_angle
        if angle_clock > 360-angle_clock:
            return float(360-angle_clock)
        else:
            return float(angle_clock)