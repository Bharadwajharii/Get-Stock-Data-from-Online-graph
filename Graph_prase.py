import time 
import re
import pyautogui 
time.sleep(10) 
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
i=0
hr=9
minu=15
co1=0
co2=0
while(i<125):
    # ImageGrab-To capture the screen image in a loop.  
    # Bbox used to capture a specific area. 
    cap = ImageGrab.grab(bbox = None) 
  
    # Converted the image to monochrome for it to be easily  
    # read by the OCR and obtained the output String. 
    tesstr = pytesseract.image_to_string(cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),lang ='eng') 
    spl=tesstr.split()
    volu = [item for item in spl if item.endswith('K')]
    try:
        if(len(volu)==1):
            vol=volu[0]
            vol=vol.rstrip('K')
            vol=float(vol)
    except:
        vol=0
        co2=co2+1
    result = [item for item in spl if re.match('\d+\.\d+$', item)]
#     result = [item for item in spl if (float(item)]
    if(len(result)==5):
        if(len(volu)==1):
            enddata = enddata.append({'DATE_TIME':datetime.datetime(2020, 5,4,hr,minu),'OPEN':float(result[0]),'HIGH':float(result[1]),'LOW':float(result[2]),'CLOSE':float(result[3]),'VOLUME':vol*1000,'OPEN_INTREST':float(result[4])}, ignore_index=True)
        else:
            co2=co2+1
            enddata = enddata.append({'DATE_TIME':datetime.datetime(2020, 5,4,hr,minu),'OPEN':float(result[0]),'HIGH':float(result[1]),'LOW':float(result[2]),'CLOSE':float(result[3]),'VOLUME':0.0,'OPEN_INTREST':float(result[4])}, ignore_index=True)
    else:
        co1=co1+1
        print(result)
        if(len(volu)==1):
            enddata = enddata.append({'DATE_TIME':datetime.datetime(2020, 5,4,hr,minu),'OPEN':float(result[0]),'HIGH':float(result[1]),'LOW':float(result[2]),'CLOSE':float(result[3]),'VOLUME':vol*1000,'OPEN_INTREST':0.0}, ignore_index=True)
        else:
            co2=co2+1
            enddata = enddata.append({'DATE_TIME':datetime.datetime(2020, 5,4,hr,minu),'OPEN':float(result[0]),'HIGH':float(result[1]),'LOW':float(result[2]),'CLOSE':float(result[3]),'VOLUME':0.0,'OPEN_INTREST':0.0}, ignore_index=True)
            
#     result.append(vol[0])
#     tot=tot+tesstr
#     print(result)
#     print(spl)
    minu=minu+3
    if(minu>=60):
        minu=minu-60
        hr=hr+1
    pyautogui.moveRel(9,0) 
#     pyautogui.typewrite(["right"]) 
    i=i+1
print(co1)
print(co2)
