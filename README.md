# deepin商店从上游更新应用的Python脚本

## 主要结构
```                                                                                                        | set_content
main| add Source(Thread).check() -> need update -> need_update(list) -> Download.download -> unpack -> repack| set_entries       -> call hooks( upload and update ver in db )
                                                                                                             | gen_deepin_info
                                                                                                             | gen_debian
```
### Source(info.py and infos/source/*.py)
用于检测上游版本信息，继承infos/info.py中的AbsSource，需要重写check方法并返回url和ver信息。
每个App都会根据滋生yaml文件中的meta_info中读取upstream信息，其中from为infos/source目录下的py文件，info为check时需要的信息。

### repack(package.py)
解压原有二进制压缩包，根据yaml中build_info信息将原有文件拷贝到新目录结构下，并调用对应的脚本修改需要修改的文件内容。

### yaml文件
模版在infos/pacakge_info.yaml中。

