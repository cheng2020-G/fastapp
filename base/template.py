import yaml
from string import Template

from base.get_token import GetParameters


class TempLate(GetParameters):
    code = GetParameters().get_code()
    token = GetParameters().get_token()

    # 使用 Template 替换 yaml文件中的token，token需要从接口中提取作为参数化传递给其他接口入参使用；
    # 替换后，在yaml文件是的书写格式为：$token
    def template_token(self):
        with open('D:/script/fastapp/data/user_system.yaml') as file:
            req = Template(file.read()).substitute(token=self.token)
        return yaml.safe_load(req)


# if __name__ == '__main__':
#     TempLate().template_token()
