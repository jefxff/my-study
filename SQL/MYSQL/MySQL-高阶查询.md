##### 进阶---数据查询      
以一个完整的从创建数据库到创建数据表，学习MySQL的查询知识

###### 数据准备
- 创建一个数据库
```sql
    create database python_test charset=utf8;
```

- 使用数据库
```sql
    use python_test;
```

- 显示使用的当前的那个数据库？
```sql
    select database();
```

- 创建学生表
```sql
    create table students(
        id int unsigned primary key auto_increment not null,
        name varchar(20) default '',
        age tinyint unsigned default 0,
        heigh decimal(5,2),
        gender enum('男', '女','中性', '保密') default '保密',
        cls_id int unsigned default 0,
        is_delete bit default 0
    );
```

- 创建班级表
```sql
    create table classes(
        id int unsigned auto_increment primary key not null,
        name varchar(30) not null
    );
```

- 向学生表插入数据
```sql
    insert into students values
        (0, '小明', 18, 180.00, 2, 1, 0),
        (0, '小月月', 18, 180.00, 2, 2, 0),
        (0, '彭于晏', 29, 185.00, 1, 1, 0),
        (0, '刘德华', 59, 175.00, 1, 2, 1),
        (0, '黄蓉', 38, 160.00, 2, 1, 0),
        (0, '凤姐', 28, 150.00, 4, 2, 1),
        (0, '王祖贤', 18, 172.00, 2, 1, 1),
        (0, '周杰伦', 36, null, 1, 1, 0),
        (0, '陈坤', 27, 181.00, 1, 2, 0),
        (0, '刘亦菲', 25, 166.00, 2, 2, 0),
        (0, '金星', 33, 162.00, 3, 3, 1),
        (0, '静香', 12, 180.00, 2, 4, 0),
        (0, '郭靖', 12, 170.00, 1, 4, 0),
        (0, '周杰', 34, 176.00, 2, 5, 0),
        (0, '津实', 18, 172.00, 2, 2, 0);
```

- 向班级表插入数据
```sql
    insert into classes values
        (0, 'python_01期')   , 
        (0, 'python_02期'),
        (0, 'python_04期'), 
        (0, '菜鸟班');
```
--- 

##### 查询
###### 基础查询
- 查询所有字段
```sql
    -- select * from 表名;
    select * from students;
    select * from classes;
```

- 查询指定字段
```sql
    -- select 列1, 列2,... from 表名;
    select name, age from students;
```

- 使用 as 给字段起别名
```sql
    -- select 字段 as 名字... from 表名;
    select name as '姓名', age as '年龄' from students;
```

- select 表名.字段 ... from 表名;
```sql
    select students.name, students.age from students;
```

- 可以通过 as 给表起别名
```sql
    -- select 别名.字段 ... from 表名 as 别名;
    select students.name, students.age from students;
    select s.name, s.age from students as s;
```

- 消除重复行
```sql
    -- distinct 字段
    select distinct gender from students;
```

----

######条件查询
- 比较运算符
```sql
    -- select ... from 表名 where ...
    -- > "大于"
    -- 查询大于18岁的信息
    select * from students where age>18;    
    select id, name, gender from students where age>18;

    -- < "小于"
    -- 查询小于18岁的信息
    select * from students where age<18;

    -- >= "大于等于"
    -- <= "小于等于"
    -- 查询小于或者等于18岁的信息
    select * from students where age<=18;

    -- = "等于"
    -- 查询年龄为18岁的所有学生的名字
    select * from students where age=18;

    -- != 或者 <> "不等于"
    select * from students where age!=18;
```

- 逻辑运算符
```sql
    -- and
    -- 18到28之间的所有的学生的信息
    select * from students where age>18 and age<28;
    -- select * from students where age>18 and <28; -- 失败

    -- 18岁以上的女生
    select * from students where age>18 and gender=2;
    select * from students where age>18 and gender='女';

    -- or
    -- 18岁以上或者身高超过180(包含) 以上
    select * from students where age>18 or heigh>=180;

    -- not
    -- 不在 18岁以上的女性 这个范围内的信息
    select * from students where not (age>18 and gender=2);

    -- 年龄不是小于或者等于18 并且是女性
    select * from students where not <=18 and gender=2;
```

----

###### 模糊查询
- **like**
```sql
    -- `%` 替换1个或者多个，也可以没有
    -- `_` 替换1个，必须有一个
    -- 查询姓名中 以 “小” 开始的名字
    select name from students where name like "小%";

    -- 查询姓名中 有 “小” 的所有名字
    select name from students where name like "%小%";

    -- 查询有2个字的名字
    select name from students where name like "__";

    -- 查询有3个字的名字
    select name from students where name like "___";

    -- 查询至少有2个字的名字
    select name from students where name like "__%";
``` 

