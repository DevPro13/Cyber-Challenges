import jwt

key = ""

print(jwt.encode({"username":"admin"}, key=key, algorithm='HS256'))
