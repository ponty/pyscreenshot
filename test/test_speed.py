import pyscreenshot
import tempfile
import time


def run(force_backend, n, to_file, bbox=None):
    print force_backend,'\t',
    if len(force_backend)<9:
        print '\t',
        
    f = tempfile.NamedTemporaryFile(suffix='.png', prefix='test')
    filename=f.name
    start = time.time()
    for i in range(n):
        if to_file:
            pyscreenshot.grab_to_file(filename, force_backend=force_backend)
        else:
            pyscreenshot.grab(bbox=bbox, force_backend=force_backend)
    end = time.time()
    print int(10*(end - start))/10.0, 'sec'

def run_all(n, to_file, bbox=None):
    print
    print 'n=%s' %  n, 'to_file:', to_file,'bounding box:', bbox
    print '------------------------------------------------------'
    run('scrot', n, to_file, bbox)
    run('imagemagick', n, to_file, bbox)
    run('pygtk', n, to_file, bbox)
    
def test_speed():    
    run_all(10, True)
    run_all(10, False)
    run_all(10, False, (10,10,20,20))


if __name__ == "__main__": 
    test_speed() 


