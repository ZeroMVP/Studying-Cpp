#include <iostream>
using namespace std;



void swap(int * a, int * b) {
	int t = *a;
	*a  =  *b;
	*b = t;
}

void rotate(int a[], unsigned size, int shift) {
	for(int m = 0; m<shift;m++)
	for(unsigned i=0;i < size-1;i++)
	{
		int y = i + 1;
		int t = a[i];
		a[i] = a[y];
		a[y] = t;
		
	};

}

int main()
{
	
	int k = 10, m = 20;
	int a[8] = {1,2,3,4,5,6,7,8};
	rotate(a, 8, 3);
	cout << a[0] << a[1] << a[2] << a[3] << a[4] << a[5] << a[6] << a[7];
	cin >> k;

	
}