import os

from Lib.AES import super_aes
from Lib.archive import new_name
from config import *

DBKEY = 'db.key'


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

# get_crypt('search.db3', 'decrypt')
# e = super_aes('db.key')
# data_file = os.path.join(data_path, 'search.db3')
# output_db = new_name(data_file, 'db')  # 输出加密后的数据库
# e.decrypt(data_file, output_db)
