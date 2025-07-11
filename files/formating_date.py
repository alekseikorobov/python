#%%
import re
def formating(dt_text):
    v = 19701231
    pattern = r'(\d{4})\W(\d{1,2})\W(\d{1,2})(\W(\d\d)|)(\W(\d\d)|)(\W(\d\d)|)'
    m = re.match(pattern,dt_text)
    if m:
        gs = m.groups()
        #print(gs)
        gs = [int(g) for g in gs if g is not None and g.isdigit()]
        result = (gs[0] * 10000) + (gs[1] * 100) + gs[2]
        #print(gs,result,result < v)
        if result < v:
            return None,None
        gs = [f'{g:02d}' for g in gs]
        return '-'.join(gs[0:3])+ ' ' + '-'.join(gs[3:]),m.group()
    
    pattern = r'(\d{1,2})(\W)(\d{1,2})\W(\d{4})(\W(\d\d)|)(\W(\d\d)|)(\W(\d\d)|)'
    m = re.match(pattern,dt_text)
    if m:
        gs = m.groups()
        sep = gs[1]
        #print(sep)
        gs = [int(g) for g in gs if g is not None and g.isdigit()]
        if sep == '/':
            #print(gs)
            result = (gs[2] * 10000) + (gs[0] * 100) + gs[1]            
            if result < v:
                return None,None
            gs = [f'{g:02d}' for g in gs]
            return (f'{gs[2]}-{gs[0]}-{gs[1]}'+ ' ' + '-'.join(gs[3:])).strip(),m.group()
        else:
            result = (gs[2] * 10000) + (gs[1] * 100) + gs[0]
            #print(gs,result,result < v)
            if result < v:
                return None,None
            gs = [f'{g:02d}' for g in gs]
            return '-'.join(gs[0:3])+ ' ' + '-'.join(gs[3:]),m.group()
        
    pattern = r'(\d{4})(\d{2})(\d{2})(.|)(\d{2})(\d{2})(\d{2})'
    m = re.match(pattern,dt_text)
    #print('='*100)
    #print(m)
    if m:
        gs = m.groups()
        gs = [int(g) for g in gs if g is not None and g.isdigit()]
        ##print(gs)
        result = (gs[0] * 10000) + (gs[1] * 100) + gs[2]
        #print(gs,result,result < v)
        if result < v:
            return None,None
        gs = [f'{g:02d}' for g in gs]
        #print(gs)
        return '-'.join(gs[0:3])+ ' ' + '-'.join(gs[3:]),m.group()
    
    pattern = r'(\d{4})(\d{2})(\d{2})'
    m = re.match(pattern,dt_text)
    #print('='*100)
    #print(m)
    if m:
        gs = m.groups()
        gs = [int(g) for g in gs if g is not None and g.isdigit()]
        ##print(gs)
        result = (gs[0] * 10000) + (gs[1] * 100) + gs[2]
        #print(gs,result,result < v)
        if result < v:
            return None,None
        gs = [f'{g:02d}' for g in gs]
        #print(gs)
        return '-'.join(gs[0:3]),m.group()
        
    return None,None