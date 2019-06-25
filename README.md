# qiancheng_api

'''
框架说明：
-qiancheng_api
	-config     #配置文件目录
		--config.ini
	-data      #测试数据目录
		--test_datas.xlsx
	-log      #存放运行日志
	-report      #存放测试报告
	-src      #存放所有的程序代码
		--test_resource      #存放所有测试相关代码
			--common      #存放通用的抽离出来的代码（如web中的BasePage）
				--filepath.py      #文件路径
				http_request.py      
			--page      #PO，存放页面对象
			--suite      #测试套件，决定运行哪些case
			--testcases      #存放测试用例
				--test_api.py     
		--utils      #存放所有的支撑代码，如读取config文件、操作Excel、mysql、发送邮件等的类
			--my_logger.py      
			--operate_excel.py      
			--operate_mysql.py      
			--read_config.py      
	-run.py      #运行文件
	-READEME.md      #项目说明
'''
