# Linux Studies

---
- [Command](#command)
- [Wine](#wine)
- [Bash file](#bash-file)

---

![](16_LinuxStudies/16_LinuxStudies_2023-02-20-09-31-24.png)

## Command
 - **neofetch**
 - **ls**
 - **sl** - train
 - **cowsay**
 - **wine - - version** - Version command 
 - **ssh** - connect to a machine 'username@machineip'
 - **pwd** - print working directory
 - **cd** - change working directory
 - **touch** - create a file, ex. touch zac.txt
 - **cp** - copy, ex. cp zac.txt ./zac/zac.txt
 - **mv** - move, ex. cp zac.txt ./zac/zac.txt
 - **rm** - remove/delete, ex. rm zac.txt'
 - **whoami** - tell user name
 - **man/whatis** - manual, tell how to use a command, ex. man sudo 
 - **free** - check the memory 
 - **shotdown/reboot/**
 - **mkdir**  - create a new folder.
 - **rmdir** - remove a folder.
 - **chmod** - change mode 控制用户对文件的权限的命令
       - who	用户类型	说明
       - u	user	文件所有者
       - g	group	文件所有者所在组
       - o	others	所有其他用户
       - a	all	所用用户, 相当于 ugo
       - operator的符号模式表:

       - Operator	说明
       - +	为指定的用户类型增加权限
       - -	去除指定用户类型的权限
       - =	设置指定用户权限的设置，即将用户类型的所有权限重新设置
       - permission的符号模式表:

       - 模式	名字	说明
       - r	读	设置为可读权限
       - w	写	设置为可写权限
       - x	执行权限	设置为可执行权限
       - X	特殊执行权限	只有当文件为目录文件，或者其他类型的用户有可执行权限时，才将文件权限设置可执行
       - s	setuid/gid	当文件被执行时，根据who参数指定的用户类型设置文件的setuid或者setgid权限
       - t	粘贴位	设置粘贴位，只有超级用户可以设置该位，只有文件所有者u可以使用该位



## Wine
 - Wine = 'Wine Is Not an Emulator'

## Bash file
-  .bashrc文件
      在linux系统普通用户目录（cd /home/xxx）或root用户目录（cd /root）下，用指令ls -al可以看到4个隐藏文件，
      .bash_history 记录之前输入的命令
      .bash_logout 当你退出时执行的命令
      .bash_profile 当你登入shell时执行
      .bashrc 当你登入shell时执行
