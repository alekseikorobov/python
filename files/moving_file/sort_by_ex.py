#
#uv run --directory /media/aleksei/home/MyProject/python/files moving_file/sort_by_ex.py
#


from loguru import logger
import os

if not os.path.isfile("log/sort_by_ex.log"):
    raise(Exception('not file path'))

logger.add("log/sort_by_ex.log", enqueue=True, rotation="500 MB",level='INFO')

categories = {
    'docs':'.docx,.doc,.pdf,.djvu,.txt,.mhtml,.htm,.html,.xps,.DOCX,.pptx,.md,.rtf,.mht,.fb2',
    'excel':'.xls,.xlsx,.csv,.xltx,.xlsm,.xlt',
    'Diagram':'.vsdx,.drawio,.eapx',
    'log':'.log',
    'Audio':'.wav,.m4a,.mp3',
    'Videos':'.wmv,.webm,.mp4',
    'Backup':'.sgbp',
    'Link':'.lnk',    
    'Torrent':'.torrent',
    'Zip':'.zip,.rar,.gz,.tgz,.tar.xz',
    'Proform':'.xsn',
    'Image':'.PNG,.png,.jpg,.JPG,.svg,.jpeg,.HEIC,.heic,.ico,.bmp',
    'Bin':'.exe,.dll,.msi,.msu,.whl,.config,.bin',
    'Scripts':'.ipynb,.bat,.markdown,.ps1,.xml,.json,.sql,.cs,.py,.wsdl,.xsd,.dtsx,.pbix,.rdl,.vsix,.nupkg,.pac,.js,.ts,.graphql,.h',
    'Messages':'.msg,.eml',
    'Tracks':'.gpx,.kml,.geojson',
    'Certificat':'.crt,.cer,.pem',
    'Other':'',#not change name!
}

base_dirs = [
    '/home/aleksei/Downloads',
    '/home/aleksei/Downloads/Telegram Desktop/'
    #r'c:\Users\akorobov\Documents',
    #r'c:\Users\akorobov\Downloads',
    #r'c:\Users\akorobov\Desktop',
    #r'c:\Users\akorobov\Documents\Other'
]

def move_file(base_dir,file_name,key):
    file_path = os.path.join(base_dir,file_name)

    if not os.path.exists(file_path):        
        logger.warning(f'file not exists {file_path}')
        return
    file_new_path = os.path.join(base_dir,key,file_name)
    if len(file_new_path) > 255:
        logger.warning(f'file {file_name} is very long')
        return

    #logger.debug(f'file new path {file_new_path}')
    index = 1
    while os.path.exists(file_new_path):
        logger.debug(f'file exists {file_new_path}')
        filename, file_extension = os.path.splitext(file_name)
        file_name_new = f'{filename} ({index}){file_extension}'
        file_new_path = os.path.join(base_dir,key,file_name_new)
        index += 1
    logger.info(f'move {file_path} -> {file_new_path}')
    os.rename(file_path,file_new_path)


def sort_by_cat(base_dir,key):
    val = categories[key]
    logger.debug(f'{key} - {val}')
    full_dir = os.path.join(base_dir,key)
    vals = val.split(',')
    logger.debug(f'vals - {tuple(vals)}')
    files = os.listdir(base_dir)

    logger.debug(f'all files - {len(files)}')

    if not 'Other' == key:        
        files = [ file for file in files if file.lower().endswith( tuple(vals) ) ]
    else:
        files = [ file for file in files if os.path.isfile(os.path.join(base_dir,file)) ]

    logger.debug(f'filtered files - {len(files)}')
    if len(files)>0:
        if not os.path.exists(full_dir):
            logger.debug(f'create dir - {full_dir}')
            os.mkdir(full_dir)
        for v in files:        
            move_file(base_dir,v,key)

if __name__ == '__main__':
    logger.info('start sorting')
    for base_dir in base_dirs:
        logger.debug(f'base_dir - {base_dir}')
        for cat in categories:
            sort_by_cat(base_dir,cat)
            logger.debug(cat)