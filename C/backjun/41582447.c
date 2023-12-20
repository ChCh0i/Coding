#include <stdio.h>
int main() {
	int a, b = 0;
	int str[1000] = {};
	for (int i = 0; i < 10; i++) {
		scanf("%d", &a);
		str[i] = a % 42;
	}
	int count=0;
	int result = 0;
	for (int i = 0; i < 10; i++) {
		count = 0;
		for (int j = i + 1; j < 10; j++) {
			if (str[i] == str[j]) count++;
		}
		if (count == 0)result++;
	}
	printf("%d", result);
}
