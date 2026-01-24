---
title: "ArchLinux安装教程"
description: "乔治网的遗产，记忆的重拾，随笔+教程"
date: 2026-01-22
image: https://www.helloimg.com/i/2026/01/24/69741efb655d4.jpg
categories:
    - 教程
    - 随笔
tags:
    - 随笔
    - Linux
    - 教程
---
*这是一篇乔治网（George Website）的遗产，之前发表在了知乎，现在改了改，写了一些随笔，重新发布在 Victory Blog*

## 前言
我一直以来是 Windows 的忠实用户，从古老的 xp 到 2003 到 visit 到 win7 ， win8 ...我都用过，大多数的感受是微软再也不震撼人心了...

我用过 win11 的泄露版本，当时我还在小学，突然网上流传了泄密的 win11 ，我重装了系统，然而 win11 泄露版并不好用，存在着许多 BUG ，我无奈回到了 win10 ，这期间丢失了许多在 C 盘写的一些随笔，后来我做了 win11 to go 。后来发布的 win11 预览版我并没用，因为 win11 的泄密版对我打击很大，后来，我来到了 win11 正式版。惊喜却少了许多……

我有一台 MacBook ，但是我并不满足，我总是渴望着折腾完黑苹果后的那种快感，无奈黑苹果对我来说是不可能的。

我是一个编程爱好者，虽然只是爱好者，但喜欢折腾，然后我就盯上了 Linux 。

我虽然使用 Linux 的时间不是很长，但我走了很多路，最早的 Cent OS ，然后 Ubuntu ，再然后统信 UOS ，期间安装过虚拟机，也安装过实体机，我还试过 WSL ， Archlinux 是我最后选择的一款系统。

Archlinux 是一款不错的系统，就是很难上手。

写到这，它更多地不再是一个教程，而是一个随笔。

##  ArchLinux 安装指南
### 一.分区（这一步要在 Windows 中进行）
我们要准备 Diskgenius 进行分区。

首先要准备一个大于 30 GB 的 ROOT 分区，博主用的 50 GB ，如果你是 Linux 专业人员，酌情考虑。

其次我们还需要一个 6GB 左右的 SWAP 分区。

这些需要在 Windows 下工作， Mac 用户建议不要尝试。
### 二.制作系统u盘

这个和做winpe有点像。

1.首先进入[ArchLinux官网](http://archlinux.org)。

2.右上角 “Download” ， “BitTorrent Download (recommended)” ， “Torrent for 2020.04.01” （数字为当前版本号），下载了种子文件后，可以用迅雷、 bitcomet 、 qbittorrent 、 FDM 等工具下载。

3.到[rufus官网](rufus.ie)下载rufus，这是写入镜像工具。

4.在大大的 “Download” 下边找到并点击 “Rufus 3.9 Portable” （数字为版本号），下载。双击运行，点“选择”，找到之前下载的 ArchLinux 的ISO文件，开始以ISO文件写入。

### 三.正式安装

首先进入bois更改启动项（请您百度自行查询）。

#### 0.如果您的键盘不好使，解决办法

每次引导到 Linux 前，请在 GRUB 界面按 “e” ，找到 “linux” ，在句末添加 `i8042.dumbkbd` 。

#### 1.联网

##### （1）有线连接者输入ip a即可联网

##### （2）如果您需要无线连接，请执行以下命令

a.输入`iwctl`；

b.进入 iwd 模式后，输入`device list`；

c.查看您的网卡名字，一般情况是 wlan0 ，那么输入`station wlan0 scan`；

d.检查扫描网络，输入`station wlan0 get-networks`；

e.查看您的网络名称,输入`station wlan0 connect "您的wlan名称”`；

f.输入您的密码，然后就连上网络了；

g.退出 iwd 模式，输入`exit`；

##### （3）检查网络，输入`ping www.baidu.com`，如果显示延迟等数据后， <kbd>CTRL</kbd> + <kbd>C</kbd> 退出。

#### 2.更新系统时间

请输入`timedatectl set-ntp true`

#### 3.列出磁盘分区表

（1）请输入`fdisk -l`

（2）找到您的 ROOT 分区的设备名 `/dev/nvme0n1pX` 和 SWAP 分区的设备名 `/dev/nvme0n1pX` 和 EFI 分区的设备名 `/dev/nvme0n1p1` （X代表数字）

#### 4.格式化分区

（1）输入`mkfs.ext4 /dev/root_partition`（ root_partition 指的是根分区例如 nvme0n1p4 ）

（2）输入`mkswap /dev/swap_partition`（ swap_partiton 指的是交换空间分区）

#### 5.挂载分区

（1）输入`mount /dev/root_partition /mnt` ( root_partition 指的是根分区例如 nvme0n1p4 )

（2）输入`mkdir /mnt/boot`

（3）输入`mkdir /mnt/boot/efi`

（4）输入`mount /dev/nvme0n1p1 /mnt/boot/efi`（默认 efi 分区是 nvme01p1 )

#### 6.更换 Pacman 镜像

（0）推荐清华源

（1）输入`vim /etc/pacman.d/mirrorlist`

（2）按一下i键进入写入模式

（3）将白色部分第一行 `https://xxx.xxx.xxx.xxx/`部分改为 `https://mirrors.tuna.tsinghua.edu.cn/`（这是清华源的改法，其他请自行百度）

（4）其他部分不要动！按下 <kbd>ESC</kbd> + <kbd>w</kbd> + <kbd>q</kbd> 退出 VIM

