import subprocess
import os

def git_process(folder_path):
<<<<<<< HEAD
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
=======
    # 定义压缩文件的扩展名
    compress_extensions = {'.zip', '.rar', '.tar.gz', '.gz', '.7z'}

    # 遍历文件夹及其子文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            try:
                # 检查文件是否是压缩文件
                if os.path.splitext(file)[1].lower() in compress_extensions:
                    # 如果是压缩文件，直接执行命令
                    commit_message = f'"Update compressed file: {file}"'
                else:
                    # 获取不带扩展名的文件名
                    filename_without_extension = os.path.splitext(file)[0]
                    commit_message = f'"{filename_without_extension}"'

                # 执行 git add
                subprocess.run(['git', 'add', file_path], check=True)

                # 执行 git commit
                subprocess.run(['git', 'commit', '-m', commit_message], check=True, shell=True)

                # 执行 git push
                subprocess.run(['git', 'push', 'origin', 'main'], check=True, shell=True)

                print(f'Processed {file_path}')
            except subprocess.CalledProcessError as e:
                print(f'An error occurred while processing {file_path}: {e}')

    print('All files have been processed.')

# 指定要遍历的文件夹路径
folder_path = r'C:\cdpan\2023面试大全'

# 调用函数
git_process(folder_path)
>>>>>>> 8db71bf7e9ff68e161c385e9bebb822458c7f9a0
