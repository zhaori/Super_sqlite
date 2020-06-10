import os

from Lib.debug_error import ZIP_ERROR


def seven_zip(file, source):
    try:
        os.system(r'.\Script\7z.exe a {} {}'.format(file, source))
    except ZIP_ERROR as e:
        return e
