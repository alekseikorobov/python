import base64
import sys
enc = 'UTF-8'

def decode():
    source_as_hash = ''
    with open('data.txt','r',encoding=enc) as f:
        source_as_hash = f.read()
    
    source_as_text = base64.b64decode(source_as_hash.encode(enc)).decode(enc)
    with open('data.txt','w',encoding=enc) as f:
        f.write(source_as_text)

def encode():
    source_as_text = ''
    with open('data.txt','r',encoding=enc) as f:
        source_as_text = f.read()
    source_as_hash = base64.b64encode(source_as_text.encode(enc)).decode(enc)
    with open('data.txt','w',encoding=enc) as f:
        f.write(source_as_hash)
    

if __name__  == '__main__':
    if len(sys.argv) == 2:
        inp = sys.argv[1]
        if inp == '1':
            encode()
        if inp == '2':
            decode()
