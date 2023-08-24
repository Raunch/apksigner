# apksigner

## 反编译
unpack.py 支持反编译

使用方法: python unpack.py apk路径名

## 回编
compile.py 支持回编

使用方法：python compile.py 反编译文件夹路径

## 重新签名
resign.py 支持重新签名
使用方法：python resign.py 需从新签名apk绝对路径


如果需要修改签名信息，请将制定签名文件拷贝至本工具路径下，同时修改constance.py文件中相应信息：

JKS_FILE_NAME为签名文件.

JKS_ALIAS为别名信息.

JKS_PASSWORK为秘钥.

```
JKS_FILE_NAME = "commonalias_pwd_common123456.jks"

JKS_ALIAS = "commonalias"

JKS_PASSWORK = "common123456"
```

