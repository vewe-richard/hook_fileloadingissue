from torch import torch
import os

from hook_fileloadingissue import Hook_FileLoadingIssue

search_dir = '/home/richard/work/fileloading/data/'
files = os.listdir(search_dir)

if __name__ == '__main__':

    hook = Hook_FileLoadingIssue(search_dir, files)
    for i_f, file_name in enumerate(files):
        hook.before_loading(file_name)
        file_data = torch.load(search_dir + file_name)
        hook.after_loading()

    exit(-1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
