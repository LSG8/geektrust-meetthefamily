# -*- coding: utf-8 -*-

'''
@author: Lahari Sengupta
Created on 29.01.21
Modified on 05.02.21
'''

class Persons:
       
    def __init__(self,name,gender,mother='',spouse='',children=''):
        self._name = name
        self._gender = gender
        self._mother = mother
        self._spouse = spouse
        self._children = children
    
    def get_name(self):
        return self._name
    
    def get_gender(self):
        return self._gender
    
    def get_is_married(self):
        return bool(self._spouse)
    
    def get_mother_name(self):
        return self._mother
    
    def get_spouse_name(self):
        return self._spouse
        
    def get_has_child(self):
        return bool(self._children)
    
    def get_has_this_child(self,this_child):
        for child in self._children:
            if child == this_child:
                return True
        return False
   
    def get_children_name(self):
        return self._children
    
    def set_has_child(self,new_children):
        self._children.append(new_children)
        
    def set_is_married(self,spouse):
        self._spouse=spouse
   