import pyscreenshot
import tempfile
import time


def run(force_backend, n, to_file):
    print 'backend:', force_backend,
    print 'n:', n,
    print 'to_file:', to_file
    start = time.time()
    for i in range(n):
        if to_file:
            f = tempfile.NamedTemporaryFile(suffix='.png', prefix='test')
            filename=f.name
            
            pyscreenshot.grab_to_file(filename, force_backend=force_backend)
        else:
            im = pyscreenshot.grab(force_backend=force_backend)
    end = time.time()
    print int(10*(end - start))/10.0, 'sec'

def test_speed():    
    run('scrot', 10, True)
    run('imagemagick', 10, True)
    
    run('scrot', 10, False)
    run('imagemagick', 10, False)

if __name__ == "__main__": test_speed() 


