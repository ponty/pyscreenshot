from pyscreenshot.plugin_loader import get_plugin
import pyscreenshot
import pyscreenshot as ImageGrab

backends = ['pil', 'scrot', 'imagemagick', 'pygtk'] 

def print_versions():
    print 'pyscreenshot', pyscreenshot.__version__
    for b in backends:
        x = get_plugin(force_backend=b)
        print b, 
        if x :
            print x.backend_version()
        else:
            print 'missing'

if __name__ == "__main__": 
    print_versions() 
