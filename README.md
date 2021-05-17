**Requests+Pytest+Allure**

~~~~说明：使用api_object分层模式~~~~
1、baseapi配置页面：
    --构建send请求方法（所有接口层都将继承send方法，即request方法）
    --单独提取获取token方法（提供给需要使用token的关联接口使用）
    --并使用Template模板替换token参数（替换yaml文件中的token，作为参数化）

2、api接口层，为每个类别的接口构建方法
    --接口层继承baseapi
    --直接return返回结果
    --注意：不要在接口层做任何断言
    
（1）getoken
（2）getuserid
（3）login
（4）getcode
...

3、basecase页面，setup初始化
    --实例化每个api接口，用例层将继承此方法

4、case中编写测试用例
    --继承basecase，并使用assert进行响应断言

5、测试数据使用yaml文件统一管理
    --yaml文件中不能使用tab缩进，只能使用空格；
    --传参格式为：json

6、result中存放使用pytest执行的测试结果，使用allure测试报告打开

使用方法：
1、直接在api层写相关接口，直接return结果；
2、在basecase中实例化（1）中新增的接口
3、在case中调用（2）中实例化的所需接口，书写测试用例，并使用assert做响应断言
4、测试数据（请求方法，请求url，请求header及请求参数）都放入data层，以yaml文件存储


执行测试用例：

1、使用pyets执行单个测试用例
`pytest test_upm.py`

2、使用pytest执行多个test文件(保存测试结果，使用allure收集)
`pytest -p no:doctest case --alluredir=result\20210512`

3、使用allure查看测试结果
`allure serve result\20210512`


Jenkins执行测试脚本可以集成Allure-Report
