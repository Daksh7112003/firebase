import pyrebase
 

firebaseConfig = {
#     'apiKey': "AIzaSyCjlB82mH47x_7-BRkBZB2KBQWw9Ei6VhA",
#   'authDomain': "daksh-3e20b.firebaseapp.com",

# #   'databaseURL': "https://realtimedbstorage-4249a-default-rtdb.firebaseio.com",


#   'projectId': "daksh-3e20b",
#   'storageBucket': "daksh-3e20b.appspot.com",
#   'messagingSenderId': "428124117760",
#   'appId': "1:428124117760:web:d618f8c329b6fa51c5b1e5",
#   'measurementId': "G-QHSPMX7NTQ"



  'apiKey': "AIzaSyCjlB82mH47x_7-BRkBZB2KBQWw9Ei6VhA",
  'authDomain': "daksh-3e20b.firebaseapp.com",
 ' projectId': "daksh-3e20b",
  'storageBucket': "daksh-3e20b.appspot.com",
  'messagingSenderId': "428124117760",
  'appId': "1:428124117760:web:d618f8c329b6fa51c5b1e5",
'measurementId': "G-QHSPMX7NTQ"


}


firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
storage = firebase.storage()

name = input("Enter name: ")
age = input("Enter age: ")
profession = input("Enter profession: ")
filename = input("Enter the name of the file you want to upload to storage: ")
cloudfilename = input("Enter the name of the file in the cloud: ")

storage.child(cloudfilename).put(filename)
url = storage.child(cloudfilename).get_url(None)
data = {"name": name, "age": age, "profession": profession, "url": url}
db.child("users").push(data)







