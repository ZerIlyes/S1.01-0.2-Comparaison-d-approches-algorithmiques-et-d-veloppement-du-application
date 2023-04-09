#!/usr/bin/env python
# coding: utf-8
import json

def est_base(a):
    if a=="A" or a=="T" or a=="G" or a=="C":
        return True 
    else:
        return False

def est_adn(b):
    i=0
    while i<len(b):
        if est_base(b[i])==False:
            return False
        i+=1
    return True

def arn(cara):
    i=0
    t=""
    if est_adn(cara)==True:
        while i<len(cara):
            if cara[i]=="T":
                t+="U"
            else:
                t+=cara[i]
            i+=1
        return t   
    else:
        return None    

def arn_to_codons(chaine):
  i=0
  var = ""
  tab=[]
  while (i != len(chaine)):
      var += chaine[i]
      i+=1
      if i%3 == 0:
        tab.append(var)
        var=""
  return tab

def load_dico_codons_aa(lienVersJson):
    with open(lienVersJson) as leFichierJson:
        data = json.load(leFichierJson)
    return data

def codons_stop(dictionnaire):
    data = dictionnaire
    tab=[]
    i = 0
    for key, value in data.items():
         if key == "GUU":
                tab.append(value)
    return tab 
