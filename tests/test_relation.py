# -*- coding: utf-8 -*-

'''
@author: Lahari Sengupta
Created on 29.01.21

'''

from unittest import TestCase, main
from pathlib import Path
import sys
import os
sys.path.append((os.path.dirname(__file__)))
from InputLoad import InputLoad


class TestRelation(TestCase):

    path = Path(__file__)   
    family = InputLoad().load_members(str(path.parents[1])+'\\input1.txt')    

    def test_get_son_1(self):
        parent_name = "Vyan"
        parent_obj = self.family.get_object(parent_name)
        sons = self.family.get_son(parent_obj)
        self.assertEqual("Asva Vyas",sons)
        
    def test_get_son_2(self):
        parent_name = "Lika"
        parent_obj = self.family.get_object(parent_name)
        sons = self.family.get_son(parent_obj)
        self.assertEqual("NONE",sons)
        
    def test_get_son_3(self):
        parent_name = "Yodhan"
        parent_obj = self.family.get_object(parent_name)
        sons = self.family.get_son(parent_obj)
        self.assertEqual("NONE",sons)
        
    def test_get_son_4(self):
        parent_name = "Yodhn"
        parent_obj = self.family.get_object(parent_name)
        sons = self.family.get_son(parent_obj)
        self.assertEqual("PERSON_NOT_FOUND",sons)

    def test_get_daughter_1(self):
        parent_name = "Vyas"
        parent_obj = self.family.get_object(parent_name)
        daughters = self.family.get_daughter(parent_obj)
        self.assertEqual("Krithi",daughters)
        
    def test_get_daughter_2(self):
        parent_name = "Jaya"
        parent_obj = self.family.get_object(parent_name)
        daughters = self.family.get_daughter(parent_obj)
        self.assertEqual("NONE",daughters)
        
    def test_get_daughter_3(self):
        parent_name = "Ish"
        parent_obj = self.family.get_object(parent_name)
        daughters = self.family.get_daughter(parent_obj)
        self.assertEqual("NONE",daughters)
        
    def test_get_daughter_4(self):
        parent_name = "Isha"
        parent_obj = self.family.get_object(parent_name)
        daughters = self.family.get_daughter(parent_obj)
        self.assertEqual("PERSON_NOT_FOUND",daughters)
        
    def test_get_siblings_1(self):
        member_name = "Vila"
        member_obj = self.family.get_object(member_name)
        siblings = self.family.get_direct_sibling(member_obj)
        self.assertEqual("Chika",siblings)
        
    def test_get_siblings_2(self):
        member_name = "Asva"
        member_obj = self.family.get_object(member_name)
        siblings = self.family.get_direct_sibling(member_obj)
        self.assertEqual("Vyas Atya",siblings)
        
    def test_get_siblings_3(self):
        member_name = "Vasa"
        member_obj = self.family.get_object(member_name)
        siblings = self.family.get_direct_sibling(member_obj)
        self.assertEqual("NONE",siblings)
        
    def test_get_siblings_4(self):
        member_name = "Vase"
        member_obj = self.family.get_object(member_name)
        siblings = self.family.get_direct_sibling(member_obj)
        self.assertEqual("PERSON_NOT_FOUND",siblings)
        
    def test_brother_in_laws_1(self):
        member_name = "Arit"
        member_obj = self.family.get_object(member_name)
        brother_in_laws = self.family.get_brother_in_law(member_obj)
        self.assertEqual("Ahit",brother_in_laws)
    
    def test_brother_in_laws_2(self):
        member_name = "Amba"
        member_obj = self.family.get_object(member_name)
        brother_in_laws = self.family.get_brother_in_law(member_obj)
        self.assertEqual("Ish Vich Aras",brother_in_laws)
    
    def test_brother_in_laws_3(self):
        member_name = "Jnki"
        member_obj = self.family.get_object(member_name)
        brother_in_laws = self.family.get_brother_in_law(member_obj)
        self.assertEqual("NONE",brother_in_laws)
    
    def test_brother_in_laws_4(self):
        member_name = "Vese"
        member_obj = self.family.get_object(member_name)
        brother_in_laws = self.family.get_brother_in_law(member_obj)
        self.assertEqual("PERSON_NOT_FOUND",brother_in_laws)
        
    def test_sister_in_laws_1(self):
        member_name = "Jaya"
        member_obj = self.family.get_object(member_name)
        sister_in_laws = self.family.get_sister_in_law(member_obj)
        self.assertEqual("Tritha",sister_in_laws)
    
    def test_sister_in_laws_2(self):
        member_name = "Chitra"
        member_obj = self.family.get_object(member_name)
        sister_in_laws = self.family.get_sister_in_law(member_obj)
        self.assertEqual("Satya",sister_in_laws)
    
    def test_sister_in_laws_3(self):
        member_name = "Jnki"
        member_obj = self.family.get_object(member_name)
        sister_in_laws = self.family.get_sister_in_law(member_obj)
        self.assertEqual("NONE",sister_in_laws)
    
    def test_sister_in_laws_4(self):
        member_name = "Vese"
        member_obj = self.family.get_object(member_name)
        sister_in_laws = self.family.get_sister_in_law(member_obj)
        self.assertEqual("PERSON_NOT_FOUND",sister_in_laws)
        
    def test_paternal_uncle_1(self):
        member_name = "Kriya"
        member_obj = self.family.get_object(member_name)
        paternal_uncles = self.family.get_paternal_uncle(member_obj)
        self.assertEqual("Asva",paternal_uncles)
        
    def test_paternal_uncle_2(self):
        member_name = "Dritha"
        member_obj = self.family.get_object(member_name)
        paternal_uncles = self.family.get_paternal_uncle(member_obj)
        self.assertEqual("Ish Vich Aras",paternal_uncles)
        
    def test_paternal_uncle_3(self):
        member_name = "Atya"
        member_obj = self.family.get_object(member_name)
        paternal_uncles = self.family.get_paternal_uncle(member_obj)
        self.assertEqual("NONE",paternal_uncles)
        
    def test_paternal_uncle_4(self):
        member_name = "Vese"
        member_obj = self.family.get_object(member_name)
        paternal_uncles = self.family.get_paternal_uncle(member_obj)
        self.assertEqual("PERSON_NOT_FOUND",paternal_uncles)
        
    def test_maternal_uncle_1(self):
        member_name = "Vila"
        member_obj = self.family.get_object(member_name)
        maternal_uncles = self.family.get_maternal_uncle(member_obj)
        self.assertEqual("NONE",maternal_uncles)
        
    def test_maternal_uncle_2(self):
        member_name = "Lavnya"
        member_obj = self.family.get_object(member_name)
        maternal_uncles = self.family.get_maternal_uncle(member_obj)
        self.assertEqual("Ahit",maternal_uncles)
        
    def test_maternal_uncle_3(self):
        member_name = "Krithi"
        member_obj = self.family.get_object(member_name)
        maternal_uncles = self.family.get_maternal_uncle(member_obj)
        self.assertEqual("NONE",maternal_uncles)
        
    def test_maternal_uncle_4(self):
        member_name = "Vese"
        member_obj = self.family.get_object(member_name)
        maternal_uncles = self.family.get_maternal_uncle(member_obj)
        self.assertEqual("PERSON_NOT_FOUND",maternal_uncles)
        
    def test_paternal_aunt_1(self):
        member_name = "Vasa"
        member_obj = self.family.get_object(member_name)
        paternal_aunts = self.family.get_paternal_aunt(member_obj)
        self.assertEqual("Atya",paternal_aunts)
        
    def test_paternal_aunt_2(self):
        member_name = "Kriya"
        member_obj = self.family.get_object(member_name)
        paternal_aunts = self.family.get_paternal_aunt(member_obj)
        self.assertEqual("Atya",paternal_aunts)
        
    def test_paternal_aunt_3(self):
        member_name = "Laki"
        member_obj = self.family.get_object(member_name)
        paternal_aunts = self.family.get_paternal_aunt(member_obj)
        self.assertEqual("NONE",paternal_aunts)
        
    def test_paternal_aunt_4(self):
        member_name = "Vese"
        member_obj = self.family.get_object(member_name)
        paternal_aunts = self.family.get_paternal_aunt(member_obj)
        self.assertEqual("PERSON_NOT_FOUND",paternal_aunts)
        
    def test_maternal_aunt_1(self):
        member_name = "Yodhan"
        member_obj = self.family.get_object(member_name)
        maternal_aunts = self.family.get_maternal_aunt(member_obj)
        self.assertEqual("Tritha",maternal_aunts)
        
    def test_maternal_aunt_2(self):
        member_name = "Lavnya"
        member_obj = self.family.get_object(member_name)
        maternal_aunts = self.family.get_maternal_aunt(member_obj)
        self.assertEqual("NONE",maternal_aunts)
        
    def test_maternal_aunt_3(self):
        member_name = "Chika"
        member_obj = self.family.get_object(member_name)
        maternal_aunts = self.family.get_maternal_aunt(member_obj)
        self.assertEqual("NONE",maternal_aunts)
        
    def test_maternal_aunt_4(self):
        member_name = "Vese"
        member_obj = self.family.get_object(member_name)
        maternal_aunts = self.family.get_maternal_aunt(member_obj)
        self.assertEqual("PERSON_NOT_FOUND",maternal_aunts)

            
if __name__ == "__main__":
    main()
