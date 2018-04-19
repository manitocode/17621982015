#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 6

int main(int argc, char const *argv[])
{
	int i,j,temp;
	int count = 5; //当前未打入冷宫的嫔妃个数

	char kingName[50];
	int choice;
	int searchIndex = -1;//查找的下标
	char temp_name[20];
	char names[MAX][20] = {"MISS_A", "MISS_B", "MISS_C", "MISS_D", "MISS_E"};
	// 嫔妃的级别[数组]
	char levelNames[5][10] = {"贵人", "嫔妃", "贵妃", "皇贵妃", "皇后"};
	// levels 用来存放每位妃子的级别，每个数组元素对应每个妃子的当前级别
	// -1 用来预留第六位嫔妃的位置
	int levels[MAX] = {1, 2, 0, 0, 4, -1};
	// loves 对应每个妃子的好感度，初始为100
	int loves[MAX] = {100, 100, 100, 100, 100, -1};

	/*
	printf("-------------------------------\n");
	printf("测试代码：查看嫔妃的状态\n");
	printf("姓名\t级别\t好感度\n");
	for (int i = 0; i < count; i++)
	{
		printf("%s\t%s\t%d\n", names[i], levelNames[levels[i]], loves[i]);
	}
	printf("-------------------------------\n");*/

	printf("请输入姓名：\n");
	scanf("%s", kingName);
	printf("欢迎%s\n",kingName);
	printf("1.皇帝下旨选妃：\t（增加功能）\n");
	printf("2.翻牌宠幸：\t\t（修改状态功能）\n");
	printf("3.打入冷宫：\t\t (删除功能)\n");
	printf("4.单独召见爱妃\n");
	printf("请陛下宠幸：\n");

	scanf("%d", &choice);
	switch(choice)
	{
		case 1://皇帝下旨选妃：\t（增加功能）
			//增加前须判断数组有没有空间
			//增加names\levels\loves数组元素
			printf("%d\n", count);
			if (count < MAX) //当前妃子数小于最大值-1
			{
				//执行添加
				printf("请输入妃子的名讳：\n");
				scanf("%s", names[count]);
				//将第count个元素的状态初始化
				levels[count] = 0;
				loves[count] = 100;
				count++;//添加完元素后，记得增加计数器
			}
			else
			{
				printf("后宫人满为患了～\n添加失败\n");
			}
			break;
		case 2://翻牌宠幸：\t\t（修改状态功能）
			//1.找到要宠幸妃子的下标
			//2.修改这个妃子的状态 好感度+10，级别升1级，如果最高级则不再升级
			//3.修改其她妃子状态 由于羡慕嫉妒恨，好感度-10
			//未支持姓名不存在的情况，先加一循环判断是否存在于names中
			printf("翻牌宠幸某位妃子的名字:\n");
			scanf("%s", temp_name);

			for (int i = 0; i < count; i++)
			{
				if(strcmp(temp_name, names[i]) == 0)
				{
					loves[i] += 10;
					levels[i] = levels[i] >= 4 ? 4 : levels[i] + 1;
				}
				else
				{
					loves[i] -= 10;
				}
			}
			break;
		case 3://printf("3.打入冷宫：\t\t (删除功能)\n");
			//1.查找
			//2.后面一个赋给前一个
			//3.总数 --;
			//修改其她妃子的状态，好感度+20
			printf("打入冷宫的妃子姓名:\n");
			scanf("%s", temp_name);
			//
			for (int i = 0; i < count; i++)
			{
				if (strcmp(temp_name, names[i]) == 0)
				{
					searchIndex = i;
					break;
				}
			}

			if (-1 == searchIndex)
			{
				printf("没有人打入冷宫\n");
			}
			else
			{
				for (int i = searchIndex; i < count-1; i++)
				{
					//names[i] = names[i+1]; 因为是字符数组，C语言中不支持数组的直接赋值
					strcpy(names[i], names[i+1]);
					loves[i] = loves[i+1];
					levels[i] = levels[i+1];
				}
				count --;
				for (int i = 0; i < count; i++)
				{
					loves[i] += 20;
				}
			}
			break;
		case 4://printf("4.单独召见爱妃\n");
			//1.查找
			//2.增加好感度即可
			//3.可以使用数组设计诗歌，使用随机数字的方式，表现皇帝的文采

			break;
		default:
			printf("输入有误！！\n");
			break;
	}
	//最后打印所有妃子状态前，按级别排序
	for (int i = 0; i < count-1; i++)
	{
		for (int j = 0; j < count-i-1; j++)
		{
			/* code */
			if(levels[j] < levels[j+1])
			{
				//需要交换names\levels\loves
				temp = levels[j];
				levels[j] = levels[j+1];
				levels[j+1] = temp;

				temp = loves[j];
				loves[j] = loves[j+1];
				loves[j+1] = temp;
				//注意字符串的交换
				strcpy(temp_name, names[j]);
				strcpy(names[j], names[j+1]);
				strcpy(names[j+1], temp_name);
			}
		}
	}

	printf("-------------------------------\n");
	printf("测试代码：查看嫔妃的状态\n");
	printf("姓名\t级别\t好感度\n");
	for (int i = 0; i < count; i++)
	{
		printf("%s\t%s\t%d\n", names[i], levelNames[levels[i]], loves[i]);
	}
	printf("-------------------------------\n");
	return 0;
}