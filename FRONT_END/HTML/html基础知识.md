##### html概述
- HTML是 HyperText Mark-up Language 的首字母简写，意思是超文本标记语言，超文本指的是超链接，标记指的是标签，是一种用来制作网页的语言，这种语言由一个个的标签组成，用这种语言制作的文件保存的是一个文本文件，文件的扩展名为html或者htm。
- 一个html文件就是一个网页，html文件用编辑器打开显示的是文本，可以用文本的方式编辑它，如果用浏览器打开，浏览器会按照标签描述内容将文件渲染成网页，显示的网页可以从一个网页链接跳转到另外一个网页。

##### html基本结构
###### 一个html的基本结构：
```css
    <!DOCTYPE html>  ----->文档声明    
    <html lang="en"> ----->声明HTML文档        
        <head> ----->声明网页的标题(<tltie>标题</title>)及初始化的设置                   
            <meta charset="UTF-8"> -----> 网页的编码       
            <title>网页标题</title> ----->网页的标题     
        </head>     
        <body>  ----->网页的内容        
              网页显示内容        
        </body>     
    </html>     
``` 

* 说明：第一行是文档声明，第二行`<html>`标签和最后一行`</html>`定义html文档的整体，`<html>`标签中的`lang=“en”`定义网页的语言为英文，定义成中文是`lang="zh-CN"`,不定义也没什么影响，它一般作为分析统计用。 `<head>`标签和`<body>`标签是它的第一层子元素，`<head>`标签里面负责对网页进行一些设置以及定义标题，设置包括定义网页的编码格式，外链css样式文件和javascript文件等，设置的内容不会显示在网页上，标题的内容会显示在标题栏，`<body>`内编写网页上显示的内容。

###### HTML文档类型
- 目前常用的两种文档类型是xhtml 1.0和html5   
- 快捷键：

    > `xhtml 1.0   --> html:xt + tab`

    >    

    > `html5    --> ! + tab`        

###### html文档规范
- *xhtml制定了文档的编写规范，html5可部分遵守，也可全部遵守，看开发要求。*
- 所有的标签必须**小写**

    > `<body></body>` 

- 所有的属性必须用**双引号**括起来

    > `<div class="aa" id="div1"></div>`  

- 所有标签必须**闭合**，成对标签应该成对出现，单个标签应该早结尾加 "/"

    > `<br />`      

- img必须要加alt属性(对图片的描述)    

    > `<img src="images/001.jpg" alt="道路图"> `       

- 注释

    > `<!-- 这种方式就是注释 -->`           

##### html语言标签

###### html标题
- 通过 `<h1>、<h2>、<h3>、<h4>、<h5>、<h6>`,标签可以在网页上定义6种级别的标题。6种级别的标题表示文档的6级目录层级关系，比如说：` <h1>`用作主标题（最重要的），其后是 `<h2>`（次重要的），再其次是 `<h3>`，以此类推。搜索引擎会使用标题将网页的结构和内容编制索引，所以网页上使用标题是很重要的。
```css
    <h1>这是一级标题</h1>         
    <h2>这是二级标题</h2>         
    <h3>这是三级标题</h3>         
    <h4>这是四级标题</h4>         
    <h5>这是五级标题</h5>         
    <h6>这是六级标题</h6>         
```

###### html段落
- `<p></p>`标签定义一个文本段落，一个段落含有默认的上下间距，段落之间会用这种默认间距隔开。

###### html段落换行
>  `<br />`             

###### html字符实体
- 代码中成段的文字，如果文字间想空多个空格，在代码中空多个空格，在渲染成网页时只会显示一个空格，如果想显示多个空格，可以使用空格的字符实体，代码如下：
```css
    <!--  在段落前想缩进两个文字的空格，使用空格的字符实体：&nbsp;   -->
    <p>
    &nbsp;&nbsp;一个html文件就是一个网页，html文件用编辑器打开显示的是文本，可以用<br />
    文本的方式编辑它，如果用浏览器打开，浏览器会按照标签描述内容将文件<br />
    渲染成网页，显示的网页可以从一个网页链接跳转到另外一个网页。
    </p>
```
- 在网页上显示 “<” 和 “>” 会误认为是标签，想在网页上显示“<”和“>”可以使用它们的字符实体，比如：
``` css   
    <!-- “<” 和 “>” 的字符实体为 &lt; 和 &gt;  -->          
    <p>         
        3 &lt; 5 <br>   3小于5            
        10 &gt; 5   10大于5           
    </p>            
```

###### html块、含样式的标签
- html块
    - **div标签** 块元素，表示一块内容，没有具体的语义。
    - **span标签** 行内元素，表示一行中的一小段内容，没有具体的语义。

