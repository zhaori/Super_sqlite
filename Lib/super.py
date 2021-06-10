import hashlib
import json
import os
import time

Data_Json = {
    "Admin": {
        "admin": {
            "Authority": '1',
            "password": '02bd175f329720378ce83dd56a1b6b1f5291a60182d6c54b5e0d1e8d248a267a',
        }
    },
    "User": {

    },
    "Guest": {

    }
}


def _get_log(err_name, error_data):
    err_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    with open(os.path.join('./Log', err_name), 'a', encoding="utf-8") as f:
        data = err_time + "   " + str(error_data)
        f.write(str(data) + "\n")


def get_sha256(s):
    return hashlib.sha256(str(s).encode('utf-8')).hexdigest()


def new_json(path):
    with open(os.path.join(path, "group.json"), 'w', encoding='utf-8') as f:
        f.write(json.dumps(Data_Json, indent=4, ensure_ascii=False))


class json_sqlite(object):
    def __init__(self, json_file):
        """
        :return 对group.json文件进行增删改
        """
        self.json_file = json_file
        try:
            with open(self.json_file, 'r', encoding="utf-8") as f:
                self.data_json = dict(json.loads(f.read()))
        except FileNotFoundError:
            error_data = str(self.__init__.__name__) + "      %s  文件不存在" % json_file
            _get_log('error.log', error_data)
            print(error_data)

    def write_json(self):
        with open(self.json_file, 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.data_json, indent=4, ensure_ascii=False))

    def upgrade_name(self, root, tag, new_tag):
        """
        root: 预更改的组
        tag：预更改的用户
        new_tag: 更改的值
        """
        value = self.data_json[root].get(tag)
        del self.data_json[root][tag]
        self.data_json[root][new_tag] = value
        return self.data_json

    def upgrade_value(self, root, tag, value):
        """
        root: 预更改的组
        tag：预更改的用户
        value：预更改的值
        """
        self.data_json[root][tag]['Authority'] = value
        return self.data_json

    def upgrade_pwd(self, root, tag, pwd):
        """
        root：预更改的组
        tag：预更改的用户
        pwd：预更改的密码
        """
        self.data_json[root][tag]['password'] = get_sha256(pwd)
        return self.data_json

    def add_user(self, root, username, password):
        admin_list = [u for u in self.data_json['Admin'].keys()]
        user_list = [u for u in self.data_json['User'].keys()]
        guest_list = [u for u in self.data_json['Guest'].keys()]
        if username not in admin_list and \
                username not in user_list and \
                username not in guest_list:
            # print(user_list)
            self.data_json[root][username] = {"Authority": 1,
                                              "password": get_sha256(password),
                                              }
            print("用户：%s 添加成功" % username)

        elif username in admin_list or username in user_list or username in guest_list:
            print('拒绝添加，%s 已存在' % username)
        # print(self.data_json['User'])

    def del_user(self, root, username):
        """
        删除用户
        """
        try:
            del self.data_json[root][username]
            print('%s 已删除' % username)
        except KeyError:
            error_data = str(self.del_user.__name__) + "      %s  用户不存在" % username
            _get_log('error.log', error_data)

    def verify(self, user, pwd):
        """
        验证用户和密码
        """
        user_data_li = ['Admin', 'User', 'Guest']
        for d in user_data_li:
            user_list = [u for u in self.data_json[d].keys()]
            try:
                if self.data_json[d][user]['password'] == get_sha256(pwd):
                    # print("登陆成功")
                    return True

                elif self.data_json[d][user]['password'] != get_sha256(pwd):
                    # print("密码错误")
                    return False

                elif user not in user_list:
                    # print("用户不存在")
                    return False

            except KeyError as e:
                error_data = str(self.verify.__name__) + "       %s     不存在或者错误" % e
                _get_log('error.log', error_data)
                print(e, '不存在')

    def return_data(self, root, son, grandson):
        """
         分别返回父、子、孙节点的值
        """
        return [self.data_json[root],
                self.data_json[root][son],
                self.data_json[root][son][grandson]]

    def return_Authority(self, root, user):
        root_list = [r for r in root]
        user_list = [self.data_json[u] for u in root_list]
        for a in user_list:
            print(a[user]['Authority'])
        # print(user_list)


if __name__ == "__main__":
    d = json_sqlite('../group.json')
    user_data_li = ['Admin', 'User', 'Guest']
    d.return_Authority(user_data_li, 'admin')

    # with openSqlite('123456') as f:
    # Q f.crypt(r'./search.db')
    # f.crypt('./search.db', './search.db.bak')
    #    f.decrypt('./search.db.bak', './search.db')
    # new_json()
    # a = d.verify(' ', '123456')
    # print(a)
    # print(d.return_data('User', 'zzg', 'Authority')[2])
    # d.add_user('User', '皮得狠1', '000000', './search.db')
    # d.upgrade_name('User', 'zgz', 'zzg')
    # d.write_json()
    # gc.collect()
    # d.del_user('User', 'zgz')
    # print(type(time.strftime('%Y.%m.%d.%X', time.localtime(time.time()))))
    # with OpenSqlite('666666') as f:
    #    f.crypt(r'../Log/error.log', r'../error.log')
    # if __name__ == "__main__":
    #    with OpenSqlite('666666') as f:
    #        f.decrypt(r'../error.log', r'../Log/error.log')
