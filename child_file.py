# @Time : 2022/7/13 2:03
import os


def find_file(root_path):
    """
    输入：根路径
    返回：其中所有子文件路径的生成器
    """
    for file in os.listdir(root_path):
        temp_path = os.path.join(root_path, file)
        if os.path.isdir(temp_path):
            yield from find_file(temp_path)
        else:
            yield temp_path
