
class ScheduleError(Exception):      #تمامی اکسپشن های ما در پروژه از این ارث بری میکنند
   """ base schedule Exeption"""
class ScheduleValueError(ScheduleError):
    """base schedule value Error"""
class IntervalError(ScheduleError):
   """use improper intervalv Error"""












class Job:
    def __init__(self,intervalv):
        self.intervalv=intervalv
        self.job_func = 'as'
        self.unit = "mojtaba"
    @property
    def second(self):
        if self.intervalv != 1:
            raise IntervalError (' use seconds instead of second')
        return self.seconds
    @property
    def seconds(self):
        self.unit = "seconds"
        return self.__str__()


test=Job(1)


