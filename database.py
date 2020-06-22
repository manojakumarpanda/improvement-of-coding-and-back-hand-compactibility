import dbconnector as s

s.cur.execute("insert in to student values(10,'debasish maharana','electronics and telecommucication','gopalpur')")
print('The data is inserted successfully::')
s.cn.commit()
print('the data is inserted successfully::')

