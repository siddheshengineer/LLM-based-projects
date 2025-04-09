import time
import os
from datetime import datetime, timedelta

## Cleanup downloads folder, to avoid stale storage issue ##

DOWNLOAD_DIR = "./downloads"
CLEANUP_INTERVAL = 3600 # time in seconds
FILE_TTL = 3600 # time in seconds

def cleanup_downloads():
    while True:
        now = datetime.now()
        cutoff = now - timedelta(seconds=FILE_TTL)

        for fname in os.listdir(DOWNLOAD_DIR):
            fpath = os.path.join(DOWNLOAD_DIR, fname)
            try:
                if os.path.isfile(fpath):
                    mtime = datetime.fromtimestamp(os.path.getmtime(fpath))

                    if mtime < cutoff:
                        os.remove(fpath)
                        print(f"Deleted: {fpath}")
            
            except Exception as e:
                print(fpath, " : ", e)
        
        time.sleep(CLEANUP_INTERVAL)


