/*
程序内容：用户输入一年内看过的电影，\
	储存电影的各种信息：片名、导演、评级等
版本： 20180427_0.1.0  wangwg
*/

#include <stdio.h>
#include <string.h>

#define TSIZE 45 /* 存储片名的数组大小 */
#define FMAX 5 /* 影片的最大数量 */


struct film {
	char title[TSIZE];
	int rating;
};

char * s_gets(char str[], int lim);

int main(void)
{
	struct film movies[FMAX];
	int i = 0;
	int j;

	puts("Enter first movie title:");
	while(i < FMAX && s_gets(movies[i].title, TSIZE) != NULL &&
		movies[i].title[0] != '\0')
	{
		puts("Enter your rating:");
		scanf("%d", &movies[i++].rating); //等同于 scanf("%d", &movies[i].rating); i++;
		while(getchar() != '\n')
			continue;
		puts("Enter next movie title (empty line to stop):");
	}

	if (i == 0)
	{
		printf("No data entered.\n");
	}
	else
	{
		printf("Here is the movie list:\n");
	}

	for (int j = 0; j < i; j++)
		printf("Movie: %s Rating: %d \n", movies[j].title, movies[j].rating);
	printf("Bye");

	return 0;
}

char * s_gets(char *st, int n)
{
	/*
	1.从终端输入值，存储值ret_val中，将'\n'替换成'\0'
	2.若是空行，则继续输入
	*/
	char * ret_val;
	char * find;

	ret_val = fgets(st, n, stdin);
	if(ret_val)
	{
		find = strchr(st, '\n');
		if(find)
			*find = '\0';
		else
			while (getchar() != '\n')
				continue;
	}

	return ret_val;
}