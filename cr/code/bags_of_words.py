# 原始语料，3个文本
strs_train =[
'God is love',
'OpenGL on the GPU is fast',
'Doctor David is PHD']
# 提取特征
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(strs_train)
shape = X_train_counts.shape
# 查看数值特征
todense = X_train_counts.todense()#转换成数值特征Bags of words
# 查看特征名
voc = count_vect.vocabulary_#特征名
print(shape)
print(todense)
print(voc)