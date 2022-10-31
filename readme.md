- #### 工程说明
    - pipexport.sh用来导出本地安装的包列表到 requirements.txt 文件
    - pipinstall.sh用来根据requirements.txt安装依赖包
    - 用例存放规则 app/{应用名}/{模块名}/{场景}.py 例如 故障上报 app/aios/fault/test_report_fault.py
    - 测试使用的url统一放在apiurl.py中的ApiUrl枚举维护,需要写好相对地址及说明
    - http状态相关的放在app/{应用名}/httpcommon.py中维护
    - 如果在自己分支上引入了新的库，请运行pipexport.sh导出依赖方便其他同学安装，同时更新readme
    - 通用功能维护在根路径下common，如果只有自己应用的测试用例用到维护在app/{系统}/common下
    - 请求使用的数据维护在app/{系统}/data下
    - 可复用的断言维护在 app/{应用}/common/common_assert中
- #### 相关引用框架
    - 测试框架
        - [pytest](https://docs.pytest.org/en/7.1.x/)
        - [pytest中文](https://www.osgeo.cn/pytest/contents.html)
    - allure桥接器
        - [allure-pytest](https://github.com/allure-framework/allure-python)
    - requests http请求库
        - [requests](https://requests.readthedocs.io/projects/cn/zh_CN/latest/)
    - allure
        - allure主要用于根据pytest测试用例的结果生成图表
        - [说明文档](https://qualitysphere.github.io/ext/allure/#1-%E5%85%B3%E4%BA%8E)
- #### 关于allure
    - @allure.epic 用于定义一个业务系统名称例如GTS值班长工作台、铜雀
    - @allure.feature 用于定义一个大的业务模块 比如故障、风险等
    - @allure.story 用于定义一个大的业务模块中的具体业务场景比如创建故障、故障恢复、报障GOC等
    - @allure.severity 用于标明一个allure.story的严重性，不允许直接写字符串需要引用TestCaseSeverity的定义
- #### pytest
    - 一些默认约定
        - 测试用例的文件必须以test_开头
        - 测试类必须以Testxxxxx命名
        - 测试类中的方法必须以test_开头
- #### 生成报告
    - 执行测试用例
    ```
    pytest app/  --alluredir=./result --clean-alluredir
    ```
    - 以服务形式生成测试报告
    ```
  allure serve ./result
  ```