- **rlike **正则
```sql
    -- 查询以 周开始的名字
    select name from students where name rlike "^周.*";

    -- 查询以 周开始、伦结尾的姓名  -- 引号中间是正则表达式
    select name from students where name rlike "^周.*伦$";
    select name from students where name rlike "^周.+伦$";
```

----

###### 范围查询
- **in (1, 3, 8)**表示在一个非联系的范围内(记住用法)
```sql
    -- 查询 年龄为18、34的姓名
    select name, age from students where age=18 or age=34;
    select name, age from students where age in (18,12,34);
```

- **not in** 不在非连续的范围内
```sql
    -- 年龄不是 18、34岁之间的信息
    select name, age from students where age not in (18,12,34);
```

- **between ... and ... **表示在一个连续的范围内
```sql
    -- 查询 年龄在18到34之间的信息
    select name, age from students where age between 18 and 34;
``` 

- **not between ... and ... **表示不在一个连续的范围内
```sql
    -- 查询 年龄不在18到34岁之间的信息
    select * from students where age not between 18 and 34;
    -- select * from students where not age between 18 and 34; -- 不要记这种
    -- not between 是一个整体
    -- select * from students where age not (between 18 and 34); -- 失败的
```

----

###### 空判断
- 判断 **is null**
```sql
    -- 查询身高为空的信息
    select * from students where hrigh is null;
```

- 判断非空 **is not null** 
```sql
    select * from students where hrigh is not null;
``` 

----

###### 排序
- **order by 字段 asc/desc;**
    - asc从小到大排序，即升序
    - desc从大到小排序，即降序
```sql
    -- 查询年龄在18到34岁之间的男性，按照年龄从小到大排序
    select * from students where (age between 18 and 34) and gender=1;
    -- 下面两条语句的结果一样
    select * from students where (age between 18 and 34) and gender=1 order by age;
    select * from students where (age between 18 and 34) and gender=1 order by age asc;

    -- 查询年龄在18到34岁之间的女性，身高从高到低排序
    select * from students where (age between 18 and 34) and gender=2 order by heigh desc;
```

- **order by 多个字段**;
```sql
    -- 查询年龄在18到34岁之间的女性，身高从高到低排序，如果身高相同的情况下按照年龄从小到大排序
    select * from students where (age between 18 and 34) and gender=2 order by heigh desc, age asc;

    -- 查询年龄在18到34岁之间的女性，身高从高到低排序，如果身高相同的情况下按照年龄从小到大排序，
    -- 如果年龄也相同那么按照id从小到大排序
    select * from students where (age between 18 and 34) and gender=2 order by heigh desc, age asc, id asc;

    -- 按照年龄从小到大排序，身高从高到低排序
    select * from students order by age, heigh desc;
```



###### 聚合函数（一些普通的函数）
- 总数 **count**
```sql
    -- 查询男性多少人，女性多少人    
    select * from students where gender=1;
    select count(*) from students where gender=1;
    select count(*) as '男性人数' from students where gender=1;
    select count(*) as '女性人数' from students where gender=2;
```

- 最大值 **max**
```sql
    -- 查询最大年龄
    select max(age) from students;

    -- 查询女性的最高身高
    select max(heigh) from students where gender=2;
```

- 最小值 **min**
```sql
    select min(heigh) from students where gender=2;
```

- 求和 **sum**
```sql
    -- 计算所有人的年龄总和
    select sum(age) from students;
``` 

- 平均值 **avg**
```sql
    -- 计算平均年龄
    select avg(age) from students;

    -- 计算平均年龄 sum(age)/count(*)
    select sum(age)/count(*) from students;
```

- 四舍五入 **round**(123.23, 2),保留2位小数
```sql
    -- 计算所有人的平均年龄，保留2位小数
    select round(avg(age), 2) from students;
    select round(sum(age)/count(*), 2) from students;

    -- 计算男性的平均身高，保留2位小数
    select round(avg(heigh) ,2) from students where gender=1;
``` 


###### 分组(分组和聚合一起使用才有分组的意义)
- **group by** 
```sql
    -- 按照性别分组，查询所有的性别
    select gender from students group by gender;
    -- 失败 select * from students group by gender;

    --计算每种性别中的人数
    select gender, count(*) from students group by gender;

    --显示每种性别，并显示姓名
    select gender, group_concat(name) from students group by gender;

    -- 计算男性的人数
    select gender, count(*) from students where gender=1 group by gender;
``` 

- **group_concat(...)**
```sql
    -- 查询同种性别中的姓名
    select gender, group_concat(name) from students group by gender;
    -- 查询同种性别中的姓名、年龄、id
    select gender, group_concat(name, age, id) from students group by gender;
    -- 显示男性的姓名、年龄及id
    select gender, group_concat(name,"_", age,"_", id) from students where gender=1 group by gender;
``` 

