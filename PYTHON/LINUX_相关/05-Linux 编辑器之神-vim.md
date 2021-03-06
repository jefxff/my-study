##### Linux 编辑器之神——vim

###### vi 简介
- vi 只是一个文本编辑程序
- 例如：vi 1.py	表示：使用 vi 打开 1.py,如果没有 1.py 则保存成 1.py
###### vi 3种工作模式
1. 命令模式(默认模式)
	- 按 :（英文输入下的冒号）冒号，从命令模式进入末行模式
	- 在末行模式下按 Esc 退出到命令模式
2. 编辑模式（文本输入模式）
 	- 按键盘上小写字母 i (在光标的前面（左边）插入) 从命令模式进入编辑模式
	- 按键盘上大写字母 I (在光标的行首插入)从命令模式进入编辑模式
	- 按键盘上小写字母 a (在光标的后面（右边）插入)从命令模式进入编辑模式
	- 按键盘上大写字母 A (在光标的行尾插入)从命令模式进入编辑模式
	- 按键盘上小写字母 o（在光标的下一行插入）从命令模式进入编辑模式
	- 按键盘上大写字母 O（在光标的上一行插入）从命令模式进入编辑模式
 	- 按键盘上 Esc 键，从编辑模式进入命令模式 
3. 末行模式
	- 输入 :wq 表示：保存退出
	- 输入 :q! 表示：不保存退出
	- 输入 :x(小写的x)  表示：保存退出
	- 保存退出快捷方式：在命令模式下 按 Shift 键的同时连续按两次 z 键，也可以保存退出（Shift + zz)
4. 四种模式转换图（第四种是可视模式）       
<img src="https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=704307202,3977275952&fm=26&gp=0.jpg" width="750" height="450" />	
	
###### vim 基础操作
- 进入插入模式：
	- i	在光标前一个字符插入
	- I	在光标所在行首插入
	- a	在光标后一个字符插入
	- A	在光标所在行尾插入
	- o	在光标所在的下一行的行首插入
	- O	在光标所在的上一行的行首插入

- 进入命令模式：		
	- Esc:从插入模式或末行模式进入命令模式

##### 命令模式下基本操作命令：
###### 移动
- h  左移
- j  下移
- k  上移
- l  右移
- M  光标移动到中间行
- L  光标移动到屏幕最后一行行首
- G  移动到指定行，行号-G
- 15G  表示：跳转到第15行
- 1G  表示：跳转到第1行
- gg  表示：跳转到第1行
- W  向右一次移动一个字
- b  向前一次移动一个字
- {  按段移动，上移
- }  按段移动，下移
- Ctrl + d	向下翻半屏	
- Ctrl + u	向上翻半屏
- Ctrl + f	向下翻一屏
- Ctrl + b	向上翻一屏

###### 粘贴、剪切、复制命令：
- yy  复制， 8yy 表示：从当前光标所在的行开始复制8行
- p  粘贴
- dd  剪切， 2dd 表示：从当前光标所在的行开始剪切8行

###### 撤销、替换命令：
- u	 一步一步撤销
- Ctrl + r 	反撤销
- r  命令模式下替换字母
###### 删除命令：
- x	 删除光标后一个字符，相当于 Del
- X	 删除光标前一个字符，相当于 Backspace
- dd  删除光标所在行，n dd 删除指定的行数
- D  删除光标后本行所有内容，包含光标所在
- d0  删除光标前本行所有内容，不包含光标所在字符
- dw  删除光标开始位置的字符，包含光标所在的字符
###### 文本行移动：
- ">>"  (连续按两次 > )文本行右移
- "<<"  (连续按两次 < )文本行左移
###### 重复命令：
- .(英文符号下的点)重复上一次操作的命令
###### 快速查找命令：
- /	 str查找（命令模式下输入 / （斜杠），在斜杠后面输入要搜索的东西）
- n	 光标跳转到下一个查找到的东西
- N	 光标跳转到上一个查找到的东西
###### 替换命令：
- 例如：
	- 末行模式下，将文本中**所有**的 abc 替换成 123
	- :%s/abc/123/g
	- 末行模式下，将**第一行至第十行**之间的 abc 替换成 123
	- :1,10s/abc/123/g
###### vim 里执行 shell 下的命令：
- 末行模式里输入 ！，后面跟命令(如 ls pwd touch mkdir rm mv cp ...)

###### 附图vi命令树
<img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559809667564&di=3dfe1e3cbbc330c0540083f917d4635f&imgtype=jpg&src=http%3A%2F%2Fimg2.imgtn.bdimg.com%2Fit%2Fu%3D406702772%2C3851416019%26fm%3D214%26gp%3D0.jpg " width="800" height="500" />

