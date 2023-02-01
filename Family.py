# -*- coding: utf-8 -*-


'''
@author: Lahari Sengupta
Created on 05.02.21

'''



class Family:
    
    members = []
    
    def __init__(self,start_member):
        self._start_member = start_member
        self.members.append(self._start_member)
    
    #@staticmethod
    def add_child(self,mom,child):
        mom_obj = self.get_object(mom)
        if not bool(mom_obj):
            return 'PERSON_NOT_FOUND'
        else:
            return self._addition_child(mom_obj,child)
     
    def _addition_child(self,mom,child):
        if not (mom.get_gender() == 'Female'):
            return "CHILD_ADDITION_FAILED"
        elif not mom.get_is_married():
            return "CHILD_ADDITION_FAILED: NOT_MARRIED"
        else:
            self.members.append(child)
            if not mom.get_has_this_child(child.get_name()):
                mom.set_has_child(child.get_name())
            husband_name = mom.get_spouse_name()
            husband_obj = self.get_object(husband_name)
            if not husband_obj.get_has_this_child(child.get_name()):
               husband_obj.set_has_child(child.get_name())
            return "CHILD_ADDITION_SUCCEEDED"
        
    def add_spouse(self,member,spouse):
        member_obj = self.get_object(member)
        self.members.append(spouse)
        member_obj.set_is_married(spouse.get_name())
        return 0
        
    # @staticmethod
    def get_daughter(self,parent):
        if not bool(parent):
            return 'PERSON_NOT_FOUND'
        elif parent.get_has_child():
            return ' '.join(self._get_children(parent,'Female'))
        else:
            return 'NONE'
    
    # @staticmethod
    def get_son(self,parent):
        if not bool(parent):
            return 'PERSON_NOT_FOUND'
        elif parent.get_has_child():
            return ' '.join(self._get_children(parent,'Male'))
        else:
            return 'NONE'
    
    def _get_children(self,parent,gender):
        children=[]
        for child in parent.get_children_name():
            if self.get_object(child).get_gender() == gender:
                children.append(child)
        if len(children)<1:
            children = ['NONE']
        return children
    
    # @staticmethod
    def get_direct_sibling(self,target_obj):
        if not bool(target_obj):
            return 'PERSON_NOT_FOUND'
        else:
            siblings=[]
            siblings = self._get_sibling(target_obj)
            return self._get_formatted_string(siblings)
    
    # @staticmethod
    def get_brother_in_law(self,member_obj):
        if not bool(member_obj):
            return 'PERSON_NOT_FOUND'
        
        brother_in_law = []
        
        #spouse's brothers
        spouse_obj = self.get_object(member_obj.get_spouse_name())
        if bool(spouse_obj):
            brother_in_law.extend(self._get_spouse_siblings(spouse_obj,'Male'))
        
        #husbands of siblings
        brother_in_law.extend(self._get_siblings_spouses(member_obj,'Female'))
                    
        return self._get_formatted_string(brother_in_law)
    
    # @staticmethod
    def get_sister_in_law(self,member_obj):
        if not bool(member_obj):
            return 'PERSON_NOT_FOUND'
        
        sister_in_law = []
                
        #spouse's sisters
        spouse_obj = self.get_object(member_obj.get_spouse_name())
        if bool(spouse_obj):
            sister_in_law.extend(self._get_spouse_siblings(spouse_obj,'Female'))
        
        #wives of siblings
        sister_in_law.extend(self._get_siblings_spouses(member_obj,'Male'))
                    
        return self._get_formatted_string(sister_in_law)
    
    # @staticmethod
    def get_maternal_uncle(self,member_obj):
        if not bool(member_obj):
            return 'PERSON_NOT_FOUND'
        mom_sibling = self._get_parent_sibling('Mom',member_obj)
        maternal_uncle = []
        for each in mom_sibling:
            if self.get_object(each).get_gender() == 'Male':
                maternal_uncle.append(each)
        return self._get_formatted_string(maternal_uncle)
     
        
    # @staticmethod
    def get_paternal_uncle(self,member_obj):
        if not bool(member_obj):
            return 'PERSON_NOT_FOUND'
        dad_sibling = self._get_parent_sibling('Dad',member_obj)
        paternal_uncle = []
        for each in dad_sibling:
            if self.get_object(each).get_gender() == 'Male':
                paternal_uncle.append(each)
        return self._get_formatted_string(paternal_uncle)
        
    
    # @staticmethod
    def get_maternal_aunt(self,member_obj):
        if not bool(member_obj):
            return 'PERSON_NOT_FOUND'
        mom_sibling = self._get_parent_sibling('Mom',member_obj)
        maternal_aunt = []
        for each in mom_sibling:
            if self.get_object(each).get_gender() == 'Female':
                maternal_aunt.append(each)
        return self._get_formatted_string(maternal_aunt)
    
    # @staticmethod
    def get_paternal_aunt(self,member_obj):
        if not bool(member_obj):
            return 'PERSON_NOT_FOUND'
        dad_sibling = self._get_parent_sibling('Dad',member_obj)
        paternal_aunt = []
        for each in dad_sibling:
            if self.get_object(each).get_gender() == 'Female':
                paternal_aunt.append(each)      
        return self._get_formatted_string(paternal_aunt)
    
    def _get_parent_sibling(self,parent_type,target):
        if parent_type == 'Mom':
            parent_obj = self.get_object(target.get_mother_name())
        else:
            mom_obj = self.get_object(target.get_mother_name())
            if bool(mom_obj):
                parent_obj = self.get_object(mom_obj.get_spouse_name())
            else:
                parent_obj = False
        if bool(parent_obj):
            return self._get_sibling(parent_obj)
        else:
            return []
    
    def _get_spouse_siblings(self,spouse,gender):
        siblings = []
        for sibling in self._get_sibling(spouse):
            if self.get_object(sibling).get_gender() == gender:
                siblings.append(sibling)
        return siblings
     
    def _get_siblings_spouses(self,member,gender):
        spouses = []
        for sibling in self._get_sibling(member):
            sibling_obj = self.get_object(sibling)
            if sibling_obj.get_spouse_name() and sibling_obj.get_gender() == gender:
                spouses.append(sibling_obj.get_spouse_name())
        return spouses
    
    # @staticmethod
    def _get_sibling(self,target):
        mom_obj = self.get_object(target.get_mother_name())
        if bool(mom_obj):
            return self._sibling_list(mom_obj,target)
        return []
    
    def _sibling_list(self,mom,target):
        all_children = mom.get_children_name()
        sibling = []
        for child in all_children:
            if not child == target.get_name():
                sibling.append(child)
        return sibling
    
    def _get_formatted_string(self,list_to_string):
        if len(list_to_string)<1:
            return 'NONE'
        else:
            return ' '.join(list_to_string)
    
    #@staticmethod
    def get_object(self,name):
        for member in self.members:
            if member.get_name() == name:
                return member
        return False