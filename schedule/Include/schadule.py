import logging
import  functools

logger=logging.getLogger('schedule')




class ScheduleError(Exception):      #تمامی اکسپشن های ما در پروژه از این ارث بری میکنند
   """ base schedule Exeption"""
class ScheduleValueError(ScheduleError):
    """base schedule value Error"""
class IntervalError(ScheduleError):
   """use improper intervalv Error"""

class Scheduler: #  اجرا کننده هر جاب میباشد
    def __init__(self):
        self.jobs=[]     #اسم جابهایی را که می  آیند را در اینجا ذخیره میکنیم و با شرایط کی در کلاس پایین داره آنرا اجرا میکنیم

    def every(self, intervalv):   #ما اینترولو را میگیریم و در کلاس ها ذخیره میکنیم
        job=Job(intervalv,self)
        return job

class Job: #اطلاعات مربوط به هر جاب را ذخیره میکند
    def __init__(self,intervalv,scheduler):
        self.intervalv=intervalv    #فاصله زمانی جابها
        self.job_func = None  #اون فانکشنی که ما باید اجرا کنیم و آنرا میفرستیم
        self.unit = None     #واحدی که ما باید برای فاصله زمانی در نظر بگیریم
        self.scheduler = scheduler   #این اون کلاسی هستش که کاربر دوست دارد با آن کارهایش را اجرا کند
    @property
    def second(self):
        if self.intervalv != 1:
            raise IntervalError (' use seconds instead of second')
        return self.seconds
    @property
    def seconds(self):
        self.unit = "seconds"
        return self

    @property
    def minute(self):
        if self.intervalv != 1:
            raise IntervalError(' use minutes instead of minute')
        return self.minutes

    @property
    def minutes(self):
        self.unit = "minutes"
        return self

    # این تابع ابندا جاب فانک را گرفته به مورد خودش در بالا اضافه میکند و نهایت  آنرا به لیست جاب اضافه میکند
    #ارگ و کیبورد ارگ اون اروگومانهایی هستن که ممکن هستش نیاز باشه به جاب فانگ ارسال کنیم
    #جاب فانگ اون فانکشنی هستش که کاربر به ما میدهد
    def do(self,job_func, *args , **kwargs):
       self.job_func = functools.partial(job_func,*args, **kwargs) #پارشیال به ما اجازه میدهد که تابع جاب فانک را به همراه وردهایش در متغیر ذخیره کنیم
       functools.update_wrapper(self.job_func, job_func)  #*1
       slef._schedule_next_run()
       if self.scheduler is None :
            raise  ScheduleError (
                'unable to add job to schedule. '
                'job is not associated with an schduler'
                                                              )

       self.scheduler.jobs.append(self)
       return self
    def _schedule_next_run(self):
        pass
defult_Scheduler=Scheduler()

def every(intervalv = 1):     #ساختن همان شرکات برای متد اوری از بالا
    defult_Scheduler.every(intervalv)
"""*1)ما در تابع پارشیال میاییم و یک فانکش را به همراه اروگومان های در یک متغییر ذخیره میکنیم.
این یک خوبی برای ما دارد  که 
میتوانیم همه را در یک متغییر داشته باشیم اما نقطه ضعف ان انیست 
که همه داندرهای موجود برای جاب فانک برای این متغییر  جدید ما 
فعال نیست برای برطرف کردن این عیب ما باید بتوانیم از آپدیت رپر استفاده کنیم تا این عیب هم برطرف شود"""