#!/usr/bin/python

import grp, pwd, os
from ctypes import *
from ctypes.util import find_library

libc = cdll.LoadLibrary(find_library('libc'))

getgrouplist = libc.getgrouplist
# 50 groups should be enought?
ngroups = 50
getgrouplist.argtypes = [c_char_p, c_uint, POINTER(c_uint * ngroups), POINTER(c_int)]
getgrouplist.restype = c_int32

grouplist = (c_uint * ngroups)()
ngrouplist = c_int(ngroups)

user = pwd.getpwuid(2540485)

ct = getgrouplist(user.pw_name, user.pw_gid, byref(grouplist), byref(ngrouplist))

# if 50 groups was not enought this will be -1, try again
# luckily the last call put the correct number of groups in ngrouplist
if ct < 0:
    getgrouplist.argtypes = [c_char_p, c_uint, POINTER(c_uint *int(ngrouplist.value)), POINTER(c_int)]
    grouplist = (c_uint * int(ngrouplist.value))()
    ct = getgrouplist(user.pw_name, user.pw_gid, byref(grouplist), byref(ngrouplist))

for i in xrange(0, ct):
    gid = grouplist[i]
    print grp.getgrgid(gid).gr_name
