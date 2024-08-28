# MAS dfab - Endless Wall

---

Contents

- [What is NCCR DFAB](#what-is-nccr-dfab)
- [NCCR phases](#nccr-phases)
- [What is AEC](#what-is-aec)
- [NCCR principles](#nccr-principles)
- [What you can do](#what-you-can-do)
- [JSON 与 XML：](#json-与-xml)
- [JSON 与 CSV:](#json-与-csv)
- [为什么使用大写命名法](#为什么使用大写命名法)
- [os.path.relpath](#ospathrelpath)
- [关于 string 的 replace 方法，需要注意 replace 不会改变原 string 的内容。](#关于-string-的-replace-方法需要注意-replace-不会改变原-string-的内容)
- [Slice](#slice)

---

## What is NCCR DFAB

- 'NCCR' is the SNSF NCCR program
- 'NCCR' is national centers of competence in research (Swiss) which transfers the innovation into practice and industry partners. It is from Swiss National Science Foundation
- Current NCCR: 21, Completed NCCR: 15
- Construction is a bad adaptor of technologies
- Two ways of construction: prefabrication and construction

## NCCR phases

- FT1: digital timber
- FT2: digital concrete
- FT3: digital construction site
- FT4: digital collaboration

## What is AEC

- Architecture Engineering and Construction

## NCCR principles

- Collaboration, Sustainability and Transfer
- We use the things that is the best for it.
- MAS dfab alumni: 115 until now
- This year: contribute, after this year: AEC, future: share

## What you can do

- Peer networking
- Skill training
- Communication
- Career planning
- be dfab

## JSON 与 XML：

JSON 与 XML 的相同之处：

- JSON 和 XML 数据都是 "自我描述" ，都易于理解。
- JSON 和 XML 数据都是有层次的结构
- JSON 和 XML 数据可以被大多数编程语言使用

JSON 与 XML 的不同之处：

- JSON 不需要结束标签
- JSON 更加简短
- JSON 读写速度更快
- JSON 可以使用数组

## JSON 与 CSV:

- 由于 CSV 文件的简单性质，因此解析起来要简单得多，实际上，在一般情况下，对逗号进行简单的拆分会将记录分成几列。 CSV 本质上是一个数组数组或一个哈希表数组，具体取决于您的外观。
- JSON 结构比 CSV 灵活得多，因此解析起来要复杂得多。 每个元素可以无限包含子元素。 JSON 还定义了几种不同的类型。 值可以是字符串，数字，true，false，null，对象或数组。 数组包含 0 个或多个 value 元素。 对象包含键值对，其中键是字符串，并且值如上定义。

  ![](7_MASdfab_Week7/7_MASdfab_Week7_2022-11-04-10-15-53.png)

## 为什么使用大写命名法

  - ![](7_MASdfab_Week7/7_MASdfab_Week7_2022-11-06-12-07-37.png)
  - ![](7_MASdfab_Week7/7_MASdfab_Week7_2022-11-06-12-07-50.png)

  ## os.path.relpath

```Python
  # Python program to explain os.path.relpath() method

  # importing os module
  import os

  # Path
  path = "/home / User / Desktop / file.txt"

  # Path of Start directory
  start = "/home / User"

  # Compute the relative file path
  # to the given path from the
  # the given start directory.
  relative_path = os.path.relpath(path, start)

  # Print the relative file path
  # to the given path from the
  # the given start directory.
  print(relative_path)
```

- 语法:os.path.relpath(path, start =os.curdir)。参数: path:表示文件系统路径的类路径对象。start(可选):表示文件系统路径的类路径对象。给定路径的相对路径将相对于 start 所指示的目录进行计算。这个参数的默认值是 os.curdir，它是操作系统用来引用当前目录的常量字符串。类路径对象是表示路径的字符串或字节对象。返回类型:该方法返回一个字符串值，表示从起始目录到给定路径的相对文件路径。

## 关于 string 的 replace 方法，需要注意 replace 不会改变原 string 的内容。

实例：

```Python
  temp_str = 'this is a test'
  print(temp_str.replace('is','IS'))
  print(temp_str)
```

结果为：

```Python
#   thIS IS a test
#   this is a test
```

## Slice

    s[i:j] = t
    slice of s from i to j is replaced by the contents of the iterable t
