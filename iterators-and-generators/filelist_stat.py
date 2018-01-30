
from autotest import filelist_test,res_code
from sys import argv


def filelist(folder):
    required = ["README",
                "ex8_2nd_order.py",
                "ex8_iterators.py"
                ]



    try:
        val=filelist_test(folder, required, format='zip')
    except:
        res_code("zipfile",output="Testing zip file failed...")
        print('@@@@@@@@@@   fail   @@@@@@@@@@@')
        return val
    if val==1:
        print('@@@@@@@@@@   pass   @@@@@@@@@@@')
    if val==-1:
        print('@@@@@@@@@@   fail   @@@@@@@@@@@')
    return val
