'''
题目：TinyURL 的加密与解密
TinyURL是一种URL简化服务。
比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
它将返回一个简化的URL http://tinyurl.com/4e9iAk

要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。
你的加密和解密算法如何设计和运作是没有限制的，
你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL

'''
import random,string,hashlib

prefix_str = 'http://tinyurl.com/'
letters = string.ascii_letters + string.digits
full_tiny = {}

# 做到生成6位数字（从62个字符中随机获取和组合：random） + longUrl和shortUrl是一一对应的（dict）
# 生成数据是否应该具备唯一性：若是62的6次方，得到的1个有限的数据。所以，暂时忽略数据边界问题！！！

def encodeUrl(longUrl):
    def six_addr():
        ans = ''.join([letters[random.randint(0,1000)%62] for t in range(6)])
        if ans in full_tiny.values(): # 保证唯一性
            six_addr()
        else:
            return ans

    if longUrl in full_tiny:
        return prefix_str + full_tiny[longUrl]
    else:
        suffix = six_addr()
        full_tiny[longUrl] = suffix
        return prefix_str+suffix

def decodeUrl(shortUrl):
    shortUrl = shortUrl.split('/')[-1]
    for key,value in full_tiny.items():
        if value == shortUrl:
            return key
    return None

original_str = 'https://leetcode.com/problems/design-tinyurl'
print(encodeUrl(original_str),decodeUrl(encodeUrl(original_str)))