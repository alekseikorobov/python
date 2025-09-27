import create_note
import os
from loguru import logger
from tqdm import tqdm
import random
import time
def mass_upload():
    file_urls = 'obsidian/urls.txt'
    if os.path.isfile(file_urls):
        logger.info(f'start mass upload from file ={file_urls}')
        with open(file_urls, "r") as file:
            for line in tqdm(file.readlines()):
                line = line.strip()
                lines = line.split('\t')
                url = lines[0]
                tags = []
                if len(lines) == 2:
                    tags = lines[1].split(' ')
                status, result = '',''
                try:
                    status, result = create_note.handler(url,notify=False,tags=tags)
                    if status != 'warn':
                        time.sleep(random.randint(1,3))
                    logger.info(f'{status=}, {result=}')
                except Exception as ex:
                    result = f'{ex}'
                    logger.exception(ex)
        logger.info('done')
    else:
        logger.warning(f'not found file={file_urls}')

if __name__ == '__main__':    
    mass_upload()
    #from_buffer()
    
