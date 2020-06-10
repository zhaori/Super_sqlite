import sqlite3

from Lib.archive import new_name


class Create_db(object):

    def __init__(self, table, mode, sql, path, safety=None):
        self.table = table  # 表名
        self.mode = mode  # 插入表
        self.sql = sql  # 插入数据
        self.dbpath = path  # 数据库存储路径
        self.con = sqlite3.connect(self.dbpath, check_same_thread=False)  # 这种写法是为了处理SQLite数据库多线程

    def com_clone(self):
        # 提交事务及关闭数据库连接
        self.con.commit()
        self.con.close()

    def new_sql(self):
        """
         数据库创建、插入表
         md是model.py里的模板
        """
        try:
            self.con.execute(self.mode)
            self.com_clone()
            print('Start database successfully')
        except Exception as e:
            # 捕获SQLite数据库 table datafile already exists
            return e

    def add_sql(self, add_data):
        """
        增添数据
        这里将提交事务及关闭数据库连接的方法另写为com_clone
        如果是往数据库批量写入数据，如外部结构是for循环，能够极大提高数据存储效率
        经测试，往数据库写入2108条记录，1.0176119804382324
        """

        cn = self.con.cursor()
        cn.execute(self.sql, add_data)
        raise Exception("add_data 以字典、json格式传入")

    def delete_sql(self, element):
        # 删除表里的某一项数据table,element
        with sqlite3.connect(self.dbpath) as con:
            self.con.execute(
                "delete from " + self.table + " where " + element
            )
            print("delete a %s successfully" % element)

    def delete_table(self, table_name):
        # 删除表
        with sqlite3.connect(self.dbpath) as con:
            con.execute("drop table " + table_name)
            print('database %s delete successfully' % table_name)

    def search_table(self):
        """
         查询表
         sqlite_sequence是SQLite数据库一张隐含的表，表字段就是数据库里所有的表名称
        """
        with sqlite3.connect(self.dbpath) as con:
            sql_table = con.execute("select name from sqlite_sequence")
            return sql_table.fetchall()

    def search_key(self, tab_name):
        # 查表字段
        with sqlite3.connect(self.dbpath) as con:
            k = con.execute('select * from %s' % tab_name)
            key_name_list = [data[0] for data in k.description]
            return key_name_list

    def search_sql(self, query):
        """
         查询数据
         query 输入查询的字段，多个字段用,分开，如 'name, password, arg'

        """
        with sqlite3.connect(self.dbpath) as con:
            sql_data = con.execute(
                "select " + query + " from " + self.table
            )
            return sql_data.fetchall()

    def update_sql(self, table, value, data, id):
        # 更新数据
        with sqlite3.connect(self.dbpath) as con:
            con.execute(
                "update %s set %s = '%s' where id = %d"
                % (table, value, data, id)
            )
            # con.execute('update pwd set username = "zzg" where id = 1')
        print('update %s \'s %s successfully ' % (table, value))


def backup_data(old):
    old_data = sqlite3.connect(old)
    new_data = sqlite3.connect(new_name(old, 'mdf'))
    with new_data:
        old_data.backup(new_data)
    old_data.close()
    new_data.close()


def str_to_tuple(n):
    """
    这个函数是处理从数据库读取字段后将列表格式转化为元祖用于读取
    """
    return tuple(eval(str(n).strip('[]')))


def list_to_str(n):
    """
    适用于[('xxxxxxx',), ('xxxxx',),]
    """
    return str(n).strip('()')[:-1].strip(" '' ")


def str_remove(s):
    """
     去掉换行符
    """
    return str(s).strip('\n').replace(u'\u3000', u' ').replace(u'\xa0', u' ')


if __name__ == "__main__":
    backup_data(r'..\data\lsreport.db')
