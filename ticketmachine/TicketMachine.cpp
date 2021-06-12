/*
 * TicketMachine.cpp
 *
 *  Created on: 2021年6月12日
 *      Author: timo
 */

#include "TicketMachine.h"
#include <iostream>
using namespace std;

//构造函数
TicketMachine::TicketMachine() : PRICE(0),balance(0),total(0){//初始化
    //TODO:
}
TicketMachine::~TicketMachine(){//析构函数

}

void TicketMachine::showPrompt()
{
    cout<<"something";
}

void TicketMachine::insertMoney(int money)
{
    balance +=money;
}

void TicketMachine::showBalance()
{
    cout<<balance;
}


