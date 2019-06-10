##### MySQL-NOTE-01

---
###### 安装（Linux环境下)
```sql	
 	sudo apt-get install mysql-server mysql-client
```	
	
###### 管理服务
- 启动
```sql
	service mysql start
```

- 停止
```sql
 	service mysql stop
```

- 重启
```sql
 	service mysql restart
```

- 连接命令
```sql
 	mysql -u root -p mysql
```

- 退出
```sql
 	exit/quit/ctrl+d
```
	

- 允许远程连接
	- 找到mysql配置文件并修改

	> 	sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf


	>	将bind-address=127.0.0.1注释掉

	- 登录mysql，运行命令

	>	grant all privileges on *.* to 'root'@'%' identified by 'mysql' with grant option;

 	>	flush privileges;	-- 刷新权限


	- 重启mysql	
			
###### 友情链接
- 解决root用户无法登录数据库的方法,链接如下：
	- [https://www.cnblogs.com/cpl9412290130/p/9583868.html ](https://www.cnblogs.com/cpl9412290130/p/9583868.html )
	- [http://www.cnblogs.com/py1612919884/p/9327015.html   ](http://www.cnblogs.com/py1612919884/p/9327015.html   )

- 解决图形界面配置问题
	- [https://www.cnblogs.com/tanrong/p/10173109.html](https://www.cnblogs.com/tanrong/p/10173109.html)		

---

##### 基础操作
###### 数据库相关操作
- 显示数据库版本
```sql
 	SELECT VERSION();
```

- 查看所有数据库
```sql
 	SHOW DATABSES;
```

- 创建（初始化）数据库。
```sql
  	CREATE DATABASE samp_db charset=utf8;
```
- 查看创建数据库的语句
```sql
 	SHOW CREATE DATABASE `数据库名`;
```

- 使用数据库
```sql
    USE samp_db;      
  	-- 也可以使用 mysql samp_db 激活数据库
```

- 查看当前使用的数据库
```sql
 	SELECT DATABASE();
```

- 删除数据库
```sql
 	DROP DATABASE `数据库名`;
```

- 查看当前数据库中所有表
```sql
 	SHOW TABLES;
```

----
###### 数据库中数据表相关操作
###### `创建表时用到的数据类型`
- 整数： **int**  
- 小数： **decimal** (浮点数，例如：(5,2)代表的意思就是数一共5位，小数后面占两位)
- 字符串： **char, varchar, text** (char,varchar都是有限长度的，char中存的字符固定，varchar中存的字符可变，text不指定长度)
- 日期时间： **datetime, date, time** 
- 布尔： **bit** 
- 枚举类型 **(enum)** python中没有 C语言中有（把可能出现的结果列举出来）
- 使用数据类型的原则：
	- 够用就行，尽量使用取值范围小的，而不用大的，这样可以节省存储空间
    - 对于图片、音频、视频等文件，不存储在数据库中，而是上传到某个服务器上，然后在表中存储这个文件的保存路径

###### `创建表时数据类型的约束`
- 主键 **primary key** :物理上存储的顺序
- 非空 **not null** :此字段不允许填写空值
- 惟一 **unique** :此字段不允许重复
- 默认 **default** :当不填写此值时会使用默认值，如果填写时以填写稳准
- 外键 **foreign key** :对关系字段进行约束，当为关系字段填写值时，会到关联的表中查询此值是否存在，如果存在则填写成功，如果不存在则填写失败并抛出异常
- 说明：虽然外键约束可以保证数据的有效性，但是在进行数据的crud(增加、修改、删除、查询)时，都会降低数据的性能，所以不推荐使用，那么怎么保证数据的有效性呢？ 
	- 答案：在逻辑层进行控制	
	
<br />
###### 数据表相关操作
- 创建数据表
```sql
	CREATE TABLE 表名(列名1 约束, 列2 约束);	
	
	CREATE TABLE president
		(last_name VARCHAR(15) NOT NULL,
		 first_name VARCHAR(15) NOT NULL,
		 suffix VARCHAR(5) NULL,
		 city VARCHAR(20) NOT NULL,
		 state VARCHAR(2) NOT NULL,
		 birth DATE NOT NULL,
		 death DATE NULL
		);	
```

- 也可以将表导入数据库
```sql
	mysql> LOAD DATA LOCAL INFILE "member.txt" INTO TABLE member;	
	-- 该语句读取位于客户机上当前目录中数据文件member.txt 的内容，并将其发送到服务器装入 member 表。
```
- 也可以导入*.sql的文件
```sql
	mysql samp_db < insert_president.sql
	mysql samp_db < insert_member.sql
	mysql samp_db < insert_student.sql
```

- 对表重命名
```sql
	ALTER TABLE tab_name RENAME AS new_tab_name
```

- 查看表的创建语句
```sql
	SHOW CREATE TABLE 表名字；
```

- 查看表结构
```sql
	DESC 数据表的名字；
```

- 表中插入数据
```sql
	INSERT INTO students VALUES(0, "老王", 18, 188.88, "男", 0);
```

- 修改表-**添加字段**-表添加列
```sql
	ALTER TABLE 表名 ADD 列名 类型；        
	ALTER TABLE students ADD birthday DATETIME;
```

- 修改表-修改字段：**不重命名**版--修改表的约束条件或类型
```sql
	ALTER TABLE 表名 MODIFY 列名 类型及约束；               
	ALTER TABLE students MODIFY birthday DATE;
```

- 修改表-修改字段：**重命名版**--修改列名及类型约束
```sql
	ALTER TABLE 表名 CHANGE 原名 新名 类型及约束；        
	ALTER TABLE students CHANGE birthday birth DATE DEFAULT "1990-01-01";
```

- 修改表-删除字段
```sql
	ALTER TABLE 表名 DROP 列名；  `-- 物理删除 `             
	ALTER TABLE students DROP high;
```

- 删除表
```sql
	DROP TABLE 表名； 
```
---


##### 增删改查（CURD）
- **CURD**：**C**reate(创建) **U**pdate(更新) **R**etrieve(读取)**D**elete(删除)
<br />
###### 增加 
- 全列插入
```sql
    	主键字段 可以用0 null default 来占位、代替
	insert into students values(0, "东哥", 28, 170.33, 3, 1, "1988-9-25");
	insert into students values(null, "东哥", 28, 170.33, 3, 1, "1988-9-25");
	insert into students values(default, "东哥", 28, 170.33, 3, 1, "1988-9-25");
        -- 失败 有枚举的时候，必须符合创建表时枚举所列举出的选项，不符合就会报错
	insert into students values(0, "东哥", 28, 170.33, "第四性别", 1, "1988-9-25");
	-- 枚举中的下标从1开始 1---> "男" 2--->"女"......
	insert into students values(0, "东哥", 28, 170.33, 3, 1, "1988-9-25");
```	

- 部分插入
```sql
   	insert into 表名(列1,...) values(值1,...);
	insert into students (name, gerder) values("小乔","女");
```

- 多行插入
```sql
	insert into students (name, gerder) values("大乔","女"),("貂蝉", 2);
	insert into students values(default, "西施", 28, 170.33, 3, 1, "1988-9-25"),(default, "东施", 28, 170.33, 3, 1, "1988-9-25");
```	
---

###### 删除
- 物理删除 （一般不用）
```sql
	delete from "表名" where "条件";
	delete from students; -- 整个数据表中的数据全部删除
	delete from students where name="东哥"; -- 只删除name为东哥的数据
```

- 逻辑删除（假删除--一般使用的就是这种）
```sql
	-- 用一个字段来表示 这条信息是否已经不能使用了
	-- 例如给students表添加一个 is_delete 字段 bit 类型
	alter table students add is_delete bit default 0;
	update students set is_delete=1 where id=6;
	-- 查询未被删除的数据
	select * from students where not is_delete;
	-- 查询被删除的数据
	select * from students where is_delete;
```
---

###### 修改
- `update 表名 set 列1=值1, 列2=值2... where 条件;`
```sql
	update students set gerder=1; -- 全部修改
	update students set gender=1 where name="小李飞刀";-- 只要是name是小李飞刀的,全部修改
	update students set gerder=1 where id=3;  -- 只修改id=3的值
	update students set age=33, gender=1 where id=3; -- 只要是id为3的 进行修改
```
---

###### 基本查询使用
- 查询所有列
```sql
	select * from "表名";
	select * from students;
```

- 指定条件查询
```sql
	select * from students where name="东哥";  -- 查询name为东哥的所有信息
	select * from students where id>3;  -- 查询id大于3的所有信息
```

- 查询指定列
```sql
	select "列1", "列2",... from "表名";
	select name, age from students;
```

- 可以使用as为列或者表指定别名
```sql
	select "字段"(as "别名"), "字段"(as "别名") from "数据表" where ......;
	select name as "姓名", age as "年龄" from students;
```

- 字段的顺序
```sql
	select name, age, id from students;
	select id, name, age from students;
	select id as "序号", name as "姓名", age as "年龄" from students;
```
