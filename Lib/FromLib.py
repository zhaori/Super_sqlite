import gzip
import os


class import_config(object):

    def __init__(self, file, gzip_file):
        self.file = file
        self.gzip = gzip_file

    def reduce(self):
        if os.path.exists(self.file) is True:
            g = gzip.GzipFile('', "wb", fileobj=open(self.gzip, 'wb'))
            g.write(open(self.file, 'rb').read())
            g.close()
        else:
            print('%s 不存在' % self.file)

    def unreduce(self):
        if os.path.exists(self.gzip) is True:
            g = gzip.GzipFile(mode="rb", fileobj=open(self.gzip, 'rb'))
            open(self.file, "wb").write(g.read())
            g.close()
        else:
            print('%s 不存在' % self.file)


def reduce_open():
    f = 'config.py'
    gz_file = './config.py.gz'
    g = import_config(f, gz_file)
    g.unreduce()
    os.remove(gz_file)


def reduce_close():
    f = 'config.py'
    gz_file = './config.py.gz'
    g = import_config(f, gz_file)
    g.reduce()
    os.remove(f)
