from os import path

# 数据库表名
db_table = 'datafile'

# 数据库存储位置及名称
data_path = r'./data'
db_name = 'search.db'
db_path = path.join(data_path, db_name)

# 数据库备份路径
db_backup = r'./backup'
db_mode = """
        create table """ + db_table + """ (
            [id] integer PRIMARY KEY AUTOINCREMENT,
            file_path text,
            file_name text,
            c_time text,
            x_time text,
            file_size text,
            file_hash text
        )
"""

# 插入数据
db_data = """
        insert into """ + db_table + """ 
            ( file_path, file_name, c_time, x_time, file_size, file_hash ) 
            values 
            (:file_path, :file_name, :c_time, :x_time, :file_size, :file_hash )        
"""

DBKEY = 'db.key'
GROUP_JSON = r'./group.json'
