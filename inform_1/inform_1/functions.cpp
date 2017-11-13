#include "InformHeadere.h"
//#include <stdio.h>
//include <iostream>
//#include <math.h>
//#include "functions.cpp"
//using namespace std;

double xresult(double x, int n) {
	int m = 2 * n + 1;
	return (pow((x - 1), m) / (m*(pow((x + 1), m))));
}

double lnresult(double x, int max) {
	double q = 0;
	for (int n = 0; n < max; n++) {
		q += (xresult(x, n));
	}
	return 2 * q;
}

/*double one(double x, double delta, int *i) {
	*i = 1;
	while (abs( log(x) - lnresult(x, *i)) > delta) {
		(*i)++;
	}
	return lnresult(x, *i);
}*/

/*void stroke(double x, double delta) {
	int k = 5;
	int *i = &k;
	cout << x << " " << log(x) << " " << one(x, delta,i) << " " << k << '\n' ;
}*/

double one(double x, double delta) {
	int i = 1;
	while (abs(log(x) - lnresult(x, i)) > delta) {
		i++;
	}
	return lnresult(x, i);
}

void stroke(double x, double delta) {
	cout << x << " " << log(x) << " " << one(x, delta) << '\n';
}

void table(double x, double step, double last, double delta) {
	for (x; x < last; x += step)
		stroke(x, delta);
	stroke(last, delta);
}
