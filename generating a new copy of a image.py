import base64
with open("address of png image", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
bs=str.decode()
print(type(bs)) 
bs=bs.encode()
   
    
    
fh = open("name of new name with extesion(png)", "wb")
fh.write(base64.b64decode(bs))
fh.close()
