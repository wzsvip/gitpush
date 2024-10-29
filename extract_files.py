import os
import re
from pyunpack import Archive

def main():
    # 切换到origin main目录
    os.chdir('main')
    
    # 查找所有正则表达式匹配的.zip文件
    zip_files = [f for f in os.listdir() if re.match(r'^[a-zA-Z0-9_]+\.zip$', f)]
    
    if not zip_files:
        raise FileNotFoundError("No .zip files found in the main directory")
    
    # 解压找到的第一个.zip文件
    zip_file = zip_files[0]
    Archive(zip_file).extractall('unzip')
    print(f"Extracted {zip_file} to unzip directory")

if __name__ == '__main__':
    main()