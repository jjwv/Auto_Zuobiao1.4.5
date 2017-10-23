#coding:utf-8
#单例模式函数，用来修饰类
import sys,os
sys.path.append(os.getcwd())
def singleton(cls,*args,**kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args,**kw)
        return instances[cls]
    return _singleton