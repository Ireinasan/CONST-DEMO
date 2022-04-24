import requests
 
url = "http://0.0.0.0:5000"
 
filepath='./test/newbus.jpg'
split_path = filepath.split('/')
filename = split_path[-1]
print(filename)
 
file = open(filepath, 'rb')
files = {'file':(filename, file, 'image/jpg')}
 
r = requests.post(url,files = files)
result = r.text
print (result)