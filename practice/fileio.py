#file inpout output
msg1="Pay taxes with a smile"
msg2="I tried so hard but" 
msg3="Dont lie"
f=open('messages','w')
f.write(msg1)
f.write(msg2)
f.write(msg3)
f.close()

f=open('messages','r')
data=f.read()
print(data)
f.close()
