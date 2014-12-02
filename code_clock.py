'''World_clock'''
class Clock():
	hour = input()
	minute = input()
print Clock.hour, Clock.minute
##
def country():
    ''''To compare of Thailand between time of country in the World '''
    lenmin = 2 - len(str(Clock.minute))
    #---Adilade Town in Australia (+2.30 HR. From TH)---
    aus_hour = str(abs((Clock.hour + 2)%23))
    aus_min = str(Clock.minute + 30) + ("0" * lenmain)
    aus_1 = aus_hour, aus_min

        #Fuckyouekok
    usa = "USA" + " "+ str(abs((Clock.hour - 12)%23)) + ":" + str(Clock.minute) + ("0" * (2-len(str(Clock.minute))))

    jpn = "Japan" + " "+ str(abs((Clock.hour + 2)%23)) + ":" + str(abs(Clock.minute%59)) + ("0" * (2-len(str(Clock.minute))))
    
    #return usa + "\n" + jpn
print country()
