#installation Module
import pip
def install(package):
    pip.main(['install',package])
if __name__=='_main_':
    install("hashlib")

