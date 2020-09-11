# coding:utf-8
import hmac

secret_key1 = b'This is my secret key'
message1 = b'Hello world'
hex_res1 = hmac.new(secret_key1, message1, digestmod="MD5").hexdigest()
print(hex_res1)

