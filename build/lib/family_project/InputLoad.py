# -*- coding: utf-8 -*-

'''
@author: Lahari Sengupta
Created on 05.02.21

'''

from Persons import Persons
from Family import Family
import csv

class InputLoad:
    
    @staticmethod
    def load_members(file_name):
        family = object()
        try:
            f = open(file_name, mode='r', encoding='utf-8')
            reader = csv.DictReader(f)
            
            for count, line in enumerate(reader):
                name = line['name']
                gender = line['gender'] 
                mother = line['mother']
                spouse = line['spouse'] 
                children_str = line['children']
                if bool(children_str):
                    children = children_str.split(';')
                    #print(children)
                else:
                    children = []
                    
                member = Persons(name,gender,mother,spouse,children)
                
                if count == 0:
                    family = Family(member)
                elif member.get_mother_name():
                    family.add_child(member.get_mother_name(),member)
                else:
                    family.add_spouse(member.get_spouse_name(),member)
                
            f.close()
                        
        except FileNotFoundError as err:
            print(err)
            
        return family
        
        
        

