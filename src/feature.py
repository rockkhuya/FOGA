#!/usr/bin/python
# -*- coding: utf8 -*-
import codecs
import os
import VietProcessing
VP = VietProcessing

class Feats(str):
    """ Return features of a syllable"""
    def __init__(self, feat):
        #dinh nghia cach viet chuan
        self.chinhxac = feat
        #dinh nghia cach viet khong dau
        self.khongdau = VP.BoDauStr(feat)
        #dinh nghia dau 
        self.dau = VP.getDau(feat)
        #dinh nghia kieu type
        self.type = VP.Type(feat)
  
def changeWord(str_):
    """ Convert a VNese-char syllable to non-VNese-char syllable"""
    feat = Feats(str_)
    result = feat.khongdau + "|" + feat.dau + "|" + feat.type
    return result

def changeStr(str_):
    """Convert a Vietnamese-char string to  non-Vietnamese-char String"""
    # xoa 2 dau
    for char in " \n\t" : 
        str_ = str_.strip(char)
    # thay chu cai dau tien bang chu thuong
    str_ = str_[0].lower() + str_[1:]
    
    result = ''
    for char in ":!*?-()[]><.,;'" :
        str_ = str_.replace(char,' ' + char + '')
    str_ = str_.replace('"', ' " ')
    str_ = "BOS BOS " + str_ + " BOS BOS"
    BOW = str_.split(" ")
    for word in BOW :
        if word not in " \n\t\b" :  
            result += ' ' + changeWord(word)
    return result
 
def changeFile(filename):
    """ Convert a VNese-char file to a non-VNese-char file"""
    fi = codecs.open(filename,"r","utf8")
    fo = open(filename + ".feat","w")
    for line in fi :
        if len(line) > 10 : 
            fo.writelines(changeStr(line)+"\n")
    fi.close()
    fo.close()

path = "/home/anh/data-VNLP/docs"
FJoin = os.path.join
files = [FJoin(path, f) for f in os.listdir(path)]

count = 0
for file in files : 
    changeFile(file)
    count += 1
    print count
    
print "***Done!***"
    