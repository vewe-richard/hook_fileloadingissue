import subprocess
import time

# it's better to clean page cache before running the test, but it's not must
# below command clean page cache
# sync; echo 3 > /proc/sys/vm/drop_caches
#

class Hook_FileLoadingIssue:
    LINUX_FTOOLS = '/home/richard/work/fileloading/tmp/linux-ftools'

    def __init__(self, directory, files):
        self._prev_time = time.time()
        self._list_files = []
        for i_f, file_name in enumerate(files):
            self._list_files.append(directory + "/" + file_name)

    def before_loading(self, file_name):
        curtime = time.time()
        proc_time = curtime - self._prev_time
        self._prev_time = curtime
        print("hook: data processing time", proc_time)
        print("\n\nLoading new file", file_name, "......")
        self.page_cache_status()
        pass

    def after_loading(self):
        curtime = time.time()
        loading_time = curtime - self._prev_time
        self._prev_time = curtime
        print("hook: loading time", loading_time)
        self.page_cache_status()

    def page_cache_status(self):
        subprocess.run(["free"])
        args = [self.LINUX_FTOOLS + "/fincore", "--pages=false", "--summarize", "--only-cached"]
        args.extend(self._list_files)
        #print(args)
        subprocess.run(args)
        pass










