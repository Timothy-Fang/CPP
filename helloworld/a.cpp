#include <iostream>
#include <stdio.h>

using namespace std;

class A
{
public:
	int i;
	void f();

};
struct B
{
	int i;
};

void A::f()
{
	cout << i << endl;
	i= 20;
	cout << i << endl;
	printf("A::F()--&i=%p\n",&i);
}
void f(struct B* p)
{
	p->i = 20;
	cout << p->i << endl;
}
int main()
{
	A a;
	A aa;
	B b;
	a.i = 10;
	cout <<a.i;
	printf("a=%p\n",&a);
    printf("a.i=%p\n",&(a.i));
	a.f();
	cout <<a.i;
	aa.i= 100;
	aa.f();
	f(&b);
}