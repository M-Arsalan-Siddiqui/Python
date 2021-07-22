#installation Module
import pip
def install(package):
    pip.main(['install',package])
if __name__=='_main_':
    install("hashlib") #only replace hashlib with your module name 

