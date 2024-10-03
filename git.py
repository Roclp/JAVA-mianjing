import subprocess
import os

def git_process(folder_path):
    # 遍历文件夹及其子文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(file)
            try:
                # 执行 git add
                subprocess.run(['git', 'add', file_path], check=True)

                # 执行 git commit
                commit_message = f'"{file}"'
                subprocess.run(['git', 'commit', '-m', commit_message], check=True)

                # 执行 git push
                subprocess.run(['git', 'push', 'origin', 'main'], check=True)

                print(f'Processed {file_path}')
            except subprocess.CalledProcessError as e:
                print(f'An error occurred while processing {file_path}: {e}')

    print('All files have been processed.')

# 指定要遍历的文件夹路径
folder_path = './'

# 调用函数
git_process(folder_path)