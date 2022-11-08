# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:33:31 2022

@author: etiguercha
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def readList(List):
    ListOfNodes = []
    for i in range(len(List)):       
        ListOfNodes.append(ListNode(List[i],None))
    for i in range(len(List)-1):
        ListOfNodes[i].next = ListOfNodes[i+1]
    return ListOfNodes[0]  
    
    
def mergeTwoLists(list1,list2):
    mergeList =ListNode(0,None)
    mergeListcopy = mergeList.copy()
    
    while list1.next != None and list2.next!=None:
    
        if list1.val>list2.val:
            mergeList.next = ListNode(list2.val,None)
            mergeList = mergeList.next
            list2=list2.next
            
        elif list1.val<list2.val:
            mergeList.next = ListNode(list1.val,None)
            mergeList = mergeList.next
            list1=list1.next
            
        elif list1.val==list2.val:
            mergeList.next =ListNode(list2.val,ListNode(list1.val,None))
            mergeList = mergeList.next.next
            list1=list1.next
            list2=list2.next
    return mergeListcopy.next
    

# def mergeTwoLists(list1,list2):
#     mergeList =[]
#     i=0
#     j=0
    
#     while i <len(list1) and j<len(list2):
    
#         if list1[i]>list2[j]:
#             mergeList.append(list2[j])
#             j+=1
#         elif list1[i]<list2[j]:
#             mergeList.append(list1[i])
#             i+=1
#         elif list1[i]==list2[j]:
#             mergeList.append(list1[i])
#             mergeList.append(list2[j])
#             i+=1
#             j+=1
        
#         if i ==len(list1):
#             mergeList+=list2[j:]
#         elif j == len(list2):
#             mergeList+=list1[i:]
            
            
    return mergeList

a =[1,3,4,5,8,10]
b =[1,2,3,5,6,7]