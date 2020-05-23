#include<stdio.h>
/**
	x^y mod m  的c程序
	@author:陈海龙
*/
int cal(int x, int y, int m) {
	int s = x;
	int i = 1;
	while (i != y) {
		x = x * s;
		x %= m;
		i++;
	}
	return x;
}

int main(){
	int x, y, m;
	scanf_s("%d %d %d", &x, &y, &m);
	int ans = cal(x, y, m);
	printf("%d\n", ans);
	return 0;
}

