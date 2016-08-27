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
    zhuang_earn = 0
    zhuang_times = 0
    xian_earn = 0
    xian_times = 0
    ping_times = 0

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
            bet_index = random.randint(0,2)
            bet_arr = [-1,0,1]
            bet = bet_arr[bet_index]
            bet_money = random.randint(1000,1100)
        else:
            bet = int(input("请输入要压庄大还是小 -1 是小  1 是大"))              
            bet_money = int(input("请输入要压的钱"))

        self.bet = bet
        self.bet_money = bet_money
       	print "bet :%d (-1 是庄小  1 是庄大)" % self.bet
       	print "bet money:%d" % self.bet_money
        
    def whetherBet(self, zhuang_score, xian_score, xian_plus, player):
        if zhuang_score in [8,9] or xian_score in [8,9]:
            return False;
        if player == 'xian':
            if xian_score >= 6:
                return False
            else:
                return True
        else:
            if xian_plus != False :
                xian_plus_compute = xian_plus%10
            else:
                xian_plus_compute = False;
            if xian_score >=6 and zhuang_score in [0,1,2,3,4,5]:
                return True
            elif xian_score >=6 and zhuang_score not in [0,1,2,3,4,5]:
                return False
            elif zhuang_score == 3 and xian_plus_compute in [1,2,3,4,5,6,7,9,0]:
                return True
            elif zhuang_score == 4 and xian_plus_compute in [2,3,4,5,6,7]:
                return True
            elif zhuang_score == 5 and xian_plus_compute in [4,5,6,7]:
                return True
            elif zhuang_score == 6 and xian_plus_compute in [6,7]:
                return True
            elif zhuang_score >= 7:
                return False
            else: 
                return False
    def playGame(self):
        times = 0;
        zhuang = []
        xian = []
        while (len(self.poker_cards) >=4):
            times = times+1
            zhuang = []
            xian = []
            xian_plus = False 
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
            xian_ori = xian_score
            zhuang_ori = zhuang_score
            is_valid = 1

            if(self.whetherBet(zhuang_ori, xian_ori, False, 'xian') and len(self.poker_cards) >0):
                xian_plus = self.poker_cards[0]
                xian.append(self.poker_cards[0])
                del self.poker_cards[0]
                xian_score = self.compute(xian)    
       	        print "贤补牌后"
                print xian
                print "贤的补牌后得分%d" % xian_score
            elif (self.whetherBet(zhuang_ori, xian_ori, False, 'xian') and len(self.poker_cards) ==0):
                is_valid = 0
            elif(self.whetherBet(zhuang_ori, xian_ori, xian_plus, 'zhuang') and len(self.poker_cards) ==0):
                is_valid = 0
            elif(self.whetherBet(zhuang_ori, xian_ori, xian_plus, 'zhuang')):
                zhuang.append(self.poker_cards[0])
                del self.poker_cards[0]
                zhuang_score = self.compute(zhuang)
       	        print "庄补牌后"
                print zhuang
                print "庄的补牌后得分%d" % zhuang_score
            if(is_valid == 1):
            	if (zhuang_score > xian_score) :
                    self.zhuang_times = self.zhuang_times+1
                    self.zhuang_earn = self.zhuang_earn + self.bet*self.bet_money
                    self.money = self.money + self.bet*self.bet_money
            	elif (zhuang_score < xian_score):
                    self.xian_times= self.xian_times+1
                    self.xian_earn= self.xian_earn + self.bet*self.bet_money
                    self.money = self.money - self.bet*self.bet_money
                else:
                    self.ping_times = self.ping_times + 1;
            	print "money:%d" % self.money
            else:
                print "最后一局没有成功"
            #time.sleep(1)
        print "final money:%d" % self.money    	
        print "final zhuangtimes:%d" % self.zhuang_times   	
        print "final zhuangmoney:%d" % self.zhuang_earn
        print "final xiantimes:%d" % self.xian_times   	
        print "final xianmoney:%d" % self.xian_earn
        print "final pingtimes:%d" % self.ping_times
 
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

'''
baccarat = Baccarat(8,0);
print "baccarat.whetherBet(3,0,7,'zhuang')"
print baccarat.whetherBet(3,0,7,'zhuang')

print "baccarat.whetherBet(3,0,8,'zhuang')"
print baccarat.whetherBet(3,0,8,'zhuang')
print "baccarat.whetherBet(4,0,3,'zhuang')"
print baccarat.whetherBet(4,0,3,'zhuang')
print "baccarat.whetherBet(4,0,8,'zhuang')"
print baccarat.whetherBet(4,0,8,'zhuang')
print "baccarat.whetherBet(5,0,6,'zhuang')"
print baccarat.whetherBet(5,0,6,'zhuang')
print "baccarat.whetherBet(5,0,8,'zhuang')"
print baccarat.whetherBet(5,0,8,'zhuang')
print "baccarat.whetherBet(6,0,6,'zhuang')"
print baccarat.whetherBet(6,0,6,'zhuang')
print "baccarat.whetherBet(6,0,8,'zhuang')"
print baccarat.whetherBet(6,0,8,'zhuang')
print "baccarat.whetherBet(7,0,2,'zhuang')"
print baccarat.whetherBet(7,0,2,'zhuang')
print "baccarat.whetherBet(8,0,2,'zhuang')"
print baccarat.whetherBet(8,0,2,'zhuang')
print "baccarat.whetherBet(3,9,7,'zhuang')"
print baccarat.whetherBet(3,9,7,'zhuang')
print "baccarat.whetherBet(3,7,7,'zhuang')"
print baccarat.whetherBet(3,7,7,'zhuang')
print "baccarat.whetherBet(6,7,7,'zhuang')"
print baccarat.whetherBet(6,7,False,'zhuang')
'''
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

        	





