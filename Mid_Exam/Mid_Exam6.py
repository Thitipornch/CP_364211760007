"""
Name: {ฐิติพร แช่มศิริวัฒน์}
SID: {364211760007}
Group: {MIT211}
"""
try:
    year = int(input( 'Input (ค.ศ.):' ))
except:
    year = 0

if year > 0:
    x = year + 543
    print('Output (พ.ศ.):',x,)