- 含样式和语义的标签
    - **em标签** 行内元素，表示语气中的强调词
    - **i标签** 行内元素，原本没有语义，w3c强加了语义，表示专业词汇
    - **b标签** 行内元素，原本没有语义，w3c强加了语义，表示文档中的关键字或者产品名
    - **strong标签** 行内元素，表示非常重要的内容

- 语义化的标签
    - 语义化的标签，就是在布局的时候多使用语义化的标签，搜索引擎在爬网的时候能认识这些标签，理解文档的结构，方便网站的收录。比如：**h1标签**是表示标题，**p标签**是表示段落，**ul**、**li标签**是表示列表，a标签表示链接，**dl**、**dt**、**dd**表示定义列表等，语义化的标签不多。

###### html图像
- `<img>`标签可以在网页上插入一张图片，它是独立使用的标签，通过`“src”`属性定义图片的地址，通过`“alt”`属性定义图片加载失败时显示的文字，以及对搜索引擎和盲人读屏软件的支持。           
```html
    <img src="images/pic.jpg" alt="产品图片" />         
```

###### html链接
- `<a>`标签可以在网页上定义一个链接地址，通过src属性定义跳转的地址，通过title属性定义鼠标悬停时弹出的提示文字框。    
```css
    <a href="#"></a> <!--  # 表示链接到页面顶部   -->

    <a href="http://www.itcast.cn/" title="跳转的传智播客网站">传智播客</a>

    <a href="2.html">测试页面2</a>
``` 

###### 定义页面内滚动跳转
-  页面内定义了“id”或者“name”的元素，可以通过a标签链接到它的页面滚动位置，前提是页面要足够高，有滚动条，且元素不能在页面顶部，否则页面不会滚动。
```css
    <a href="#mao1">标题一</a>         
    ......          
    ......                  
    <h3 id="mao1">跳转到的标题</h3>           
``` 
##### html列表

###### 有序列表
- 快捷键 'ol>li*3'
```css
    <ol>
        <li>列表文字一</li>
        <li>列表文字二</li>
        <li>列表文字三</li>
    </ol>
``` 
- 在网页上生成的列表每条项目上会按"1,2,3"编号，有序列表在实际开发中较少使用。

###### 无序列表
- 快捷键 'ul>li*3'
- 在网页上生成的列表，每条项目上会有一个小图标，这个小图标在不同浏览器上显示效果不同，所以一般会用样式去掉默认的小图标，如果需要图标，可以用样式自定义图标，从而达到在不同浏览器上显示的效果相同,实际开发中一般用这种列表。


###### 无序列表带a标签可跳转
- 快捷键 'ul>(li>a)*5'
```css
    <ul>
        <li><a href="#">新闻标题一</a></li>
        <li><a href="#">新闻标题二</a></li>
        <li><a href="#">新闻标题三</a></li>
        <li><a href="#">新闻标题四</a></li>
        <li><a href="#">新闻标题五</a></li>
    </ul>
```

###### 定义列表
- 快捷键 'dl>(dt+dd)*3'
```css
    <dl>
    <dt>html</dt>   
    <dd>负责页面的结构</dd>

    <dt>css</dt>
    <dd>负责页面的表现</dd>

    <dt>javascript</dt> 
    <dd>负责页面的行为</dd>
    </dl>
```

##### html表格
###### table常用标签
- **table标签**：声明一个表格
- **tr标签**：定义表格中的一行
- **td和th标签**：定义一行中的一个单元格，td代表普通单元格，th表示表头单元格

###### table常用属性
- **border** 定义表格的边框
- **cellpadding** 定义单元格内内容与边框的距离
- **cellspacing** 定义单元格与单元格之间的距离
- **align** 设置单元格中内容的水平对齐方式,设置值有：left | center | right
- **valign** 设置单元格中内容的垂直对齐方式 top | middle | bottom
- **colspan** 设置单元格水平合并
- **rowspan** 设置单元格垂直合并 

