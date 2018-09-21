# HttpClient.py is written by [xqin]: https://github.com/xqin/SmartQQ-for-Raspberry-Pi
from http import cookiejar
from urllib import request,parse
from urllib.error import URLError,HTTPError

class HttpClient:
    __cookie = cookiejar.CookieJar()
    __handler = request.HTTPCookieProcessor(__cookie)
    print("Http:.......")
    __opener = request.build_opener(__handler)
    
    __opener.addheaders = [
        ('Accept', 'application/javascript, */*;q=0.8'),
        ('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)')
    ]
    request.install_opener(__opener)

    def Get(self, url, refer=None):
        try:
            req = request.Request(url)
            if not (refer is None):
                req.add_header('Referer', refer)

            return request.urlopen(req).read().decode("utf-8")
        except HTTPError as  e:
            return e.read()

    def Post(self, url, data, refer=None):
        try:
            req = request.Request(url, parse.urlencode(data).encode('utf-8'))
            if not (refer is None):
                req.add_header('Referer', refer)
            return request.urlopen(req).read().decode("utf-8")
        except HTTPError as e:
            print("httpError:>>",e)
            return e.read()

    def Download(self, url, file):
        output = open(file, 'wb')
        output.write(request.urlopen(url).read())
        output.close()

#  def urlencode(self, data):
#    return urllib.quote(data)

    def getCookie(self, key):
        for c in self.__cookie:
            if c.name == key:
                return c.value
        return ''

    def setCookie(self, key, val, domain):
            pass
        
#self.__cookie.clear() clean cookie
# vim : tabstop=2 shiftwidth=2 softtabstop=2 expandtab
