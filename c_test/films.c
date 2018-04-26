/*
程序内容：用户输入一年内看过的电影，\
	储存电影的各种信息：片名、导演、评级等
版本： 20180427_0.1.0  wangwg
	  20180427_0.1.1  wangwg
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define TSIZE 45 /* 存储片名的数组大小 */

struct film {
	char title[TSIZE];
	int rating;
	struct film *next;
};

char * s_gets(char str[], int lim);

int main(void)
{
	struct film *head = NULL;
	struct film *current;
	struct film *prev;
	char input[TSIZE];

	puts("Enter first movie title:");
	while(s_gets(input, TSIZE) != NULL && input[0] != '\0')
	{
		current = (struct film *) malloc(sizeof(struct film));

		if (head == NULL)
			head = current;
		else
			prev->next = current;
		current->next = NULL;
		strcpy(current->title, input);

		puts("Enter your rating:");
		scanf("%d", &current->rating); //等同于 scanf("%d", &movies[i].rating); i++;
		while(getchar() != '\n')
			continue;
		puts("Enter next movie title (empty line to stop):");
		prev = current;
	}

	if (head == NULL)
		printf("No data entered.\n");
	else
		printf("Here is the movie list:\n");
	current = head;
	while(current != NULL)
	{
		printf("Movie: %s Rating: %d \n", current->title, current->rating);
		current = current->next;
	}

	//从头开始，释放已分配的内存
	current = head;
	while(current != NULL)
	{
		free(current);
		current = current->next;
	}
	printf("Bye.\n");

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
				continue;    //处理空行
	}

	return ret_val;
}