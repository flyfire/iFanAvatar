#!/usr/bin/env python
# encoding: utf-8
"""
misc.py

Created by rex on 2010-12-01.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import commands

def getVersionInfor():
    cmd="git tag |sort -r |head -1"
    version=commands.getoutput(cmd)
    cmd='''git log -1 |grep  commit |grep -o "\<[a-f0-9]\+\>"'''
    build=commands.getoutput(cmd)
    return (version, build)
    
if __name__=='__main__':
    print getVersionInfor()
