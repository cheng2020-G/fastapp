import yaml
from string import Template

from base.test_token import TestCase


class TempLate(TestCase):
    token = TestCase().test_get_token()

    # 使用 Template 替换 yaml文件中的token，token需要从接口中提取作为参数化传递给其他接口入参使用；
    # 替换后，在yaml文件是的书写格式为：$token
    def template_token(self):
        with open('/data/get_code.yaml') as file:
            req = Template(file.read()).substitute(token=self.token)
        return yaml.safe_load(req)

# 调试
# if __name__ == '__main__':
#     TempLate().template_token()
