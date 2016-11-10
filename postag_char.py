# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:58:22 2016

@author: han

This script puts postag labels to words in a sentence.
 
"""

import sys
from pyltp import Segmentor
from pyltp import Postagger


def main():
    segmentor = Segmentor()  # 初始化实例
    segmentor.load("/home/han/Ltp/3.3.1/ltp_data/cws.model")
    postagger = Postagger() # 初始化实例
    postagger.load("/home/han/Ltp/3.3.1/ltp_data/pos.model")
    file1 = open(sys.argv[1],"r")
    file2 = open(sys.argv[2],"w")
    count = 0
    for line in file1:
        line = line.strip()
        words = segmentor.segment(line)
        postags = postagger.postag(words)
        line = [w+"_"+p for (wd,p) in zip(words,postags) for w in wd.decode("utf-8")] 
        line = " ".join(line)+"\n"
        file2.write(line.encode("utf-8"))
        count = count + 1
        if count%10000==0:
            print "%d lines processed"%count
        #break
    file1.close()
    file2.close()
    
if __name__=="__main__":
    main()
    
