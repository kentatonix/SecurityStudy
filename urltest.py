import urllib.request

url = "http://kawasaki-fujimi.com/info/2017/img0731/03-02.jpg"
imagefile = "lacrosse.jpg"

urllib.request.urlretrieve(url,imagefile)

print("File Saved")
