#coding=utf-8
import datetime

cg = open('/var/www/html/frame.html', 'r')
base = cg.read()
Cg.close()


def time(str1):
    disaster = datetime.datetime(2019,3,2,6,0)
    now =datetime.datetime.now()
    delt=round((disaster - now).total_seconds())
    d,hs = divmod(delt,86400)
    h,ms=divmod(hs,3600)
    m=round(ms/60)
    str1 = str1.replace('timedelta', '更新时间' +now.strftime('%Y-%m-%d-%H:%M')+'距离3月2日6:00还有{}天{}小时{}分'.format(d,h,m))
    return str1



out = open('index.html', 'w')
base = time(base)
out.write(base)
out.close()