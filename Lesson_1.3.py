n=2
m=61

def checkTime(days, minutes):
    
    days = ((days*24*60 - minutes) // 24*60)// (24*60)
    hours = (days*24 - minutes // 60) // 60

    

   

    #print('Time: ',str(timeHours).rjust(2,'0'), ':', str(timeMinutes).rjust(2,'0'))
    print (days)
    print (hours)

    
checkTime(n,m)