###### 传统布局
- (使用table来做整体页面的布局）目前主要运用是：快速做演示的HTML页面，商业推广EDM制作(广告邮件)
- 定义表格宽高，将**border**、**cellpadding**、**cellspacing**全部设置为**0**
- 单元格里面嵌套表格
- 单元格中的元素和嵌套的表格用align和valign设置对齐方式
- 通过属性或者css样式设置单元格中元素的样式
- 表格常用样式属性（#####待续）
- **border-collapse:collapse** 设置边框合并，制作一像素宽的边线的表格  

##### html表单
- 表单用于搜集不同类型的用户输入，表单由不同类型的标签组成，实现一个特定功能的表单区域（比如：注册），首先应该用`<form>`标签来定义表单区域整体，在此标签中再使用不同的表单控件来实现不同类型的信息输入。
- **`form`**定义一个表单区域,**`action`**属性定义表单数据提交的地址，**`method`**属性定义提交的方式。
```css
    <form action="http://www.itcast.cn" method="">
```
###### text
- **type 类型 text** 是最常见的文本框类型
```css
    <div>
    <!-- type 类型 text 是最常见的文本框类型 -->
    <!-- 一个input就是一个表单控件 -->
    <!-- for 的目的:提高用户体验; 前端实现:用户点击一下左侧的用户名,也可以在文本框输入内容; -->
    <!-- 代码实现: input控件里面设置id值,让for等于id的值即可 -->
    <label for="username">用户名:</label>
    <input type="text" name="username" id="username" value="">
    </div>
```

###### password
- **type 类型 password** 是密码类型,前端输入的数据,会以原点代替
```css
    <div>
    <!-- type 类型 password 是密码类型,前端输入的数据,会以原点代替 -->
    <label for="pwd">密码:</label>
    <input type="password" name="pwd" id="pwd">
    </div>  
``` 
###### radio
- **type 类型 radio** 是互斥的,只能二者选一个
```css
    <div>
    <!-- type 类型 radio 是互斥的,只能二者选一个 -->
    <label for="">性别:</label>
    <input type="radio" name="gender" id="male" value="0"> <label for="male">男</label>
    <input type="radio" name="gender" id="female" value="1"><label for="female">女</label>
    </div>
```

###### checkbox
- **type 类型 checkbox** 是可以多选的
```css
    <div>
    <!-- type 类型 checkbox 是可以多选的 -->
    <label for="">爱好:</label>
    <input type="checkbox" name="like" id="" value="game"> 游戏
    <input type="checkbox" name="like" id="" value="shopping"> 逛街
    <input type="checkbox" name="like" id="" value="sleep"> 睡觉
    </div>  
```

###### file
- **type 类型是 file** 的,是上传照片或者文件`
```css
    <div>
    <!-- type 类型是 file 的,是上传照片或者文件 -->
    <label for="">上传照片:</label>
    <input type="file" name="">
    </div>
```
###### textarea
- 定义**多行文本**
```css
    <div>
    <!-- 定义多行文本 -->
    <label for="">个人描述:</label>
    <textarea name="info"></textarea>
    </div>  
```

###### select --> option
- 定义**下拉框** 使用**select标签** 其中的**选项使用option标签**
```css
    <div>
    <!-- 定义下拉框 使用select标签 其中的选项使用option标签 -->
    <label for="">籍贯:</label>   
    <select name="site" id="">
        <option value="0">北京</option>
        <option value="1">上海</option>
        <option value="2">广州</option>
        <option value="3">深圳</option>
        <option value="4">香港</option>
        <option value="5">澳门</option>
    </select>
    </div>
```
###### hidden
- **hidden 存储值**用的 , 本身**不**会显示出来，但是会把值传到后台去
```css
    <!-- hidden 存储值用的 , 本身不会显示出来，但是会把值传到后台去-->
    <!-- ?username=rose&pwd=111&gender=0&like=game&info=&site=0&hid=10000 -->
    <input type="hidden" name="hid" value="10000" >
```

###### submit
- **提交控件**
```css
    <!-- 提交控件 -->
    <input type="submit" name="" value="提交">    
``` 

###### reset
- **重置控件**
```css
    <!-- 重置控件 -->
    <input type="reset" name="" value="重置">
```

###### image
- **以图片作为提交控件**
```css
    <!-- 可以用一张图片来做提交  例如一张提交按钮-->
    <input type="image" name="" src="images/submit.png">
``` 

###### button
- **单纯的做一个按钮**
```css
    <!-- 单纯的做一个按钮 -->
    <input type="button" name="" value="按钮">    
```

##### html内嵌框架
- `<iframe>`标签会创建包含另外一个html文件的内联框架（即行内框架），`src`属性来定义另一个html文件的引用地址，`frameborder`属性定义边框，`scrolling`属性定义是否有滚动条。
```css
    <!-- frameborder="0"去边框， scrolling="no"去滚动条， width height设置宽，高 -->
    <iframe src="http://www.baidu.com" frameborder="0" scrolling="no" width="900" height="500" name="myframe"></iframe>
    <iframe src="01-html表单.html" frameborder="0" scrolling="no" width="900" height="500"></iframe>
``` 

##### 内嵌框架与a标签配合使用
- a标签的target属性可以将链接到的页面直接显示在当前页面的iframe中
```css
    <a href="01.html" target="myframe">页面一</a>  <br>
    <a href="02.html" target="myframe">页面二</a>
    <a href="03.html" target="myframe">页面三</a>
    <iframe src="01.html" frameborder="0" scrolling="no" name="myframe"></iframe>
```