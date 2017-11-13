#pragma once
#include <stdio.h>
#include <iostream>
#include <math.h>
#include <cstdlib>

using namespace std;

double lnresult(double x, int max);
double xresult(double x, int n);
double one(double x, double delta);
void stroke(double x, double delta);
void table(double x, double step, double last, double delta);