#! /usr/bin/python
# coding:utf-8
import os,shutil,getopt,sys

def iter_path(path):
    ret=[]
    src_ext=('.cpp','.c','.C','cxx')
    for dirn,dirns,filens in os.walk(path):
        for i in filens:
            fn,ext=os.path.splitext(i)
            if ext in src_ext:
                ret.append(dirn+'/'+i)
    return ret
def compiles(src_files):
    ret=[]
    obj_dir='.objs/'
    if os.path.exists(obj_dir):
        shutil.rmtree(obj_dir)
    os.mkdir(obj_dir)
    for c_file in src_files:
        if './' == c_file[0:2]:
            c_file=c_file[2:]
        out_file=obj_dir+ os.path.splitext(c_file.replace('/','_'))[0]+'.o' 
        cmd='g++ -o %s -c %s %s %s' % (out_file,c_file,cc_args,sys_cc_args)
        print(cmd)
        if 0 != os.system(cmd):
            sys.exit(-1)
        ret.append(out_file)
    return ret
def links(obj_files):
    '输出文件 obj_files sys_args link_args user_lib sys_lib'
    cmd="g++ -o %s %s %s %s %s %s" % (target," ".join(obj_files),sys_cc_args,link_args,user_lib,sys_lib)
    print(cmd)
    if 0 != os.system(cmd):
        sys.exit(-1)
    return target
def load_cfg():
    global cc_args,link_args,target,user_lib,sys_lib,sys_cc_args
    cc_args=''
    link_args=''
    target='a.out'
    user_lib=''
    sys_lib=''
    sys_cc_args=''
    args={}
    try:
        for i in range(len(sys.argv[1:])/2):
            args[sys.argv[1+i*2]] =sys.argv[2+i*2]
    except BaseException:
        pass
    try:
        target=args['-o']
    except BaseException:
        pass
    try:
        cc_args=args['-c']
    except BaseException:
        pass
    try:
        link_args=args['-l']
    except BaseException:
        pass
    cfg=[]
    for line in open(os.getenv("HOME")+"/.gcc_cfg"):
        if not line.isspace() and '#' != line[0]:
            cfg.append(line.strip())
    sys_cc_args=cfg[0]
    if cfg[1].split() > 0 :
        sys_lib=' -l '
    sys_lib+=' -l '.join(cfg[1].split())
    for i in cfg[2].split():
        if os.access(os.getenv("HOME")+"/lib/lib"+i+'.a',os.F_OK) or os.access(os.getenv("HOME")+"/lib/lib"+i+'.so',os.F_OK):
            user_lib+=" -l "+i


if __name__ == '__main__':
    load_cfg()
    srcfile = iter_path('.')
    objfile = compiles(srcfile)
    #links(objfile)
    print("输出文件为 [%s]"%links(objfile) )

