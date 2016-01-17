Title: 运维安全系列基础服务之FTP服务
Date: 2015-12-26 10:11
Modified: 2015-12-28 13:58
Category: security
Tags: operation, security, ftp
Slug: operation-security-ftp
Authors: Michael Cho
Summary: 这是有关运维安全话题的系列，主要包括下面四个方面：基础服务，网络层，应用层，云安全。今天主要讲的是基础服务里面的[FTP服务][ftp]。


这是有关运维安全话题的系列，主要包括下面四个方面：
  - 基础服务
  - 网络层
  - 应用层
  - 云安全

今天主要讲的是基础服务里面的[FTP服务][ftp]。

> 文件传输协议（英文：File Transfer Protocol，缩写：FTP）是用于在网络上进行文件传输的一套标准协议。它属于网络传输协议的应用层。
> FTP是一个8位的客户端-服务器协议，能操作任何类型的文件而不需要进一步处理，就像MIME或Unicode一样。但是，FTP有着极高的延时，
> 这意味着，从开始请求到第一次接收需求数据之间的时间，会非常长；并且不时的必须执行一些冗长的登陆进程。
> (https://zh.wikipedia.org/wiki/%E6%96%87%E4%BB%B6%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE)

从现在来看，FTP服务应该算是一个“漏洞百出”的TCP/IP协议。在Google搜索`ftp 攻击`或者其它类似FTP安全的关键词，会列出成千上万的结果。
特别是还有`anonymous ftp`这种buggy的设计。为什么会出现这种情况呢，这还需要从FTP协议设计的目的来看，RFC959中开篇介绍中就列出了FTP协议的4个目的：

* to promote sharing of files 
* to encourage indirect or implicit
* to shield a user from variations in file storage systems among hosts
* to transfer data reliably and efficiently

这些目的中没有任何关于安全方面的描述，很多FTP工具也仅仅是满足上面列出的FTP协议的目的，所以FTP协议被当做黑客攻击的目标就不足为奇了。下面主要从两个方面来讲讲FTP的安全问题，最后给出一些安全使用FTP的建议。
  - anonymous ftp
  - ftp bounce attack

## Anonymous FTP

Anonymous FTP也称作匿名FTP服务。上面说过，FTP最主要的目的就是为了在互联网上共享文件和数据，通常使用FTP服务是需要在服务端注册账号后才能使用的，而匿名FTP是建立了一个特殊的名为`anonymous`的用户ID，方便Internet上的任何人在任何地方无需注册账号就可使用该用户ID来进行文件共享。既然任何人都可以使用这个账号，这也为黑客侵入提供了便利。通常的做法是：
1. 通过匿名账号的写权限上传木马实施攻击；
2. 通过启动FTP daemon的系统账号权限进行攻击；
3. 通过匿名账号启动系统shell；
4. 即使没有上述所有权限，也可以通过大规模的`登录/退出`操作让系统日志快速增长，从而吃满服务器空间让服务器挂掉；

所以匿名FTP服务是一项非常危险的服务，如非必要，建议关闭此服务，使用HTTP/HTTPS服务来提供文件共享服务。以vsftpd为例，关闭匿名FTP服务的方法是：

```sh
cat /etc/vsftpd.conf
# Access rights
anonymous_enable=NO
no_anon_password=NO
```

然后重启vsftp服务即可。

即使需要保留匿名FTP，也有以下建议：
  - 关闭匿名用户的上传数据权利，并提供下载数据文件的校验文件
  - 使用无特权账号和组(比如nobody)来启动FTP daemon
  - 给匿名FTP账号使用假的shell(/bin/false or /bin/true)
  - 限制FTP账号在一定时间段内的登录次数

## FTP bounce attack

FTP bounce attack(FTP跳转攻击)是利用FTP规范中的漏洞来攻击知名网络服务器的一种方法，并且使攻击者很难被跟踪。首先攻击者通过FTP服务器发送一个FTP"PORT"命令给目标FTP服务器，其中包含该主机的网络地址和被攻击的服务的端口号。这样，客户端就能命令FTP服务器发一个文件给被攻击的服务。这个文件可能包括根被攻击的服务有关的命令（如SMTP,NNTP等）。由于是命令第三方去连接到一种服务，而不是直接连接，就使得跟踪攻击者变得困难，并且还避开了基于网络地址的访问限制。如下图所示：

![ftp bounce attack][ftp_bounce_attack]

可以看出，实施FTP跳转攻击的关键是利用FTP协议中的PORT命令来打开目标机器上的特点端口来实施攻击。所以阻止FTP跳转攻击的策略也基本都是围绕这一步来进行的。一般FTP跳转攻击首先都需要上传一个攻击文件到FTP服务器，然后再传送到目标机器，所以第一个方法也是上面提到的，禁止FTP服务器的写入功能。当然，即使禁止了FTP服务器的写入功能，攻击者还是可以通过发送其它命令的方式进行攻击，所以这个不能完全杜绝FTP跳转攻击。另外，FTP服务的默认端口是20，21，所以避免跳转攻击的另外一个建议就是在服务器上不要打开数据链接到小于1024的TCP端口号。当然最彻底的办法就是禁用PORT命令，但这会使FTP服务器丧失代理的功能。

[//]: # (These are reference links used in the body of this note )

   [ftp]: https://www.ietf.org/rfc/rfc959.txt
   [ftp_bounce_attack]: https://hakin9.org/wp-content/uploads/2014/05/f81.jpg
   [1]: https://www.giac.org/paper/gsec/748/ftp-security-hole-about/101645
   [2]: http://www.cnpaf.net/rfc/rfc2577.txt
   [3]: http://www.nsfocus.net/index.php?act=magazine&do=view&mid=1214
   [4]: http://www.ouah.org/ftpbounce.html
 
