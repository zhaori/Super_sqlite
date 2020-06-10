import os
import sys
import time


# dir_path = os.path.dirname(os.path.abspath(__file__))

def _control(_path, filename):
    # st_atime(访问时间), st_mtime(修改时间), st_ctime（创建时间)
    suffer = os.path.join(_path, filename)
    c_time = os.stat(suffer).st_ctime
    m_time = os.stat(suffer).st_mtime
    file_size = os.stat(suffer).st_size
    ctime = time.strftime('%Y.%m.%d.%X', time.localtime(c_time))
    mtime = time.strftime('%Y.%m.%d.%X', time.localtime(m_time))
    return mtime, ctime


try:
    if sys.argv[1] == '-l':
        for p in os.listdir(sys.argv[2]):
            mt, ct = _control(sys.argv[2], p)
            print('文件名：{}       修改日期：{}     创建日期：{}'.format(p, mt, ct))
except IndexError:
    for i in os.listdir('./'):
        print(i)
