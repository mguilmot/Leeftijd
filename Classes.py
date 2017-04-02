import calendar, time

class CalcTime(object):
    def __init__(self,birthdate):
        self.birthdate=birthdate
        self.currenttime=time.localtime()
        
    def get_birthdate(self):
        day=int(self.birthdate[0:2])
        mon=int(self.birthdate[2:4])
        yea=int(self.birthdate[4:])
        result=(day,mon,yea)
        return result
    
    def get_currenttime(self):
        day=self.currenttime[2]
        mon=self.currenttime[1]
        yea=self.currenttime[0]
        result=(day,mon,yea)
        return result
    
    def get_currenttime_orig(self):
        return self.currenttime

    def __str__(self):
        old=self.get_birthdate()
        new=self.get_currenttime()
        return str(new) + " - " + str(old)
    
    def difference(self):
        old=self.get_birthdate()
        new=self.get_currenttime()
        # Getting the years
        if new[2]-old[2]>0:
            if new[1]>old[1]:
                years=new[2]-old[2]
            else:
                years=new[2]-old[2]-1
        else:
            years=0
        
        # Getting the months
        if new[1]>old[1]:
          if new[0]>old[0]:
            months=new[1]-old[1]
          else:
            months=new[1]-old[1]-1
        elif new[1]==old[1]:
          months=0
        else:
          if new[0]>old[0]:
            months=12-old[1]+new[1]
          else:
            months=12-old[1]+new[1]-1
        
        # Getting the days
        if new[0]>old[0]:
            days=new[0]-old[0]
        else:
            curr=self.get_currenttime_orig()
            numcalprevious=calendar.monthrange(curr[0],curr[1]-1)
            numdaysprevious=numcalprevious[1]
            days=numdaysprevious-old[0]+new[0]
        
        result=(years,months,days)
        return result
    
    def printresult(self):
        result=self.difference()
        return "Leeftijd:\n\n" + str(result[0]) + " jaar, " + str(result[1]) + " maanden, " + str(result[2]) + " dagen."