#### 7.安装 ArchLinux 及软件包

请输入

```
{
  pacstrap /mnt base linux linux-firmware base-devel sof-firmware nano vi vim man-db man-pages texinfo networkmanager modemmanager iw net-tools dosfstools exfatprogs exfat-utils e2fsprogs ntfs-3g plasma kde-utilities sddm grub intel-ucode amd-ucode sudo efibootmgr mesa xf86-video-intel vulkan-intel libva-intel-driver libvdpau-va-gl intel-compute-runtime lib32-vulkan-intel lib32-mesa intel-gpu-tools nvidia nvidia-prime nvidia-settings nvidia-utils opencl-nvidia lib32-nvidia-utils lib32-opencl-nvidia libva-vdpau-driver xf86-video-amdgpu vulkan-radeon libva-mesa-driver mesa-vdpau opencl-mesa lib32-vulkan-radeon lib32-mesa noto-fonts-cjk noto-fonts-emoji os-prober dolphin
}
```

不要输入错了，这里面包含 ArchLinux 系统、大多数基本包、驱动程序、上网包、字体和 KDE 桌面环境

#### 8.生成 Fstab

输入`genfstab -U /mnt >> /mnt/etc/fstab`

#### 9. Chroot

输入`arch-chroot /mnt`

这将进入新的系统，原先的 /mnt 目录已经成为当前的 /（root）目录

#### 10.时区

输入`ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime hwclock --systohc`

#### 11.本地化

vim 编辑` /etc/locale.gen`，然后取消掉` en_US.UTF-8 UTF-8 和 zh_CN.UTF-8 UTF-8 前的注释（#）`

然后`locale-gen`

然后 VIM 创建 `locale.conf` 文件，输入`vim /etc/locale.conf`

并填写`LANG=en_US.UTF-8`

警告： 不要在此设置任何中文 locale，会导致 tty 乱码。

#### 12.主机名

VIM 创建 `/etc/hostname` 文件，输入`vim /etc/hostname`,填写主机名

#### 13.生成初始化内存盘

输入`mkinitcpio -P`

#### 14.设置 ROOT 密码

输入`passwd`

#### 15.添加用户

输入`useradd -m -G "wheel" "您的用户名"`

#### 16.设置用户密码

输入`passwd 您的用户名`

#### 17.让用户可以使用 sudo

输入`vim /etc/sudoers`

将同时含有` wheel 与 nopasswd 的一行取消注释（#）`然后 <kbd>:</kbd> + <kbd>w</kbd> + <kbd>q</kbd> + <kbd>!</kbd> 保存（这个文件需要添加感叹号以保存）

#### 18.安装启动加载程序（UEFI）

输入`grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB && grub-install --target=x86_64-efi --efi-directory=/boot/efi --removable`

#### 19.启用 OS-Prober、修复键盘并生成启动加载配置（UEFI）

（1）输入`vim /etc/default/grub`

（2）找到` # GRUB_DISABLE_OS_PROBER=false `行将其取消注释（#）。

（3）找到以 quiet 结尾的一行空一格并添加 `i8042.dumbkbd`

（4）然后，执行 `grub-mkconfig -o /boot/grub/grub.cfg`

#### 20.重新启动到 BIOS 来设置启动项目

重新启动到 BIOS。

设置“GRUB”为第一启动项，设置 Windows Boot Manager 为第二启动项，如果没有 GRUB，设置你的硬盘名为第一启动项。（如果您经常使用windows，您可以把Windows Boot Manager设置为第一启动项，但是您要进archlinux需要进入Bois更改）

#### 21.启动到新系统并设置服务

重新启动到 GRUB 并选择 Arch Linux。使用 root + 您设定的 root 密码登录到 TTY。登录完成后，执行以下命令

`systemctl enable sddm && systemctl enable NetworkManager && reboot`

这将启用 SDDM 登录管理器和网络组件，如果一切正确，您将在重启后看到 SDDM 登录屏幕

#### 22.设置 ArchLinuxCN 软件包源并安装实用工具

（1）重新启动到 GRUB 并选择 Arch Linux。您应该看到 SDDM 登录屏幕。

（2）使用您自己创建的用户登录到 SDDM。

（3）登录到 Plasma 后，在开始菜单中搜索 “Konsole” 来进入 Konsole。

（4）输入`sudo vim /etc/pacman.conf`

（5）找到 #[custom] 。取消该行以及下面两行（共三行）的注释并将` file:///开头的 URL `替换为`https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch`

（6）然后按 <kbd>:</kbd> + <kbd>w</kbd> + <kbd>q</kbd> 保存退出。

（7）安装 ArchLinuxCN 密钥串：

（a）输入`sudo pacman -S archlinuxcn-keyring`

（b）安装 YAY ：输入`sudo pacman -S yay`

（8）安装 DEBian To Arch Package ：输入`yay -S debtap`

#### 23.到此，恭喜您，您的archlinux安装完成，尽情玩吧！！！
## 后记
这是我在2022年写的一篇文章，里面的教程仍然可以用，今天写这篇文章也没参考2022年往后的教程了，时间过得真的好快，乔治网（George Website）的文字基本上也灰飞烟灭了，这也是乔治网（George Website）仅剩的遗产了，怀念当初折腾的日子，虽然那时已经知道这么折腾一点用处没有，普通人和Linux几乎无缘。

{\{< detail "点这里看隐藏内容！" >}}
看到这里的都是我的朋友，去看看别的文章吧！Have a good day !🥰
{\{< /detail >}}