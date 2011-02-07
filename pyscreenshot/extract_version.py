
def extract_version(txt):
    words = txt.replace(',', ' ').split()
    version=None
    for x in words:
        if len(x)>2:
            if x[0].lower()=='v':
                x=x[1:]
            if '.' in x and x[0].isdigit() and x[-1].isdigit() and x.replace('.', '0').isdigit():
                version=x
                break
    return version

