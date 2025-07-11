


def fix_text(last_partial_text:str,text:str):
    if text.startswith(last_partial_text) and len(text)>len(last_partial_text):
        ost = text.replace(last_partial_text,'')
        return ost
    
    return ''


if __name__ == '__main__':
    last_partial_text = 'поставил стрижку нам'
    text='поставил стрижку нам на понедельник'
    fix_text(last_partial_text,text)