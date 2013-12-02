#include <stdio.h>

// reverse number
int 
rev(int n)
{
	int v = 0;
	while( n > 0 ){
		v = 10 * v + n % 10;
		n /= 10;
	}
	return v;
}

// check every digit is Odd
int 
isOddDigit(int n)
{
	int r;
	while (n != 0) {
		r = n % 10;
		if (!( r & 0x1))// is this digit is even, directly return
			return 0;
		n /= 10;
	}
	return 1;
}

int
main()
{
	int i;
	int cnt = 0;
	int thresh = 1000 * 1000 * 1000;
	for (i=0; i< thresh; i++) {
		if (i % 10 == 0)// skip leading zero in reverse number
			continue;
		cnt += isOddDigit(i + rev(i));
	}
	printf("%d\n",cnt);
	return 0;
}
