import os
from tqdm import tqdm
import subprocess
from dotenv import load_dotenv
load_dotenv()
base_path = os.getenv('BASE_PATH')
print(base_path)


def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

s_all = 0
for file in tqdm(os.listdir(base_path)):    
    full_path = os.path.join(base_path,file)    
    l = get_length(full_path)
    s_all += l

print(s_all)