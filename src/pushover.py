import httplib, urllib
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "123456789",
    "user": "123456789",
    "message": "your mailbag is full",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
