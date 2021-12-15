n=10
m=1430

def checkTime(days, minutes):
    
    minutesInTotal=(days-(days*24*60-minutes)//(60*24))*60*24-minutes

    timeHours = minutesInTotal//60

    timeMinutes=minutesInTotal-timeHours*60

    print('Time: ',str(timeHours).rjust(2,'0'), ':', str(timeMinutes).rjust(2,'0'))
    
checkTime(n,m)

