from readers import *
from logistics import *  

instructions()

inputtedText = input("Please enter a number: ")
lan = 'en'

#String Reader
if (inputtedText == '1'): 
    stringReader()

#.txt Reader
elif (inputtedText == '2'):
    txtReader()

#.pdf Reader 
elif (inputtedText == '3'):
    pdfReader()

#.png Reader
elif(inputtedText == '4'):
    pngReader()

#.jpg Reader
elif(inputtedText == '5'):
    jpgReader()

#.pub Reader
elif(inputtedText == '6'):
    epubReader()

elif (inputtedText == 'x'):
    print ("Thank you for using Reader. Now exiting...")
    sys.exit(0)
else:
    error1()
