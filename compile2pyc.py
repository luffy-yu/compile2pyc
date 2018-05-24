"""
编译成pyc文件
"""

__author__ = 'zej-luffy'
__date__ = '2018/4/10'

import os
import shutil
import re
from compileall import compile_dir
import sys


def run(infolder):
    compile_dir(infolder)
    basename = os.path.basename(infolder)
    # 创建目录
    out_basename = basename + '_release'
    out_dir = os.path.join(os.path.dirname(infolder), out_basename)
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)

    p = r'(.+)\.(cpython.+)\.pyc'

    for root, dirs, names in os.walk(infolder):
        for name in names:
            src = os.path.join(root, name)
            dir_name = os.path.dirname(src)
            if dir_name.find('.') != -1:
                continue

            if name.endswith('.pyc'):
                dst = os.path.dirname(os.path.dirname(src)).replace(basename, out_basename)
                ret = re.findall(p, name)
                dstname = ret[0][0] + '.pyc'
                dst = os.path.join(dst, dstname)
                if not os.path.exists(os.path.dirname(dst)):
                    os.makedirs(os.path.dirname(dst))
                shutil.copy(src, dst)

            elif not name.endswith('.py'):
                dst = src.replace(basename, out_basename)
                print(src, dst)
                if not os.path.exists(os.path.dirname(dst)):
                    os.makedirs(os.path.dirname(dst))
                shutil.copy(src, dst)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage:')
        print('python {} folder '.format(sys.argv[0]))
        exit(1)

    run(sys.argv[1])
