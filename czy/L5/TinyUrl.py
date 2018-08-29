# TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
# 它将返回一个简化的URL http://tinyurl.com/4e9iAk.
# 要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。
# 你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL
# 可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。

import hashlib

class codeOfUrl(object):
        __author__ = 'czy'
        __slots__ = ('codeDic', 'apiurl')
        def __init__(self):
          self.codeDic = {}
          self.apiurl = "http://tinyurl.com/"
        #提取字母
        def get_alpha_str(self,s):
            result = ''.join([x for x in s if x.isalpha()])
            return result
        #Md5加密
        def calc_md5(self,string):
            md5 = hashlib.md5()
            md5.update(string.encode('utf-8'))
            return md5.hexdigest()

        #sha1加密
        def calc_sha1(self,string):
            sha1 = hashlib.sha1()
            sha1.update(string.encode('utf-8'))
            return sha1.hexdigest()

        #对url加密
        def tiny_url(self,url):
            tempMd5 = self.get_alpha_str(self.calc_md5(url))
            tempHa1 = self.get_alpha_str(self.calc_sha1(url))
            tempMethod = tempMd5[1:6] + tempHa1[2:3];
            self.codeDic[tempMethod] = url
            tinyurl =  self.apiurl + tempMethod
            return tinyurl

        #url解密
        def content_tiny_url(self,tiny_url):
            changeUrl = tiny_url.replace(self.apiurl, '')
            original = self.codeDic[changeUrl]
            return original

def main():
    a = codeOfUrl()
    b = a.tiny_url("https://leetcode.com/problems/design-tinyurl")
    c = a.content_tiny_url(b)
    print(b)
    print(c)
if __name__ == '__main__':
    main()