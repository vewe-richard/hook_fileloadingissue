import threading
import time

import torch


class FileLoading(threading.Thread):
    def __init__(self, filepaths, max_loading_files = 8):
        threading.Thread.__init__(self)
        self._filepaths = filepaths
        self._lock = threading.Lock()
        self._datalist = []
        self._max_loading_files = max_loading_files

    def run(self):
        while True:
            self._lock.acquire()
            if len(self._filepaths) == 0:
                self._lock.release()
                return
            if len(self._datalist) > self._max_loading_files:
                self._lock.release()
                time.sleep(1)
                continue

            filepath = self._filepaths[0]
            self._lock.release()

            try:
                data = torch.load(filepath)
                self._lock.acquire()
                self._datalist.append(data)
                del self._filepaths[0]
                self._lock.release()
            except Exception as e:
                print(e)
                pass


    # return None if no more data available
    # else block till get data from list
    def get(self):
        while True:
            self._lock.acquire()
            if len(self._datalist) > 0:
                data = self._datalist.pop(0)
                self._lock.release()
                return data

            if len(self._filepaths) == 0:
                self._lock.release()
                return None
            self._lock.release()
            time.sleep(1)
        return data


if __name__ == '__main__':
    import os

    search_dir = '/home/richard/work/fileloading/data/'
    files = os.listdir(search_dir)
    filepaths = []
    for f in files:
        filepaths.append(search_dir + f)

    # pass files to be prefetched
    fl = FileLoading(filepaths)
    fl.start()

    while True:
        curtime = time.time()
        data = fl.get()
        if data is None:
            break
        print(id(data), "waiting:", time.time() - curtime)

    fl.join()

