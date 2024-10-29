import os
import subprocess

def main():
    # 配置git用户信息
    subprocess.run(['git', 'config', '--local', 'user.email', 'wuzhij@mail.com'])
    subprocess.run(['git', 'config', '--local', 'user.name', 'wzsvip'])
    
    # 添加更改并提交
    subprocess.run(['git', 'add', '.'])
    commit_message = "Unzipped files from main directory"
    subprocess.run(['git', 'commit', '-m', commit_message])
    
    # 推送更改到远程仓库
    remote_url = "https://github.com/wzsvip/git.git"
    subprocess.run(['git', 'remote', 'set-url', 'origin', remote_url])
    subprocess.run(['git', 'push', 'origin', 'main'])
    print("Pushed changes to remote repository")
    
    # 删除unzip目录
    os.rmdir('unzip')
    print("Deleted unzip directory")

if __name__ == '__main__':
    main()