import os
import shutil


def delete_logs_directories(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'logs' in dirnames:
            logs_dir = os.path.join(dirpath, 'logs')
            if '.git' in dirpath:
                continue
            print(f'Deleting contents of: {logs_dir}')
            shutil.rmtree(logs_dir)
            os.makedirs(logs_dir)  # Recreate the empty logs directory


if __name__ == "__main__":
    project_root = '.'
    delete_logs_directories(project_root)
