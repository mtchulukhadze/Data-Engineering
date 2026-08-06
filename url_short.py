import pyshorteners

url = input("enter url")
short = pyshorteners.Shortener().tinyurl.short(url)

print(short)