- **having**
```sql
    -- 查询平均年龄超过30岁的性别， 以及姓名 having avg(age) > 30
    select gender, group_concat(name), avg(age) from students group by gender having avg(age)>30;
    -- 查询每种性别中人数多于2个的信息
    select gender, group_concat(name) from students group by gender having count(*)>2;
``` 


###### 分页
- **limit start, count;**
```sql
    -- 限制查询出来的数据个数  -- 显示男性前两个数据
    select * from students where gender=1 limit 2;

    -- 查询前五个数据
    select * from students limit 0, 5;

    -- 查询id6-10（包含）的书序
    select * from students limit 5, 5;

    -- 每页显示2个，第1个页面
    select * from students limit 0, 2;

    -- 每页显示2个，第2个页面
    select * from students limit 2, 2;

    -- 每页显示2个，第3个页面
    select * from students limit 4, 2;

    -- 每页显示2个，第4个页面
    select * from students limit 6, 2;    -- limit(第N-1页)*每个个数， 每页的个数；

    -- 每页显示2个，显示低6页的信息，按照年龄从小到大排序（limit 永远放在最后面）
    -- select * from students limit 2*(6-1),2;   -- 失败的
    -- select * from students limit 10,2 order by age asc;   -- 失败的
    select * from students order by age asc limit 10, 2;

    select * from students where gender=2 order by heigh desc limit 10, 2;
``` 


###### 连接查询,多表查询的时候用
- **inner join ... on**           
如下图:           
![avatar](https://s3.51cto.com/oss/201903/18/1c327cd4dcd88941d003719b71a9ad4c.jpg-wh_651x-s_2566142183.jpg)

```sql
    -- select ... from 表A inner join 表B;
    select * from students inner join classes;

    -- 查询 有能够对应班级的学生以及班级信息
    select * from students inner join classes on students.cls_id=classes.id;

    -- 按照要求显示姓名、班级
    select students.*, classes.name from students inner join classes on students.cls_id=classes.id;
    select students.name, classes.name from students inner join classes on students.cls_id=classes.id;

    -- 给数据表起名字
    select s.name, c.name from students as s inner join classes as c on s.cls_id=c.id;

    -- 查询 有能够对应班级的学生以及班级信息，显示学生的所有信息，只显示班级名称
    select s.*, c.name from students as s inner join classes as c on s.cls_id=c.id;

    -- 在以上的查询中，将班级姓名显示在第一列
    select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id;

    -- 查询 有能够对应班级的学生以及班级信息，按照班级进行排序
    -- select c.xxx s.xxx from students as s inner join classes as c on ... order by ...;
    select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id order by  c.name;

    
    -- 当是同一个班的时候，按照学生的id从小到大排序
    select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id order by  c.name, s.id;
``` 

- left join 
```sql
    -- 查询每位学生对应的班级信息   -- 谁写在 left join 的左边，就以谁为基准
        -- 有的就显示，没有的就显示为 null
    select * from students as s left join classes as c on s.cls_id=c.id;

    -- 查询没有对应班级信息的学生
    -- select ... from xxx as s left join xxx as c on ... where ...    -- 从源表里面判断结果
    -- select ... from xxx as s left join xxx as c on ... having ...   -- 查询出来的结果集里面找东西
    select * from students as s left join classes as c on s.cls_id=c.id having c.id is null;
    select * from students as s left join classes as c on s.cls_id=c.id where c.id is null;
```

- right join on 用的很少
    - 将数据表名字互换位置， 用 left join 完成


###### 自关联
- 自关联的表，一张表里面的字段关联表里的另外一个字段，熟悉省， 县， 市的查询用法
```sql
    -- 一张表里面的字段关联表里面的另外一个字段
    -- 导入 areas.sql
    -- source areas.sql
    

    -- 省级联动 url:http://demo.lanrenzhijia.com/2014/city0605/

    -- 查询所有省份
    select * from areas where pid is null;

    -- 查询出山东省有哪些市

    -- 第一种方法
    -- 第一步 查出山东省的pid
    select pid from areas where atitle="山东省";
    -- 第二步 查出pid为山东省的所有信息
    select * from areas where pid=37000;

    -- 第二种方法    
    select * from areas as province inner join areas as city on city.pid=province.aid having province.atitle="山东省";
    select province.atitle, city.atitle from areas as province inner join areas as city on city.pid=province.aid having province.atitle="山东省";

    -- 使用子查询(时间比较慢一点，性能比较慢)
    select * from areas where pid = (select aid from areas where atitle="山东省");
```

###### 子查询(一个select 中嵌套一个 select)
```sql
    -- 标量子查询
    -- 查询出高于平均身高的信息


    -- 查询出最高的男生信息
    select * from students where heigh = (select max(heigh) from students);


    -- 列级子查询
    -- 查询学生的班级号能够对应的学生信息
    -- select * from students where cls_id in (select id from classes);
    select * from students where cls_id in (select id from classes) order by cls_id;
```