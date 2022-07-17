import pymongo
client = pymongo.MongoClient("mongodb+srv://srinivasaai:HAREKrsna@cluster0.dgka1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

d = {
    'name':'srinivas',
    'email_id':'srinivasaai@gmail.com',
    'surname':'thummedala'
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)