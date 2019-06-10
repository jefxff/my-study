##### Ubuntu 中软件安装
###### 更换Ubuntu中的镜像
- 寻找国内镜像源（镜像源即提供下载软件的地方）
	- 清华大学 TUNA 镜像源： https://mirrors.tuna.tsinghua.edu.cn
- 找到对应的 Ubuntu 版本
	- 将系统自带的软件源配置文件做个备份，将该文件替换为下面内容，即可使用 TUNA 的软件源镜像。

- 备份 Ubuntu 默认的源地址
	- Ubuntu 的软件源配置文件是 /etc/apt/sources.list
	- 备份命令： sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
- 更换 sources.list 中的源
	- 将 sources.list 中的内容删除掉，将从清华软件源复制的内容粘贴到文件中，保存退出
- 更新源服务器列表
	- sudo apt-get update

###### Ubuntu 软件操作的相关命令  
- sudo apt-get update ---> 更新源
- sudo apt-get install package ---> 安装包
- sudo apt-get remove package ---> 删除包
- sudo apt-cache search package ---> 搜索软件包
- sudo apt-cache show package ---> 获取包的相关信息，如说明，大小，版本等
- sudo apt-get install package --reinstall ---> 重新安装包
- sudo apt-get -f insatll ---> 修复包
- sudo apt-get remove package --purge ---> 删除包，包括配置文件等
- sudo apt-get bulid-dep package ---> 安装相关的编译环境
- sudo apt-get upgrade ---> 更新已安装的包
- sudo apt-get dist-upgrade ---> 升级系统
- sudo apt-cache depends package ---> 了解使用该包依赖那些包
- sudo apt-cache rdepends package ---> 查看该包被那些包依赖

