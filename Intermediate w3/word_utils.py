import re

def clin(st):
    st_new = re.sub("[;:!?,.]", "", st)
    return st_new

def li(li):
    new_li = clin(li).split()
    return new_li

def long_word(lw):
    new_lw = max(li(lw), key=len)
    return new_lw