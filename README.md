# CONST-DEMO
在服务器端部署yolov5算法并实现与客户端交互的demo

运行环境：`ubuntu20.04` `Anaconda3-2020.07-Linux-x86_64.sh` `pytorch1.7` `yolov5-3.1`(魔改版，即yolov5-3.1-new文件夹中代码)

运行方法：

* 进入`yolov5-3.1-new/detect.py`文件，将`get_frame()`函数中

    > file_path = os.path.join('/home/luka/TransmissionTest', 'new' + old_file_name)

语句中，`join()`函数中的路径修改为自己部署时`TransmissionTest`文件夹的真实路径
* 进入`TransmissionTest/client.py`文件，将
    > filepath='./test/newbus.jpg'

语句中等号右侧的路径修改为自己想要传输的图片的真实路径。

在服务器端部署`yolov5-3.1-new`文件夹，进入其中，运行

> source activate
> conda activate pytorch1.7
> python detect.py

在客户端进入`TransmissionTest`文件夹,运行

>python client.py

即可运行成功