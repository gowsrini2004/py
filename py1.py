import firebase_admin as f
from firebase_admin import credentials,firestore
cred = credentials.Certificate("credentials.json")
f.initialize_app(cred)
db = firestore.client()
y = input("What to do:(r/w)")
if y == 'w':
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
        write = db.collection(u'Users').document(rec['Name'])
        write.set(rec)
    print("Done")
elif y == "r":
    read = db.collection(u'Users')
    docs = read.stream()
    for doc in docs:
        print(doc.to_dict())
elif y == "d":
    rec = input("Enter Name: ")
    db.collection(u'Users').document(rec).delete()
elif y == "u":
    val = []
    rec = input("Whose data has to be updates: ")
    read = db.collection(u'Users')
    docs = read.stream()
    docs = read.stream()
    for doc in docs:
        dict = doc.to_dict()
        val.append(dict.values())
    print(val)

