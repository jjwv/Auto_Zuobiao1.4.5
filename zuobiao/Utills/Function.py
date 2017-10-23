#coding:utf-8
import sys,os
sys.path.append(os.getcwd())
class Founction(object):
    # 动态获取当前方法名称
    def get_head_info():
        try:
            raise Exception
        except:
            f = sys.exc_info()[2].tb_frame.f_back
        return f.f_code.co_name

    def call_func():
        print
        '%s --> skdkjzz' % (get_head_info())

    def main():
        print
        get_head_info()

    if __name__ == '__main__':
        main()