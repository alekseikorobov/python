#
#uv run --directory /media/aleksei/home/MyProject/python/files moving_file/sort_by_ex.py
#


from loguru import logger
import os
import hashlib

if not os.path.isfile("log/sort_by_ex.log"):
    raise(Exception('not file path'))

logger.add("log/sort_by_ex.log", enqueue=True, rotation="500 MB",level='INFO')

categories = {
    'docs': '.docx,.doc,.txt,.mhtml,.htm,.html,.md,.rtf,.mht,.odt,.ott,.ps',
    'Books': '.pdf,.epub,.mobi,.azw,.azw3,.kfx,.prc,.pdb,.fb2,.lit,.chm,.djvu,.cbr,.cbz,.cbc,.cb7,.cbt,.oxps,.xps,.pdg,.tr2,.tr3,.acsm',
    'excel': '.xls,.xlsx,.csv,.csv.gz,.xltx,.xlsm,.xlt,.ods,.ots,.xlam,.xla,.xlw,.xlr',
    'presentation': '.ppt,.pptx,.pptm,.potx,.potm,.ppsx,.odp,.otp',
    'Diagram': '.vsdx,.drawio,.eapx,.vdx,.vsd,.gliffy,.dia',
    'log': '.log,.evtx,.etl,.trace,.trc,.audit',
    'Audio': '.wav,.m4a,.mp3,.ogg,.flac,.aac,.wma,.aiff,.opus,.amr,.au,.mid,.midi,.ac3',
    'Videos': '.wmv,.webm,.mp4,.avi,.mov,.mkv,.flv,.mpeg,.mpg,.3gp,.m4v,.h264,.hevc,.vob,.m2ts,.ogv',
    'Backup': '.sgbp,.bak,.backup,.gho,.tib,.v2i,.iso,.vhd,.vhdx,.vmdk',
    #'Link': '.lnk,.url,.webloc',
    'Torrent': '.torrent',
    'Zip': '.zip,.rar,.gz,.tgz,.tar.xz,.7z,.bz2,.xz,.lz,.lzma,.z,.tar,.cab,.dmg,.pkg,.rpm,.arj,.zst',
    'Proform': '.xsn',
    'image': '.png,.jpg,.svg,.jpeg,.heic,.ico,.bmp,.tiff,.tif,.webp,.raw,.nef,.cr2,.arw,.eps,.ai,.psd,.xcf,.gif,.apng,.avif,.jp2,.jxl',
    'Bin': '.exe,.dll,.msi,.msu,.whl,.config,.bin,.jar,.class,.apk,.ipa,.so,.lib,.a,.ko,.rpm,.deb,.com,.scr,.pyd,.pyc,.ocx,.cab,.sys,.drv,.dat',
    'Scripts': '.ipynb,.bat,.markdown,.ps1,.xml,.json,.toml,.sql,.cs,.py,.wsdl,.xsd,.dtsx,.pbix,.rdl,.vsix,.nupkg,.pac,.js,.ts,.graphql,.h,.cpp,.hpp,.java,.go,.rs,.php,.sh,.bash,.zsh,.fish,.pl,.lua,.r,.rb,.swift,.kt,.kts,.scala,.groovy,.dart,.jl,.f,.f90,.m,.hs,.clj,.scm,.vbs,.ahk,.psm1,.psd1,.ps1xml,.psc1,.reg,.inf,.ini,.yaml,.yml,.env,.conf,.properties,.tf,.tfvars,.proto,.thrift,.avdl,.asm,.s,.cob,.for,.pascal,.d,.odin,.zig,.nim,.v,.vala,.css',
    'Messages': '.msg,.eml,.pst,.ost,.mbox,.vcf,.ics',
    'Tracks': '.gpx,.kml,.geojson,.kmz,.plt,.tcx,.fit',
    'Certificat': '.crt,.cer,.pem,.pfx,.p12,.der,.key,.jks,.keystore,.truststore,.p7b,.p7c,.spc,.csr,.crl,.gpg,.asc,.sig,.p8,.pub,.ssh',
    'VirtualMachines': '.ova,.ovf,.vbox,.vdi,.vmdk,.vmx,.nvram,.vmem,.vmsn,.vmss,.vmtm,.vmxf',
    'CAD': '.dwg,.dxf,.stl,.step,.stp,.iges,.igs,.obj,.3ds,.fbx,.dae,.blend,.skp,.ifc,.rvt,.rfa,.rte,.pln,.lcf,.sat,.sldprt,.sldasm,.slddrw,.prt,.asm,.drw,.ipt,.iam,.idw,.catpart,.catproduct,.cgr,.model,.exp,.jt,.x_t,.x_b,.par,.psm,.asm,.pwd,.iam,.ipj,.dlv,.dgn,.mcd,.pcb,.sch,.brd,.epf,.idf,.emn,.bdf,.cad,.cam,.cdl,.cdw,.cmg,.design,.dsn,.edrw,.fmz,.idc,.idf,.idv,.ifz,.layout,.mc9,.model,.pc3,.pcbdoc,.pcblib,.phj,.pln,.pm,.pro,.prt,.psm,.ptf,.pwd,.sab,.scad,.schdoc,.schlib,.ses,.smg,.stl,.sym,.tct,.tcw,.vlm,.vs,.wrl,.xas,.xpr,.zbr',
    'Fonts': '.ttf,.otf,.woff,.woff2,.eot,.pfb,.pfm,.afm,.fon,.bdf,.pcf,.sfd',    
    'Database': '.sqlite,.sqlite3,.db,.db3,.mdb,.accdb,.frm,.ibd,.myd,.myi,.dbf,.sdf,.ldf,.mdf,.ndf,.bak,.dump,.archive,.dmp,.exp,.imp,.ora,.pdb,.wal,.journal,.db-shm,.db-wal,.kdbx,.kdb,.kdbx3,.kdbx4,.parquet,.orc,.avro,.feather,.hdf5,.h5,.sas7bdat,.sav,.dta,.jsonl,.ndjson,.tsv,.tsv.gz,.arrow,.fits,.sqlitedb',
    'Other': '',  # not change name!
}
skip_ext = '.dtmp,.rdp,.kdbx,.ini,.lnk,.desktop'
DELETE_DUPLICATE = True # если перемещаем файл, а в папке уже есть такой файл, тогда удаляем файл без перемещения

