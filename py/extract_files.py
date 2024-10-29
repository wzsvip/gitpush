import os
import re
from pyunpack import Archive

def main():
    # 打印当前工作目录
    print(f"Current working directory: {os.getcwd()}")
    
    # 查找所有正则表达式匹配的.zip文件
    zip_files = [f for f in os.listdir() if re.match(r'^[a-zA-Z0-9_]+\.zip$', f)]
    
    if not zip_files:
        raise FileNotFoundError("No .zip files found in the current directory")
    
    # 解压找到的第一个.zip文件
    zip_file = zip_files[0]
    
    # 确保目标目录存在
    unzip_dir = 'unzip'
    if not os.path.exists(unzip_dir):
        os.makedirs(unzip_dir)
    
    Archive(zip_file).extractall(unzip_dir)
    print(f"Extracted {zip_file} to {unzip_dir} directory")

if __name__ == '__main__':
    main()
