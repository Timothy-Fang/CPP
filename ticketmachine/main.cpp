/*
 * main.cpp
 *
 *  Created on: 2021年6月12日
 *      Author: timo
 */
#include <iostream>
using namespace std;

#include "TicketMachine.h"
int main()
{
   TicketMachine tm;
   tm.insertMoney(100);
   tm.showBalance();
   return 0;
}




