import os
import platform

os_name = platform.system()
package_list = ['psutil==5.7.0',
                'rsa'
                ]

for s_name in package_list:
    if os_name == "Windows":
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ %s' % s_name)

    else:
        print('不支持')
