#include <iostream>
using namespace std;

int main()
{
	int k = 0;
	char c = '\0';
	while (cin.get(c)) {
		if (c != ' ') {
			cout << c;
			k = 1;
		}
		if (c == ' ')
			if (k == 1) {
				cout << ' ';
				k = 0;
			}
	}

	return 0;
}