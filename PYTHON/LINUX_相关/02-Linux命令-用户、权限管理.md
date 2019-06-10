##### Linux命令--用户、权限管理

###### whoami 
- 查看当前系统当前账号的用户名。可通过 cat /etc/passwd 查看系统用户信息

###### ifconfig 查看网络状态、查看IP地址、配置网络
- windows 中使用 ipconfig
- 关闭网卡：ifconfig ens33 down
- 开启网卡：ifconfig ens33 up
- 更改IP地址：ifconfig ens33 IP地址（192.168.0.5）

###### ping 
- ping 192.168.0.4 测试网络连接是否正常

###### ssh 远程登陆
- ssh ubuntu@192.168.0.4
- ssh 用户名@IP

###### who 
- 查看当前登陆用户的信息
- who -m或am	 只显示运行 who 命令的用户名、登陆终端和登陆时间
- who -q或--count 只显示用户的登陆账号和登陆用户的数量
- who -u或--heading 只显示列标题	

###### exit 
- 远程登陆退出或者终端退出或者退出超级账户

###### useradd 
- 添加用户账号
- 使用格式：useradd [参数] 新建用户账号
- 常用选项：
	- useradd -d	指定用户登录系统是的主目录，如果不是用此参数，系统自动在 /home 目录下建立与用户名同名目录为主目录
	- useradd -m	自动建立目录
	- useradd -g	指定组目录
	- 例如：	sudo useradd 新用户名 -m -d /home/新用户名


###### passwd 
- 设置用户密码
- 在 Unix/Linux 中，**超级用户**可以使用 passwd 命令为普通用户设置或修改用户密码。用户也可以直接使用该命令来修改自己的密码，而无需在命令后面使用用户名。

###### userdel 
- 删除用户
- userdel abc(用户名)  删除 abc 用户，但不会自动删除用户的主目录
- userdel -r abc(用户名） 删除 abc 用户，同时删除用户的主目录
- 例如：sudo userdel -r 用户名

###### su 
- 切换用户
- 可以通过 su 命令来切换用户，su 后面可以加 “-”。su 和 su - 命令的不同之处在于，su - 切换到对应的用户时会将当前的工作目录自动转换到且皇后的用户主目录。
- su 需要切换的用户名
- su - 需要切换的用户名，切换用户后，还会主动跳转到该用户的家目录

###### sudo
- 当需要超级管理员的权限时需要添加，并且在命令行的最前面，后面需要添加空格
- sudo -s 表示：直接切换到 root 用户
- 输入 exit 命令退出到普通用户

###### 查看有那些用户组
- 方法一：cat /etc/group
- 方法二：groupmod + 三次Tab键

###### groupadd \ groupdel 
- 添加、删除用户组
- groupadd 新建组账号
- groupdel 删除组账号
- cat /etc/group 查看用户组

###### usermod 
- 修改用户所在组
- 使用方法：sudo usermod -g 用户组 用户名  表示：将用户名修改到用户组里面去
- 使用方法：sudo usermod -a -G 用户组 用户名 表示：将用户名添加到用户组里面去
- 注意：上面命令中 -g 后面的组一般是默认的主要组，-G 一般配合‘-a’开完成向其他组添加（表示只是这个组的成员而已）

###### 添加权限 
- 为创建的普通用户添加 sudo 权限(就是给一般用户添加超级管理员权限)新创建的用户，默认不能 sudo,需要进行一下操作
- sudo usermod -a -G adm 用户名
- sudo udermod -a -G sudo 用户名
	
	









