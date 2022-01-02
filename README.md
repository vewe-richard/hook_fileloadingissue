# hook_fileloadingissue
a python hook used to trace time cost issue on loading large files

# 1. install fincore to watch page cache
```
cd ~
git clone https://github.com/david415/linux-ftools.git
```

Open configure.ac, change below line
AM_INIT_AUTOMAKE([linux-ftools], [1.0.0])
to
AM_INIT_AUTOMAKE

```
autoreconf -i
./configure
make
```

# 2. copy hook_fileloadingissue.py to your python project
Modify below line to the location of your linux-ftools
LINUX_FTOOLS = '/home/your-user-name/linux-ftools'

# 3. add hooks to your routine
refer to main.py, add hooks
```
    hook = Hook_FileLoadingIssue(search_dir, files)
    for i_f, file_name in enumerate(files):
        hook.before_loading(file_name)
        file_data = torch.load(search_dir + file_name)
        hook.after_loading()
```

# 4. you will get log like below
```
Loading new file inception_v3_google-1a9a5a14.pth ......
              total        used        free      shared  buff/cache   available
Mem:       16294832     4826052     9306180      592784     2162600    10555292
Swap:      10239996      359100     9880896
filename size	total pages	cached pages	cached size	cached percentage
/home/richard/work/fileloading/data//inception_v3_google-1a9a5a14.pth 108857766 26577 26577 108859392 100.000000
/home/richard/work/fileloading/data//alexnet-owt-4df8aa71.pth 244418560 59673 59673 244420608 100.000000
---
total cached size: 353280000
hook: loading time 0.061667680740356445
              total        used        free      shared  buff/cache   available
Mem:       16294832     4933388     9198844      592784     2162600    10447956
Swap:      10239996      359100     9880896
filename size	total pages	cached pages	cached size	cached percentage
/home/richard/work/fileloading/data//inception_v3_google-1a9a5a14.pth 108857766 26577 26577 108859392 100.000000
/home/richard/work/fileloading/data//alexnet-owt-4df8aa71.pth 244418560 59673 59673 244420608 100.000000
---
total cached size: 353280000
hook: data processing time 0.01607489585876465


Loading new file alexnet-owt-4df8aa71.pth ......
```











