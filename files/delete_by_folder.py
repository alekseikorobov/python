

import os
import shutil
i = 0
count_del = 0
for root, dirs, files in os.walk(r'c:\myProject\new\Japps'):
    for name in dirs:
        if name in ['bin','.vs','obj','node_modules','packages','logs']:
            shutil.rmtree(os.path.join(root, name))
            print(os.path.join(root, name))
            count_del += 1
        i += 1
        #print(os.path.join(root, name))
print(i)
print(count_del)
