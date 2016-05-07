#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py
# author bitzhuxb@sina.com
# date : 20160507
import random
import time 
from random import randint

class Baccarat:
    '百家乐的类'
    poker_cards = []
    poker_num = 0
    money = 0
    bet_type = 0
    bet = 0
    bet_money = 0
    def __init__(self, poker_num,bet_type):
        '定义当前总共多少副牌'	
        self.poker_num = poker_num
        self.bet_type = bet_type
        print '初始化牌'
        self.poker_cards = range(1,14)
        #self.poker_cards = self.poker_cards.extend([0,0,0,0])
        self.poker_cards = self.poker_cards * self.poker_num * 4
        self.shuffleCards()
    def shuffleCards(self):
        random.shuffle(self.poker_cards)
    def betGame(self):
    	#押注
        bet = 0
        bet_money = 0
        if self.bet_type == 0:
            bet_index = random.randint(0,1)
            bet_arr = [-1,1]
            bet = bet_arr[bet_index]
            bet_money = random.randint(1000,1100)
        else:
            bet = int(input("请输入要压庄大还是小 -1 是小  1 是大"))              
            bet_money = int(input("请输入要压的钱"))

        self.bet = bet
        self.bet_money = bet_money
       	print "bet :%d (-1 是庄小  1 是庄大)" % self.bet
       	print "bet money:%d" % self.bet_money
        

    def playGame(self):
        times = 0;
        zhuang = []
        xian = []
        while (len(self.poker_cards) >=4):
            times = times+1
            zhuang = []
            xian = []
            print
            print
            print "第%d局" % times
            print "剩下牌%d张" % len(self.poker_cards)
            self.betGame()
            zhuang.append(self.poker_cards[0])
            zhuang.append(self.poker_cards[2])
            xian.append(self.poker_cards[1])
            xian.append(self.poker_cards[3])
       	    print "庄牌"
            print zhuang
            print "贤牌"
            print xian
        
            del self.poker_cards[0]
            del self.poker_cards[0]
            del self.poker_cards[0]
            del self.poker_cards[0]
            zhuang_score = self.compute(zhuang)
            xian_score = self.compute(xian)
            print "庄的第一次得分%d" % zhuang_score
            print "贤的第一次得分%d" % xian_score
            while(zhuang_score< 6 and len(self.poker_cards) >0):
                zhuang.append(self.poker_cards[0])
                del self.poker_cards[0]
                zhuang_score = self.compute(zhuang)
       	        print "庄补牌后"
                print zhuang
                print "庄的补牌后得分%d" % zhuang_score
            while(xian_score< 6 and len(self.poker_cards) >0):
                xian.append(self.poker_cards[0])
                del self.poker_cards[0]
                xian_score = self.compute(xian)    
       	        print "贤补牌后"
                print xian
                print "贤的补牌后得分%d" % xian_score
            if(zhuang_score >= 6 and xian_score >=6):
            	if (zhuang_score > xian_score) :
            		self.money = self.money + self.bet*self.bet_money
            	else:
            		self.money = self.money - self.bet*self.bet_money
            	print "money:%d" % self.money
            else:
                print "最后一局没有成功"
            #time.sleep(1)
        print "final money:%d" % self.money    	
    def compute(self,cards):
        ans = 0
        for card in cards:
            if card < 10:
                ans = ans+card;
        ans = ans%10
        return ans 



bet_type = int(input("请输入要压庄大还是小 0是程序自动压钱玩（1000-1100）  1 是自己压"))
num = int(input("请输入几副扑克"))
baccarat = Baccarat(num,bet_type)
baccarat.playGame()


#模拟系统1000次自己玩
'''
cur = 0
money = 0
while cur<1000:
    baccarat = Baccarat(8,0)
    baccarat.playGame()
    money = money + baccarat.money  
    cur = cur+1
print money
'''    	

        	





