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
print(a)

def sua(a):
    a['verson'] = '3.10'
sua(a)
print(a)

print(f'gia tri image: {a["image"]}')

a['environment'] = 'PYTHONUNBUFFERED=1'
print("Sau khi them:")
print(a)

if "volumes" in a:
    print("co key volumes")
else:
    print("khong co key do")

a.pop("depends")
print("Sau khi xoa:")
print(a)

print(f'So phan tu co trong dict:{len(a)}')

if "always" in a.values():
    print("Co values alway")
else:
    print("Khong co values")

new_key=input("Nhap key")
new_values=input("nhap values")

a[new_key]=new_values
print(a)