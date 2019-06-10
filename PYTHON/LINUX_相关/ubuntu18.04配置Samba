##### 安装Samba服务器及配置
Windows系统中安装Linux虚拟机，可以直接拖动文件，实现系统间文件的共享，但是Samba确实是需要了解的一项配置。

###### 安装配置步骤：
- 更新当前软件
    - sudo apt-get upgrade  
    - sudo apt-get update  
    - sudo apt-get dist-upgrade

- 安装samba服务器
    - sudo apt-get install samba samba-common

- 创建一个用于分享的samba目录
    - sudo mkdir /home/share

- 给创建的这个目录设置权限 
    - sudo chmod 777 /home/share    

- 添加用户(用户名 jeff，之后会需要设置samba的密码)。 
    - sudo smbpasswd -a jeff            

- 配置samba的配置文件。 
    - sudo nano /etc/samba/smb.conf 
    - 在配置文件smb.conf的最后添加下面的内容：
```python
        [share]
        comment = share folder
        browseable = yes
        path = /home/share
        create mask = 0700
        directory mask = 0700
        valid users = jeff
        force user = jeff
        force group = jeff
        public = yes 
        available = yes 
        writable = yes
``` 

- 重启samba服务器。
    - sudo service smbd restart

###### windows下访问方法 
- Windows徽标+R 在弹出的运行窗口中输入 \\ip即可访问。如\\192.168.0.127,输入samba用户名及密码访问即可看到共享，然后就可以在Linux系统与Windows系统直接进行文件共享了
- Windows徽标+E 打开计算机文件夹，点击"映射网络驱动器(M)"输入"\\192.168.0.127\share" 接着输入用户名及密码 就可以将共享文件夹添加到Windows目录中