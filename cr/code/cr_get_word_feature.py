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

    def Sel_Train_Class(self, cla):
        sql = "SELECT word_seg FROM `train_set` WHERE cla = %s;"
        self.cursor.execute(sql, cla)
        data = self.cursor.fetchall()
        return data

def get_word_rate():
    db = Mysql()

    for i in range(1,20):
        cla = str(i)
        data = db.Sel_Train_Class(cla)
        f = open('../analysis/word_rate_%s.txt'%(cla),'w',encoding='utf-8')
        word_rate_dir = {}
        for node in data:
            word_seg = node['word_seg']
            wordlist = word_seg.split(' ')
            for word in wordlist:
                if word in word_rate_dir.keys():
                    word_rate_dir[word] += 1
                else:word_rate_dir[word] = 1
        f.write(str(word_rate_dir))

if __name__ == '__main__':
    get_word_rate()
