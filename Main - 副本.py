import os
from Lib.AES import super_aes, get_key
from Lib.debug_error import *
from Lib.FromLib import reduce_open, reduce_close
from Lib.archive import new_name
from Lib.sqlite import Create_db
from Lib.super import json_sqlite, new_json

HELP = """
    open              打开数据库
    config            打开配置文件
    new               创建新配置文件（如果已经存在配置文件会覆盖）
"""

# reduce_close()


try:
    from config import *
except ModuleNotFoundError:
    reduce_open()
    from config import *

DB_LOGIN = False

config_file = os.path.exists(GROUP_JSON)
crypt = super_aes(DBKEY)
group = json_sqlite(GROUP_JSON)


def Login(name, pwd, path=GROUP_JSON):
    # 验证登录
    d = json_sqlite(path)
    if d.verify(name, pwd) is True:
        return True
    else:
        return False


def get_crypt(data, mode):
    """

    :param path: 数据库目录
    :param data: 数据库名称
    :param mode: 模式，加密或解密 encrypt or decrypt
    :return: 密钥默认在根目录下
    """
    crypt = super_aes(DBKEY)
    data_file = os.path.join(data_path, data)
    if mode == 'encrypt':
        output_db = new_name(data_file, 'db3')  # 输出加密后的数据库
        crypt.encrypt(data_file, output_db)

    elif mode == 'decrypt':
        crypt.decrypt(data_file, new_name(data_file, 'db'))


while 1:

    CMD = input('>>>>>')
    if CMD == 'help':
        print(HELP)

    elif CMD == 'new':
        if config_file is False:
            new_json(r'./')
        else:
            pass
        if os.path.exists('db.key') is False:
            get_key(DBKEY, 256)
        db = input('输入数据库名称：')
        get_crypt(db, 'encrypt')

    elif CMD == 'open':
        db = input('输入数据库名称：')
        if db in os.listdir(data_path):
            name = input('输入用户名：')
            pwd = input('输入用户密码：')
            sql_file = os.path.join(db_path, CMD[5:])

            if Login(name, pwd) is True:
                DB_LOGIN = True
                print('%s 登录成功' % db)
            else:
                DB_LOGIN = False
                raise USER_PASSWORD_ERROR
        else:
            DB_LOGIN = False
            print('%s  数据库不存在' % db)

    elif CMD == 'add':
        if DB_LOGIN is True:
            db = input('输入数据库文件名：')
            get_crypt(db, 'decrypt')
            group.add_user('User', '赵子淦', '666666')

    elif CMD == 'config':
        os.system(r'.\Script\Notepad3.exe config.py')

    elif CMD == 'login':
        print(DB_LOGIN)
