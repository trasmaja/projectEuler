#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:18:55 2019

@author: adamlagevik
"""
import stanfordnlp
stanfordnlp.download('en') 
nlp = stanfordnlp.Pipeline()
doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
doc.sentences[0].print_dependencies()
