import os
import subprocess
from multiprocessing import Pool
from tqdm import tqdm

def mogrify_image(file):
    subprocess.run(["mogrify", "-depth", "8", "-format", "png", file])

def main(directory, processes):
    files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".png")]
    with Pool(processes) as pool:
        list(tqdm(pool.imap(mogrify_image, files), total=len(files)))

if __name__ == "__main__":
    directory = "datasets/SolWallV3/input"  # PNG画像が含まれるディレクトリへのパスを指定
    processes = 8  # 同時に実行するプロセスの数
    main(directory, processes)