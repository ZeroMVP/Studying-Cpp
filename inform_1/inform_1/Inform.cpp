#include "InformHeadere.h"


int main(void) {
	double x = 0;
	double delta = 0;
	double step = 0;
	double last = 0 ;
	cin >> x >> step >> last >> delta;
	//cout << one(x,delta) << '\n';
	//stroke(x, delta);
    table(x, step, last, delta);
	cout << '\n';
	cout << log(x);
	cin >> x;
}





