import requests


class BaseApi:
    # 构建request请求方法
    def send(self, data):
        return requests.request(**data)

# 调试
# if __name__ == '__main__':
#     data = {
#         "url": "http://www.baidu.com",
#         "method": "get"
#     }
#     test = BaseApi().send(data)
#     print(test)
#     print(test.status_code)
#     print(test.text)
#     print(test.headers)
