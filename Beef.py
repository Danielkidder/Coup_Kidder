#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 16:18:37 2022

@author: danielkidder
"""

import random
card_abilities = {
    'duke':         ['tax','block_foreign_aid'],
    'captain':      ['steal','block_steal'],
    'contessa':     ['block_assassinate'],
    'ambassador':   ['exchange','block_steal'],
    'assassin':     ['assassinate']
            }
class Player_Beef:
    def __init__ (self, name='Beef'):
        self.name= name
        self.log=''
        self.coins= 0
        self.cards=[]
        
        
    def react(self, hint):
        if hint== 'turn':
            victim= self.find_active_target()
            log_lines=self.log.split('/n')
            last_line=log_lines[-2]
            if last_line== '':
                return 'tax'
            elif hint == 'turn':
                if self.coins>=7:
                    if card in self.cards!='assassin':
                        return 'coup'+victim
            elif hint in ['discard','placeback']:
                for card in self.cards:
                    if card!= 'duke':
                     return card
                    elif (card != 'captain'):
                        return card
                    elif (card!= 'assassin'):
                        return card
                    elif (card!= 'contessa'):
                        return card
                     
            
            elif hint== 'turn':
                for card in self.cards:
                    if card == 'duke':
                     return 'tax'
            elif hint == 'turn':
                for card in self.cards:
                    if card == 'ambassador':
                        return 'exchange'
            elif hint=='turn':
                for card in self.cards:
                    if card == 'assassin':
                        if self.coins>=3:
                            return 'assassinate'+victim
            elif hint == 'turn':
                return 'income'
            elif hint == 'challenged':
                log_lines= self.log.split('/n')
                last_lines=log_lines[-3]
                action=last_line.split()[1]
                for card in self.cards:
                    if action in card_abilities[card]:
                        return card
                    if card!= 'duke':
                     return card
                    elif (card != 'captain'):
                        return card
                    elif (card!= 'assassin'):
                        return card
                    elif (card!= 'contessa'):
                        return card
                    
            elif hint ==
                    
                
                    
                
                
                
                    
                
                
            
            
        