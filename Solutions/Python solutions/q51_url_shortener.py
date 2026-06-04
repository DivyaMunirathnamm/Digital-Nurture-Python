import hashlib

class URLShortener:

    def __init__(self):
        self.urls = {}

    def shorten(self, url):
        short = hashlib.md5(url.encode()).hexdigest()[:6]
        self.urls[short] = url
        return short

    def retrieve(self, short):
        return self.urls.get(short)

shortener = URLShortener()

short = shortener.shorten("https://google.com")

print("Short URL:", short)
print("Original URL:", shortener.retrieve(short))