base_dirs = [
    '/home/aleksei/Downloads',
    '/home/aleksei/Downloads/Telegram Desktop/'
    #r'c:\Users\akorobov\Documents',
    #r'c:\Users\akorobov\Downloads',
    #r'c:\Users\akorobov\Desktop',
    #r'c:\Users\akorobov\Documents\Other'
]

def check_duplicate_file(file_path, file_new_path):
    #batch_size = 4096
    batch_size = None
    try:
        # Открываем первый файл в бинарном режиме и считываем блоками
        with open(file_path, 'rb') as f1:
            hash1 = hashlib.md5()
            for chunk in iter(lambda: f1.read(batch_size), b''):
                hash1.update(chunk)
        
        # Открываем второй файл в бинарном режиме и считываем блоками
        with open(file_new_path, 'rb') as f2:
            hash2 = hashlib.md5()
            for chunk in iter(lambda: f2.read(batch_size), b''):
                hash2.update(chunk)
        
        # Сравниваем хеши
        return hash1.hexdigest() == hash2.hexdigest()
    
    except FileNotFoundError:
        logger.error(f"Ошибка: Один из файлов не найден ({file_path} или {file_new_path})")
        return False
    
    except Exception as e:
        logger.error(f"Произошла ошибка при проверке файлов: {str(e)}")
        return False

    
    
def move_file(base_dir,file_name,key)->int:
    file_path = os.path.join(base_dir,file_name)

    if not os.path.exists(file_path):        
        logger.warning(f'file not exists {file_path}')
        return 0
    file_new_path = os.path.join(base_dir,key,file_name)
    if len(file_new_path) > 255:
        logger.warning(f'file {file_name} is very long')
        return 0

    #logger.debug(f'file new path {file_new_path}')
    index = 1
    while os.path.exists(file_new_path):
        logger.debug(f'file exists {file_new_path}')
        if DELETE_DUPLICATE:
            is_duplicate = check_duplicate_file(file_path, file_new_path)
            if is_duplicate:
                logger.info(f'remove {file_path}')
                os.remove(file_path)
                return 0
        filename, file_extension = os.path.splitext(file_name)
        file_name_new = f'{filename} ({index}){file_extension}'
        file_new_path = os.path.join(base_dir,key,file_name_new)
        index += 1
    logger.info(f'move {file_path} -> {file_new_path}')
    os.rename(file_path,file_new_path)
    return 1

def sort_file_by_exts(files,ext_str,reverse=False):
    exts = ext_str.split(',')
    #print(f'vals - {tuple(exts)}')
    if not reverse:
        return [ file for file in files if file.lower().endswith( tuple(exts) ) ]
    else:
        return [ file for file in files if not file.lower().endswith( tuple(exts) ) ]

def sort_by_cat(base_dir,key)->int:
    val = categories[key]
    logger.debug(f'{key} - {val}')
    full_dir = os.path.join(base_dir,key)
    files = os.listdir(base_dir)
    result_moving_count = 0

    logger.debug(f'all files - {len(files)}')

    files = sort_file_by_exts(files, skip_ext, reverse=True)
    logger.debug(f'after ignore - {len(files)}')
    
    if not 'Other' == key:        
        files = sort_file_by_exts(files, val)
    else:
        files = [ file for file in files if os.path.isfile(os.path.join(base_dir,file)) ]

    logger.debug(f'filtered files - {len(files)}')
    if len(files)>0:
        if not os.path.exists(full_dir):
            logger.debug(f'create dir - {full_dir}')
            os.mkdir(full_dir)
        for v in files:        
            result_moving_count += move_file(base_dir,v,key)
    
    return result_moving_count

if __name__ == '__main__':
    
    logger.info('start sorting')
    result_moving_count_all = 0
    for base_dir in base_dirs:
        logger.debug(f'base_dir - {base_dir}')
        for cat in categories:
            result_moving_count_all += sort_by_cat(base_dir,cat)
            logger.debug(cat)
    import time
    from notify import notification
    time.sleep(10)
    notification('sorting file', message=f'{result_moving_count_all=}', app_name='sorting file',timeout = 10000)