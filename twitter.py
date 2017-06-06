# rpi twitter machine

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

'''message = "Hello #picademy! This from a Raspberrypi!"
twitter.update_status(status=message)
print("Tweeted: %s" % message)
'''

message = "Pic test post #picademy - here's a picture!"
with open('/home/pi/Downloads/picademy.jpg', 'rb') as photo:
    twitter.update_status_with_media(status=message, media=photo)
