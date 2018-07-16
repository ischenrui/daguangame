import pymysql.cursors
class Mysql(object):
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Cr648546845',
        db='daguan',
        charset='utf8'
)
# 获取游标
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)

    def InsertTrain(self, item):
        sql = "INSERT INTO train_set VALUES(%s,%s,%s,%s)"
        self.cursor.execute(sql, item)
        self.connect.commit()

    def InsertTest(self, item):
        sql = "INSERT INTO test_set VALUES(%s,%s,%s)"
        self.cursor.execute(sql, item)
        self.connect.commit()

"""
存train
"""
db = Mysql()
f = open('../input/train_set.csv','r',encoding='utf-8')
line = f.readline()
line = f.readline()
i = 0
while line:
    data = line.split(',')
    id = data[0]
    article = data[1]
    word_seg = data[2]
    cla = data[3].strip('\n')

    # print(id,article)
    db.InsertTrain((int(id),article,word_seg,cla))

    line = f.readline()
    i+=1
    print(i)

"""
存test
"""
db = Mysql()
f = open('../input/test_set.csv','r',encoding='utf-8')
line = f.readline()
line = f.readline()
i = 0
while line:
    data = line.split(',')
    id = data[0]
    article = data[1]
    word_seg = data[2]


    # print(id)
    db.InsertTest((int(id),article,word_seg))

    line = f.readline()
    i+=1
    print(i)