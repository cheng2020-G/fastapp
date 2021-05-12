**Requests+Pytest+Allure** 

~~~~说明：使用api_object分层模式~~~~

1、baseapi配置页面：
（1）构建请求方法send
（2）单独提取获取token方法
（3）并使用Template模板替换token参数

2、api页面，为每个类别的接口构建方法，并且返回结果：
（1）getoken
（2）getuserid
（3）login
（4）getcode
...

3、basecase页面，setup初始化（实例化每个api接口）

4、testcase中编写测试用例，使用assert验证

5、测试数据使用yaml文件统一管理
yaml文件中不能使用tab缩进，只能使用空格；
传参格式为：json

执行测试用例：

1、使用pyets执行单个测试用例
`pytest test_upm.py`

2、使用pytest执行多个test文件(保存测试结果，使用allure收集)
`pytest -p no:doctest case --alluredir=result\20210512`

3、使用allure查看测试结果
`allure serve result\20210512`

Jenkins执行测试脚本可以集成Allure-Report
