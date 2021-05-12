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
#     res = BaseApi().send(data)
#     print(res)
#     print(res.status_code)
#     print(res.text)
#     print(res.headers)
