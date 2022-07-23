import pymongo
client = pymongo.MongoClient("mongodb+srv://srinivasaai:HAREKrsna@cluster0.dgka1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

#{} called document
data = {
      'name':'srinivas',
      'email_id':'srinivasaai@gmail.com',
      'surname':'thummedala',
      'subject': ['Data science','big data','data analytics']
}


list_of_records = [
       {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

      {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'} ]


database = client['myinfo']
collection = database['sri']
# collection.insert_one(data)
collection.insert_many(list_of_records)

collection1 = database["dpkt"]
data1 = [  {"Time": "09:15",
            "askPrice": 6722.65,
            "askQty": 750,
            "bidQty": 750,
            "bidprice": 6389.45},
            {"Time": "09:15",
            "askPrice": 6711.55,
            "askQty": 500,
            "bidQty": 500,
            "bidprice": 6215.2}]

collection1.insert_one(data1)



