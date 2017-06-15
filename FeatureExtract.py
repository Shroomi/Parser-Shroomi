#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:51:47 2017

@author: mengruding
"""

class Feature:
    def __init__(self):
        self.b0_form = 'NULL'
        self.b0_pos = 'NULL'
        self.s0_form = 'NULL'
        self.s0_pos = 'NULL'
        self.b1_pos = 'NULL'
        self.s1_pos = 'NULL'
        self.s0_head_form = 'NULL'
        self.ld_s0_pos = 'NULL'
        self.rd_s0_rel = 'NULL'
        self.features = dict()
        self.feature_vector = []
    
    def get_feature(self, sentence, stack, buffer, arc_gold):
        if len(buffer) > 0:
            if buffer[0] != 0:
                self.b0_form = sentence.form[buffer[0] - 1]
                self.b0_pos = sentence.pos[buffer[0] - 1]
            else:
                self.b0_form = 'ROOTForm'
                self.b0_pos = 'ROOTPos'
        if len(stack) > 0:
            if stack[-1] != 0:
                self.s0_form = sentence.form[stack[-1] - 1]
                self.s0_pos = sentence.pos[stack[-1] - 1]
                self.s0_head_form = sentence.form[int(sentence.head[stack[-1] - 1]) - 1]
            else:
                self.s0_form = 'ROOTForm'
                self.s0_pos = 'ROOTPos'
            if stack[-1] in arc_gold:
                self.ld_s0_pos = sentence.pos[min(arc_gold[stack[-1]]) - 1]
                self.rd_s0_rel = sentence.rel[max(arc_gold[stack[-1]]) - 1]
        if len(buffer) > 1:
            if buffer[1] != 0:
                self.b1_pos = sentence.pos[buffer[1] - 1]
            else:
                self.b1_pos = 'ROOTPos'
        if len(stack) > 1:
            if stack[-2] != 0:
                self.s1_pos = sentence.pos[stack[-2] - 1]
            else:
                self.s1_pos = 'ROOTPos'
     
    def store_feature(self, count, feature):
        if 'b0_form=' + feature.b0_form not in self.features and feature.b0_form != 'NULL':
            self.features['b0_form=' + feature.b0_form] = count
            count += 1
        if 'b0_pos=' + feature.b0_pos not in self.features and feature.b0_pos != 'NULL':
            self.features['b0_pos=' + feature.b0_pos] = count
            count += 1
        if 's0_form=' + feature.s0_form not in self.features and feature.s0_form != 'NULL':
            self.features['s0_form=' + feature.s0_form] = count
            count += 1
        if 's0_pos=' + feature.s0_pos not in self.features and feature.s0_pos != 'NULL':
            self.features['s0_pos=' + feature.s0_pos] = count
            count += 1
        if 'b1_pos=' + feature.b1_pos not in self.features and feature.b1_pos != 'NULL':
            self.features['b1_pos=' + feature.b1_pos] = count
            count += 1
        if 's1_pos=' + feature.s1_pos not in self.features and feature.s1_pos != 'NULL':
            self.features['s1_pos=' + feature.s1_pos] = count
            count += 1
        if 's0_head_form=' + feature.s0_head_form not in self.features and feature.s0_head_form != 'NULL':
            self.features['s0_head_form=' + feature.s0_head_form] = count
            count += 1
        if 'ld_s0_pos=' + feature.ld_s0_pos not in self.features and feature.ld_s0_pos != 'NULL':
            self.features['ld_s0_pos=' + feature.ld_s0_pos] = count
            count += 1
        if 'rd_s0_rel=' + feature.rd_s0_rel not in self.features and feature.rd_s0_rel != 'NULL':
            self.features['rd_s0_rel=' + feature.rd_s0_rel] = count
            count += 1
        return count
    
    def get_feature_vector(self, features):
        if 'b0_form=' + self.b0_form in features:
            self.feature_vector.append(features['b0_form=' + self.b0_form])
        if 'b0_pos=' + self.b0_pos in features:
            self.feature_vector.append(features['b0_pos=' + self.b0_pos])
        if 's0_form=' + self.s0_form in features:
            self.feature_vector.append(features['s0_form=' + self.s0_form])
        if 's0_pos=' + self.s0_pos in features:
            self.feature_vector.append(features['s0_pos=' + self.s0_pos])
        if 'b1_pos=' + self.b1_pos in features:
            self.feature_vector.append(features['b1_pos=' + self.b1_pos])
        if 's1_pos=' + self.s1_pos in features:
            self.feature_vector.append(features['s1_pos=' + self.s1_pos])
        if 's0_head_form=' + self.s0_head_form in features:
            self.feature_vector.append(features['s0_head_form=' + self.s0_head_form])
        if 'ld_s0_pos=' + self.ld_s0_pos in features:
            self.feature_vector.append(features['ld_s0_pos=' + self.ld_s0_pos])
        if 'rd_s0_rel=' + self.rd_s0_rel in features:
            self.feature_vector.append(features['rd_s0_rel=' + self.rd_s0_rel])
        return self.feature_vector