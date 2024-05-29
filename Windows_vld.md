详细信息github：地址[KindDragon/vld: Visual Leak Detector for Visual C++ 2008-2015 (github.com)](https://github.com/KindDragon/vld)

1.官网下载地址：[vld](https://kinddragon.github.io/vld/)

结构目录
![image](https://github.com/chenyunchao1/tool/assets/96719712/0404fcfd-9b41-481f-866d-581f3413efe2)

 



2.环境配置（32的选win32，64的选win64）

 ![image](https://github.com/chenyunchao1/tool/assets/96719712/7584f227-ef06-4a70-bb65-b87fdc961ae9)

  ![image](https://github.com/chenyunchao1/tool/assets/96719712/490bd085-bbec-4951-afef-1764fd19a0c1)


![image](https://github.com/chenyunchao1/tool/assets/96719712/6ef2dc83-423e-4f4d-aaf1-3bae757a4fe2)





3.导入头文件
![image](https://github.com/chenyunchao1/tool/assets/96719712/d1cb7cd5-9b49-456a-8ef5-5d194793d79b)





4.将bin目录下的四个文件拷贝到生成的exe文件同运行目录下



可能碰到的问题
1.能正常生成exe，但是运行不起来

 不用想了，大概率是运行的四个文件vld_x64.dll、Microsoft.DTfW.DHL.manifest、dbghelp.dll、vld_x64.pdb文件没拷贝进来，或者32和64位的引用问题

2.编译不过

 可以考虑先将vld.h的导入改为绝对路径看看是否为版本不适配，在版本适合的情况下在加入git，引入相对路径



配置项

将Visual Leak Detector目录下的vld.ini复制到运行exe同目录下即可（配置设置仅在调试该程序时应用）



主要配置项

开关

![image](https://github.com/chenyunchao1/tool/assets/96719712/544c3f76-dc65-4bed-ad59-fd78741f59d2)




异常输出方式：debugger、文件、和两者都

![image](https://github.com/chenyunchao1/tool/assets/96719712/44fc6b64-7f69-4c49-8f9b-4b8bc344db76)




日志输出路径：
![image](https://github.com/chenyunchao1/tool/assets/96719712/51559648-1b5d-48ff-98a1-d7893674cb0c)



其它配置可详见配置文件中的英文解析





运行时空指vld的开关

void VLDDisable (void);

禁用函数，并且只作用于当前线程

返回值：无 （此函数始终成功） 。



void VLDEnable (void);

返回值：无 （此函数始终成功） 





将输出文件用脚本过滤

脚本所在目录：vld_result_fillter.py

运行命令：python vld_result_fillter.py targetfile

log：python vld_result_fillter.py ms_memory_leak_report.txt

后续主要对脚本的筛选目录进行维护
![image](https://github.com/chenyunchao1/tool/assets/96719712/aaae58e1-3601-47b8-866f-a07844cfd53b)





