# -*- coding: utf-8 -*-

'''
@author: Lahari Sengupta
Created on 29.01.21
Modified on 06.02.21
'''

from unittest import TestCase, main
from pathlib import Path
import sys
import os
sys.path.append((os.path.dirname(__file__)))
from Family import Family
from Persons import Persons
from InputLoad import InputLoad

class TestAddMember(TestCase):
    
    path = Path(__file__)   
    family = InputLoad().load_members(str(path.parents[1])+'\\input1.txt') 

    def test_add_child_1(self):
        original_member = "Amba"
        new_member = "New"
        new_gender = "Female"
        child = Persons(new_member,new_gender,original_member)
        self.family.add_child(original_member,child)
        mom_obj = Family.get_object(self.family,original_member)
        self.assertListEqual(['Vritha','Dritha','Tritha','New'], mom_obj.get_children_name())
        
    def test_add_child_2(self):
        original_member = "Amba"
        new_member = "New"
        new_gender = "Female"
        child = Persons(new_member,new_gender,original_member)
        self.family.add_child(original_member,child)
        child_obj = Family.get_object(self.family,new_member)
        self.assertEqual('Female', child_obj.get_gender())
        
    def test_add_child_3(self):
        original_member = "Amba"
        new_member = "New"
        new_gender = "Female"
        child = Persons(new_member,new_gender,original_member)
        self.family.add_child(original_member,child)
        mom_obj = Family.get_object(self.family,original_member)
        father_obj = Family.get_object(self.family,mom_obj.get_spouse_name())
        self.assertListEqual(['Vritha','Dritha','Tritha','New'], father_obj.get_children_name())
        
    def test_add_child_4(self):
        original_member = "Arit"
        new_member = "New"
        new_gender = "Female"
        child = Persons(new_member,new_gender,original_member)
        status = self.family.add_child(original_member,child)
        self.assertEqual('CHILD_ADDITION_FAILED', status)
        
    def test_add_child_5(self):
        original_member = "Saty"
        new_member = "New"
        new_gender = "Female"
        child = Persons(new_member,new_gender,original_member)
        status = self.family.add_child(original_member,child)
        self.assertEqual('PERSON_NOT_FOUND', status)
        
    def test_add_child_6(self):
        original_member = "Vila"
        new_member = "New"
        new_gender = "Female"
        child = Persons(new_member,new_gender,original_member)
        status = self.family.add_child(original_member,child)
        self.assertEqual('CHILD_ADDITION_FAILED: NOT_MARRIED', status)
        
    def test_add_child_7(self):
        original_member = "Chitra"
        new_member = "Boy"
        new_gender = "Male"
        child = Persons(new_member,new_gender,original_member)
        self.family.add_child(original_member,child)
        self.assertEqual('Ahit Jnki', self.family.get_direct_sibling(child))
        
    def test_add_child_8(self):
        original_member = "Chitra"
        new_member = "Boy"
        new_gender = "Male"
        relation_member = "Lavnya"
        child = Persons(new_member,new_gender,original_member)
        self.family.add_child(original_member,child)
        relation_obj = self.family.get_object(relation_member)
        self.assertEqual('Ahit Boy', self.family.get_maternal_uncle(relation_obj))
        
    def test_add_child_9(self):
        original_member = "Amba"
        new_member = "New"
        new_gender = "Female"
        relation_member = "Yodhan"
        child = Persons(new_member,new_gender,original_member)
        self.family.add_child(original_member,child)
        relation_obj = self.family.get_object(relation_member)
        self.assertEqual('Tritha New', self.family.get_maternal_aunt(relation_obj))
        
    def test_add_child_10(self):
        original_member = "Satya"
        new_member = "Joki"
        new_gender = "Female"
        relation_member = "Vasa"
        child = Persons(new_member,new_gender,original_member)
        self.family.add_child(original_member,child)
        relation_obj = self.family.get_object(relation_member)
        self.assertEqual('Atya Joki', self.family.get_paternal_aunt(relation_obj))
        
    def test_add_child_11(self):
        original_member = "Satya"
        new_member = "Joka"
        new_gender = "Male"
        relation_member = "Krithi"
        child = Persons(new_member,new_gender,original_member)
        self.family.add_child(original_member,child)
        relation_obj = self.family.get_object(relation_member)
        self.assertEqual('Asva Joka', self.family.get_paternal_uncle(relation_obj))
        
    def test_add_child_12(self):
        original_member = "Satya"
        new_member = "Joka"
        new_gender = "Male"
        relation_member = "Satvy"
        child = Persons(new_member,new_gender,original_member)
        self.family.add_child(original_member,child)
        relation_obj = self.family.get_object(relation_member)
        self.assertEqual('Vyas Joka', self.family.get_brother_in_law(relation_obj))
        
        
if __name__ == "__main__":
    main()