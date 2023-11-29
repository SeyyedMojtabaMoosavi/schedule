import logging
import  functools
import datetime

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
    def run_pending(self):
        runnable_jobs = (job for job in self.jobs if job.should_run)
        for job in sorted(runnable_jobs):
            sel._run_job(job)

    def _run_job(self, job):
       pass
class Job: #اطلاعات مربوط به هر جاب را ذخیره میکند
    def __init__(self,intervalv,scheduler):
        self.intervalv=intervalv    #فاصله زمانی جابها
        self.job_func = None     #اون فانکشنی که ما باید اجرا کنیم و آنرا میفرستیم
        self.unit = None       #واحدی که ما باید برای فاصله زمانی در نظر بگیریم
        self.period =None      #فاصله بین هر جاب را مشخص میکند
        self.next_run = None   #زمان اجرای هر جاب را مشخص میکند
        self.scheduler = scheduler    #این اون کلاسی هستش که کاربر دوست دارد با آن کارهایش را اجرا کند
    def __lt__(self, other):
        return self.next_run < other.next_run
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
    @property
    def hour(self):
        if self.intervalv != 1:
            raise IntervalError('use hours instead of hour')
        return self.hours
    @property
    def hours(self):
        slef.unit = "hours"
        return self
    @property
    def day(self):
        if self.intervalv != 1:
            raise IntervalError('use days instead of day')
        return slef.days

    @property
    def days(self):
        self.unit = "days"
        return self

    @property
    def week(self):
        if self.intervalv != 1:
            raise IntervalError('use weeks instead of week')
        return slef.weeks

    @property
    def weeks(self):
        self.unit = "weeks"
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
    @property
    def should_run(self):
        assert self.next_run is not None , "must run schedule_next_run"
        return datetime.datetime.now() >= self.next_run



    def _schedule_next_run(self):  #مشخص میکند که هر جاب من در چه بازه زمانی باید تکرار شود
        if self.unit not in ('seconds','minutes','hours','days','weeks') :
            raise ScheduleValueError ('Invalid unit'
                                      ' (valid units are `seconds`,`minuts`,`hours`,`days`,`weeks`'
                                      )

        intervalv = self.intervalv
        self.period = datetime.timedelta(**{self.unit : intervalv})  #با گذاشتن دو ستاره و آکولاد موجب میشویم که محتوای یونیت باز شود و ارسال شود به تایم دلتا
        self.next_run=datetime.datetime.now() + self.period
defult_Scheduler=Scheduler()

def every(intervalv = 1):     #ساختن همان شرکات برای متد اوری از بالا
    defult_Scheduler.every(intervalv)

def run_pending(self):
    defult_Scheduler.run_pending()
"""*1)ما در تابع پارشیال میاییم و یک فانکش را به همراه اروگومان های در یک متغییر ذخیره میکنیم.
این یک خوبی برای ما دارد  که 
میتوانیم همه را در یک متغییر داشته باشیم اما نقطه ضعف ان انیست 
که همه داندرهای موجود برای جاب فانک برای این متغییر  جدید ما 
فعال نیست برای برطرف کردن این عیب ما باید بتوانیم از آپدیت رپر استفاده کنیم تا این عیب هم برطرف شود"""