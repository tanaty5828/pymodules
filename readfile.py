def nremove(s):
    return s.replace("\n", "")

def nstrip(filename_):
    with open(filename_) as f:
        line = f.readlines()
    result = list(map(nremove, line))
    return result
