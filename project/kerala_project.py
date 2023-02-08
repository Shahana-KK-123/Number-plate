import cv2
import pytesseract
import numpy as np

cascade=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

kerala={"KL01":"THIRUVANANTHAPURAM","KL02":"KOLLAM","KL03":"PATHANAMTHITTA","KL04":"ALAPPUZHA","KL05":"KOTTAYAM","KL06":"IDUKKI","KL07":"ERNAKULAM","KL08":"THRISSUR","KL09":"PALAKKAD","KL10":"MALAPPURAM","KL11":"KOZHIKODE","KL12":"WAYANAD","KL13":"KANNUR","KL14":"KASARAGOD","KL15":"NATIONAL SECTOR","KL16":"ATTINGAL","KL17":"MUVATTUPUZHA","KL18":"VADAKARA","KL19":"PARASSALA","KL20":"NEYYATTINKARA","KL21":"NEDUMANGAD","KL22":"KAZHAKUTTOM","KL23":"KARUNAGAPPALLY","KL24":"KOTTARAKKARA","KL25":"PUNALUR","KL26":"ADOOR",
"KL27":"THIRUVALLA","KL28":"MALLAPPALLY","KL29":"KAYAMKULAM","KL30":"CHENGANNUR","KL31":"MAVELIKKARA","KL32":"CHERTHALA","KL33":"CHANGANACHERRY","KL34":"KANJIRAPPALLY","KL35":"PALA","KL36":"VAIKKOM","KL37":"VANDIPERIYAR","KL38":"THODUPUZHA","KL39":"TRIPUNITHURA","KL40":"PERUMBAVOOR","KL41":"ALUVA","KL42":"NORTH PARAVOOR","KL43":"MATTANCHERRY","KL44":"KOTHAMANGALAM","KL45":"IRANJALAKKUDA","KL46":"GURUVAYOOR","KL47":"KODUNGALLUR","KL48":"VADAKKANCHERRY","KL49":"ALATHUR","KL50":"MANNARKKAD","KL51":"OTTAPPALAM",
"KL52":"PATTAMBI","KL53":"PERINTHALMANNA","KL54":"PONNANI","KL55":"TIRUR","KL56":"KOYILANDY","KL57":"KODUVALLY","KL58":"THALASSERY","KL59":"THALIPARAMBA","KL60":"KANHANGAD","KL61":"KUNNATHUR","KL62":"RANNI","KL63":"ANGAMALI","KL64":"CHALAKKUDY","KL65":"THIRURANGADI","KL66":"KUTTANADU","KL67":"UZHAVOOR","KL68":"DEVIKULAM","KL69":"UDUMBANCHOLA","KL70":"CHITTUR","KL71":"NILAMBUR","KL72":"MANANTHAVADY","KL73":"SULTHANBATHERY","KL74":"KATTAKKADA","KL75":"THRIPRAYAR","KL76":"NANMANDA","KL77":"PERAMBRA","KL78":"IRITTY",
"KL79":"VELLARIKUNDU","KL80":"PATHANAPURAM","KL81":"VARKALA","KL82":"CHADAYAMANGALAM","KL83":"KONNI","KL84":"KONDOTTY","KL85":"RAMANATTUKARA (FEROKE)","KL86":"PAYYANNUR"}


img=cv2.imread("kerala/car_kerala_img/KL10.jpg")


img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

no_plate=cascade.detectMultiScale(img_grey,1.1,4)
print(len(no_plate))
for(x,y,w,h) in no_plate:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    crop=img_grey[y:y+h,x:x+w]
    #cv2.imshow('plate',crop)
    text=pytesseract.image_to_string(crop)
print(text)
text=''.join(i for i in text if i.isalnum())
dist_code=text[0:4]
print(dist_code)
for i in kerala:
    if (i==dist_code):
        print('Car Belongs to',kerala[i])
        place=kerala[i]
        
             

rect_img=cv2.rectangle(img,pt1=(50,55),pt2=(600,55),color=(255,255,255),thickness=150)
text1=cv2.putText(img,text="The Car number is :",org=(20,50),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(255,255,0),thickness=2)

text1=cv2.putText(img,text=text,org=(385,50),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(255,255,0),thickness=2)
text1=cv2.putText(img,text="The Car belongs to:",org=(20,80),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(255,255,0),thickness=2)
text1=cv2.putText(img,text=place,org=(385,80),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(255,255,0),thickness=2)
cv2.imshow('result',text1)
cv2.waitKey() 
cv2.destroyAllWindows()


    