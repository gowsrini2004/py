import firebase_admin as f
from firebase_admin import credentials,firestore
cred = credentials.Certificate("credentials.json")
f.initialize_app(cred)
db = firestore.client()
while(f!=0):
    y = int(input("What to do:\n1) Display\n2) Write\n3) Update\n4) Delete\n5) Stop\nEnter option: "))
    if y == 2:
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
        print("Writed\n")
    elif y == 1:
        read = db.collection(u'Users')
        docs = read.stream()
        for doc in docs:
            print(doc.to_dict())
        print("Printed\n")
    elif y == 4:
        rec = input("Enter User To Be Deleted: ")
        db.collection(u'Users').document(rec).delete()
    elif y == 3:
        rec = input("Whose data has to be updates: ")
        read = db.collection(u'Users')
        docs = read.stream()
        for doc in docs:
            if rec == doc.id:
                print("Selected User: ",doc.to_dict())
                print("Which field is to be edited: \n1) Name\n2) Age\n3) Networth\n")
                o = int(input("Enter Option(1,2,3)"))
                if o == 1:
                    name = input("Enter The New Name: ")
                    db.collection(u'Users').document(rec).update({"Name":name})
                    print("Updated Suscesfully\n")
                elif 0==2:
                    age = int(input("Enter New Age: "))
                    db.collection(u'Users').document(rec).update({"Age":age})
                    print("Updated Suscesfully\n")
                elif o==3:
                    net_worth = int(input("Enter New Net Worth"))
                    db.collection(u'Users').document(rec).update({"Networth":net_worth})
                    print("Updated Suscesfully\n")
            else:
                print("User Not Found\n")
    elif y == 5:
        f = 0
    else:
        print("Enter Proper option\n")            
