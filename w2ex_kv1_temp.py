import tempfile
import os

storage_path = os.path.join(tempfile.gettempdir(), 's.d32')
if(os.path.exists(storage_path) == False):
    print('oNIIIIIIIIIIIIIIIICE')
else:
    print('oNOT NIIIIIIIIIIIIIIIIIIIICE')
    #with open(storage_path, 'w') as f:
    #    pass
#    f.write('lolol')
