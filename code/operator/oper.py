#! /usr/bin/python
# -*- coding: UTF-8 -*-

ls = [1,2,5,7]

print ls

if( 3 in ls ):
    print "3在ls中"
else:
    print "3不在ls中"

if( 5 in ls ):
    print "5在ls中"
else:
    print "5不在ls中"

if( 5 not in ls ):
    print "5不在ls中"
else:
    print "5在ls中"