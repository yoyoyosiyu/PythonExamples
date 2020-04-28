如果没有创建虚拟环境，那么先通过pip安装virtualenv
pip install virtualenv

进入工程目录,运行
virtualenv venv

如果在命令行，那么需要先进虚拟环境，不同系统进入和退出方法不同

Unix or MacOs:
进入:source venv/bin/activate
退出:deactivate

Windows:
进入:venv\scripts\activate.bat
退出:venv\scripts\deactivate.bat

进了虚拟环境之后，再运行pip安装各种软件包，否则的话就是在全局中安装。

mysql:
pip install mysql-connector-python


### mysql
最好的帮助文档就是mysql官方的文档: https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html