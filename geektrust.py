# -*- coding: utf-8 -*-

'''
@author: Lahari Sengupta
Created on 29.01.21
Modified on 05.02.21
'''

import sys
from InputLoad import InputLoad
from Family import Family
from Persons import Persons

def get_relations(family,target,relation):
    member_obj = family.get_object(target)
    switcher = { 
            'Son': family.get_son(member_obj), 
            'Daughter': family.get_daughter(member_obj), 
            'Siblings': family.get_direct_sibling(member_obj),
            'Brother-in-law': family.get_brother_in_law(member_obj),
            'Sister-in-law': family.get_sister_in_law(member_obj),
            'Maternal-aunt': family.get_maternal_aunt(member_obj),
            'Paternal-aunt': family.get_paternal_aunt(member_obj),
            'Maternal-uncle': family.get_maternal_uncle(member_obj),
            'Paternal-uncle': family.get_paternal_uncle(member_obj)
        } 
    return switcher.get(relation, 'Not a valid relation')
    
def find_result(family,work):
    if work[0] == 'ADD_CHILD':
        mother = work[1].capitalize().strip()
        if mother == 'Queen':
            i = 3 #shift index by one
        else:
            i = 2 #keep as it is
        child = work[i].capitalize().strip()
        gender = work[i+1].capitalize().strip()
        return family.add_child(mother,Persons(child,gender,mother))
    elif work[0] == 'GET_RELATIONSHIP':
        target = work[1].capitalize().strip()
        if target == 'King' or target == 'Queen':
            i = 3 #shift index by one
        else:
            i = 2 #keep as it is
        relation = work[i].capitalize().strip()
        return get_relations(family,target,relation)
    else:
        return "Instruction is not valid in the test file"

def read_test_file(file_name,family):
    
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f]
    
    for line in lines:
        #print(line)
        instruction = line.split(" ")
        print(find_result(family,instruction))
     
    return 0

def main():
    
    family = InputLoad().load_members('input1.txt')
    
    try:
        test_file = sys.argv[1]
        read_test_file(test_file,family)
    except:
        print("Please provide the test file as an argument") 
 
if __name__ == "__main__":
    main()