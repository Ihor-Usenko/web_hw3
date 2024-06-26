import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor

def copy_file(pool_file, push_dir):
    os.makedirs(push_dir, exist_ok=True)
    shutil.copy2(pool_file, push_dir)

def process_directory(pool_dir, push_dir):
    tasks = []
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(pool_dir):
            for file in files:
                pool_file = os.path.join(root, file)
                extension = os.path.splitext(file)[1][1:]
                dest_dir = os.path.join(push_dir, extension)
                tasks.append(executor.submit(copy_file, pool_file, dest_dir))


if __name__ == "__main__":
    pool_directory = sys.argv[1]
    push_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"

    process_directory(pool_directory, push_directory)
