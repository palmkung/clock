'''World_clock'''
class Clock():
	hour = input()
	minute = input()
print Clock.hour, Clock.minute

def country():
    usa = "USA" + " "+ str(abs((Clock.hour - 12)%24)) + ":" + str(abs(Clock.minute%59))
    jpn = "Japan" + " "+ str(abs((Clock.hour + 2)%24)) + ":" + str(abs(Clock.minute%59))
    return usa + "\n" + jpn
print country()
