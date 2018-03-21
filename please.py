import urllib.request
import json
from win10toast import ToastNotifier		#To send notifications in windows 10


'''
url = 'http://api.openweathermap.org/data/2.5/forecast?q=alwar&APPID=319f928c41e93d21af0e0227dd324adb'
response = urllib.request.urlopen(url).read()#To get data from the weather API
json_obj = str(response,'utf-8')
print(json.loads(json_obj))
'''

city=input("Enter the city : ")

#To get data from the weather API
#url = 'http://api.openweathermap.org/data/2.5/forecast?q=alwar&APPID=319f928c41e93d21af0e0227dd324adb'
url = 'http://api.openweathermap.org/data/2.5/forecast?q='+city+'&APPID=319f928c41e93d21af0e0227dd324adb'
response = urllib.request.urlopen(url).read()#To get data from the weather API
json_obj = str(response,'utf-8')
data = json.loads(json_obj)

temp= str(float("{0:.2f}".format(data['list'][0]['main']['temp'] - 273.15)))   #Conversion of temperature from kelvin to celsius
temp= "The current temperature is "+temp+" degree Celsius"

#To send notifications 
toaster= ToastNotifier()
toaster.show_toast("Temperature",temp,icon_path=None,duration=5,threaded=True)
