
import pyshortenes

url = input("enter url")
short = pyshortenes.shortener().tinyurl.short(url)

print(short)