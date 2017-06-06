from picamera import PiCamera
from time import sleep

fixedtemp = 0
humidity_val = 0


# rpi twitter part
from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#sense hat parts  #################
from sense_hat import SenseHat

def getValues():
    global fixedtemp
    global humidity_val
    hat = SenseHat()

    temp = hat.temp
    fixedtemp = round(temp, 2)  # this rounds the values

    humidity = hat.humidity
    humidity_val = round((64 * humidity / 100),2) # this rounds the value

#####################

def takePicAndPost():
    global fixedtemp
    global humidity_val
    
    camera = PiCamera()

    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/tweetPics/image.jpg')
    camera.stop_preview()


    message = ('Nice here at #picademy! It is ' +  str(fixedtemp) + "C" + " and " + str(humidity_val) + "% humidity. #sensehat data")
    with open('/home/pi/Desktop/tweetPics/image.jpg', 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)

#####################


# gets the temp and humidity values from the sensehat
getValues()
    
# takes a picture and posts it to twitter @picademyenviro
takePicAndPost()

    

  

