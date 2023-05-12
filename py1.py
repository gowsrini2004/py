import firebase_admin as f
from firebase_admin import credentials,firestore
cred = credentials.Certificate("credentials.json")
f.initialize_app(cred)
db = firestore.client()
n = int(input("Enter No Of Entries: "))
data = []
for i in range(n):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    net_worth = int(input("Enter Net Worth: "))
    s = "var_"+str(i)
    s = {
    'Name':name,
    'Age':age,
    'Networth':net_worth        
    }
    data.append(s)
for rec in data:
    doc_ref = db.collection(u'Users').document(rec['Name'])
    doc_ref.set(rec)
print("Done")
