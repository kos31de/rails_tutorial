import os
import subprocess
import re

def get_simple_name(line):
    strs = re.findall(r'[A-z\-]+[A-z]', line)
    if len(strs) == 0:
        return ''
    return strs[0]

def get_gems(res):
    gems = []
    lines = res.split('\n')
    for line in lines:
        strs = filter(lambda a: a != "", re.split(' +', line))
        if len(strs) == 0:
            continue
        if strs[0] == '***':
            continue
        elif strs[0] == 'Gem':
            str = strs[1]
        else:
            str = strs[0]
        gem_name = get_simple_name(str)
        if gem_name not in gems:
            gems.append(gem_name)
    return gems

def get_local_gems():
    res = subprocess.check_output('gem list', shell=True)
    return get_gems(res)

def get_dependency_gems(gem):
    try:
        res = subprocess.check_output('gem dependency %s' % gem, shell=True)
    except subprocess.CalledProcessError as e:
        return
    return get_gems(res)


arrays = []
gems = filter(lambda a: a != "", get_local_gems())

for gem in gems:
    dependency_gems = get_dependency_gems(gem)
    index = 0
    for current_gem in dependency_gems:
        if current_gem not in gems:
            continue
        if current_gem == gem:
            continue
        array = [gem, current_gem]
        arrays.append(array)

f = open('node.gv', 'w')
f.write("digraph {")
for array in arrays:
    gem1 = array[0].replace('-', '_')
    gem2 = array[1].replace('-', '_')
    f.write("\n")
    f.write("\t%s -> %s" % (gem1, gem2))
f.write("\n")
f.write("}")
f.close()
