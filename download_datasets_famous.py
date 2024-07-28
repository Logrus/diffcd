# Source: https://github.com/ErlerPhilipp/points2surf
import os
import zipfile
import urllib.request

source_url = r"https://www.cg.tuwien.ac.at/research/publications/2020/erler-2020-p2s/erler-2020-p2s-famous.zip"
target_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
target_file = os.path.join(target_dir, "dataset_famous.zip")

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

downloaded = 0


def show_progress(count, block_size, total_size):
    global downloaded
    downloaded += block_size
    print("downloading ... %d%%" % round(((downloaded * 100.0) / total_size)), end="\r")


print("downloading ... ", end="\r")
urllib.request.urlretrieve(source_url, filename=target_file, reporthook=show_progress)
print("downloading ... done")

print("unzipping ...", end="\r")
zip_ref = zipfile.ZipFile(target_file, "r")
zip_ref.extractall(target_dir)
zip_ref.close()
os.remove(target_file)
print("unzipping ... done")
