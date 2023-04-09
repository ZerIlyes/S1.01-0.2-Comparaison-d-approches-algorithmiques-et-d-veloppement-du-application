#!/usr/bin/env python
# coding: utf-8

from biology import *
import json

def test_estbase():
    assert est_base("A")==True
    assert est_base("z")==False
    print("test ok")


def test_estadn():
    assert est_adn("ATGTCAAA")==True
    assert est_adn("ATBOAATG")==False
    print("test ok")

def test_arn():
    assert arn("ATGTCAAA")=='AUGUCAAA'
    print("test ok")

def test_arn_to_codons():
    assert arn_to_codons("CGUAAU")==['CGU','AAU']
    assert arn_to_codons("CGUAAUGC")==['CGU','AAU']
    print('test ok')    
    

print(codons_stop(load_dico_codons_aa("./codons_aa.json")))



    
