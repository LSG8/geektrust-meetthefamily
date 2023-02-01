# -*- coding: utf-8 -*-

'''
@author: Lahari Sengupta
Created on 05.02.21

'''

from unittest import TestCase, main
from pathlib import Path
import sys
import os
sys.path.append((os.path.dirname(__file__)))
from Family import Family
from InputLoad import InputLoad

class TestMember(TestCase):

    path = Path(__file__)   
    family = InputLoad().load_members(str(path.parents[1])+'\\input1.txt')    
    
    def test_mother(self):
        original_member = "Amba"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("", member_obj.get_mother_name())
        
        original_member = "Chit"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("Queen_Anga", member_obj.get_mother_name())
        
        original_member = "Lavnya"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("Jnki", member_obj.get_mother_name())
        
        original_member = "Vasa"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("Satvy", member_obj.get_mother_name())
        
        
    def test_gender(self):
        original_member = "Amba"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("Female", member_obj.get_gender())
        
        original_member = "Laki"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("Male", member_obj.get_gender())
        
        original_member = "Vyas"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("Male", member_obj.get_gender())
        
        original_member = "Vyan"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("Male", member_obj.get_gender())
        
    def test_spouse(self):
        original_member = "Ish"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("", member_obj.get_spouse_name())
        
        original_member = "Vila"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("", member_obj.get_spouse_name())
        
        original_member = "Satvy"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("Asva", member_obj.get_spouse_name())
        
        original_member = "Jaya"
        member_obj = Family.get_object(self.family,original_member)
        self.assertEqual("Dritha", member_obj.get_spouse_name())
        
    def test_children_name(self):
        original_member = "Arit"
        member_obj = Family.get_object(self.family,original_member)
        self.assertListEqual(["Laki","Lavnya"], member_obj.get_children_name())
        
        original_member = "Vyan"
        member_obj = Family.get_object(self.family,original_member)
        self.assertListEqual(['Asva','Vyas','Atya'], member_obj.get_children_name())
        
        original_member = "Satya"
        member_obj = Family.get_object(self.family,original_member)
        self.assertListEqual(['Asva','Vyas','Atya'], member_obj.get_children_name())
        
        original_member = "Chika"
        member_obj = Family.get_object(self.family,original_member)
        self.assertListEqual([], member_obj.get_children_name())
        
if __name__ == "__main__":
    main()