a = {
    'verson':'3.8',
    'services':'app',
    'image':'python:3.10-slim',
    'command':'python app.py',
    'volumes':'./app:/app',
    'restart':'always',
    'ports':'5000:5000',
    'depends':'db'
}
# print(a)

def sua(a):
    a['verson'] = '3.10'
sua(a)
print(a)