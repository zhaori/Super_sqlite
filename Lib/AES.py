import os


class super_aes(object):
    """
    AES加密解密类,因为调用的是系统的openssl,如果不存在可以下载它并添加到系统环境变量
    或者使用绝对、相对路径来指定具体位置
    """

    def __init__(self, key):
        self.key = key

    def encrypt(self, in_path, out_path):
        os.system(r".\Script\openssl.exe enc -aes-256-cbc -e -k {} -in {} -out {}".format(self.key, in_path, out_path)
                  )
        os.remove(in_path)

    def decrypt(self, in_path, out_path):
        os.system(r".\Script\openssl.exe enc -aes-256-cbc -d -k {} -in {} -out {}".format(self.key, in_path, out_path)
                  )
        os.remove(in_path)


def get_key(key_name, byes):
    """
    :key_name: 密钥名称
    :byes: 密钥位数
    """
    if key_name not in os.listdir('./'):
        os.system(r'.\Script\openssl.exe genrsa -out {} {}'.format(key_name, byes))
    else:
        pass
