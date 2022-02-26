import sqlite3

# 创建数据库链接
connection = sqlite3.connect('database.db')

# 执行db.sql中的SQL语句
with open('db.sql') as f:
    connection.executescript(f.read())

# 创建一个执行句柄，用来执行后面的语句
cur = connection.cursor()

# 插入两条文章
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('我的简易版personal blog诞生啦', '这是我的personal blog，主要用python flask框架实现')
            )


# 提交前面的数据操作
connection.commit()

# 关闭链接
connection.close()
