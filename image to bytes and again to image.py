import base64
############## converting an image to bytes###########################
with open("ar1.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(type(str))
    
######################################################################
################################# opening a binary file for writing data#############
f = open('output.bin', 'wb')
f.write(str)
f.close()
################################### done###########################################
#########################fetching data from binary file#########################
file = open("output.bin", "rb")

byte = file.read()

print(byte)
file.close()
########################## done################################################
###################################converting image from data ######################
fh = open("imageToSave.png", "wb")
fh.write(base64.b64decode((byte)))
fh.close()
############################done####################################
