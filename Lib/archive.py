import os


def new_name(text, n):
    new = os.path.splitext(text)[0] + '.{}'.format(n)
    return new


def filter_suffix(text_list):
    """
    text_list: <list> text path
    过滤db ,db3后缀文件
    """
    suffix_list = []
    for file in text_list:
        if os.path.splitext(file)[1] in ['.db', '.db3']:
            suffix_list.append(file)
    return suffix_list
