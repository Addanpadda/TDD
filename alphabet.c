#include <stdio.h>

void PrintAlphabet()
{
	for(int character_code = 65; character_code <= 90; character_code++)
	{
		printf("%c", character_code);
	}

	printf("\n");
}

int main()
{
	PrintAlphabet();

	return 0;
}
