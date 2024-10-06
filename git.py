import subprocess
import os

def git_process(folder_path):
    compress_extensions = {'.zip', '.rar', '.tar.gz', '.gz', '.7z'}

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # 判断是否为压缩文件，设置 commit message
                if os.path.splitext(file)[1].lower() in compress_extensions:
                    commit_message = f'Update compressed file: {file}'
                else:
                    filename_without_extension = os.path.splitext(file)[0]
                    commit_message = filename_without_extension

                # 执行 git add
                subprocess.run(['git', 'add', file_path], check=True)
                print(f'Added {file_path} for commit.')

                # 执行 git commit
                subprocess.run(['git', 'commit', '-m', commit_message], check=True)
                print(f'Successfully committed {file_path}.')

                # 提交成功后，立即执行 git push
                subprocess.run(['git', 'push', 'origin', 'main'], check=True)
                print(f'Successfully pushed {file_path} to repository.')

            except subprocess.CalledProcessError as e:
                print(f'Error processing {file_path}: {e}')
                continue  # 发生错误时跳过此文件，继续处理下一个文件

# 指定要遍历的文件夹路径
folder_path = '.'

# 调用函数
git_process(folder_path)
