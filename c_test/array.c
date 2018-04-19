#include <stdio.h>
#include <stdlib.h>
#define n 5

int main()
{

	int array[] = {15, 25, 35, 45, 55};
	//实现数组逆序:首尾元素交换
	int temp,i;
	int *ptr_array_start = array;//首元素地址指针
	int *ptr_array_end = array + n - 1;//尾元素地址指针
	if(n % 2 != 0)
	{
		while(ptr_array_start != ptr_array_end)
		{
			//首尾交换，指针更新
			temp = *ptr_array_start;
			*ptr_array_start = *ptr_array_end;
			*ptr_array_end = temp;
			//首元素指针向后移动
			ptr_array_start++;
			//尾元素指针向前移动
			ptr_array_end--;
		}
	}
	else
	{
		while(ptr_array_start < ptr_array_end)
		{
			//首尾交换，指针更新
			temp = *ptr_array_start;
			*ptr_array_start = *ptr_array_end;
			*ptr_array_end = temp;
			//首元素指针向后移动
			ptr_array_start++;
			//尾元素指针向前移动
			ptr_array_end--;
		}
	}
	/*for (int i = 0; i < n/2; i++)
	{
		temp = array[i];
		array[i] = array[n-i-1];
		array[n-i-1] = temp;
	}*/

	for (int i = 0; i < n; ++i)
	{
		printf("\n%d\t", *(array + i));
	}

/*	
	int array[] = {15, 25, 35, 45, 55};
	int i;
	int *ptr_array = array;

	for (int i = 0; i < 5; i++)
	{
		//printf("第%d个元素的值是%d\t地址是：%p\n", i+1, ptr_array[i], &ptr_array[i]);
		//printf("第%d个元素的值是%d\t地址是：%p\n", i+1, *ptr_array, &ptr_array[i]);
		printf("第%d个元素的值是%d\t地址是：%p\n", i+1, *ptr_array, ptr_array);
		ptr_array++; //每次循环都会移动指针的指向，要注意重置
	}*/


	/* 
	删除的逻辑
	12 34 23 67 9
	12 34 67 9 9
	1.查找要删除数字的下标： 2
	2.从下表开始，后面一个覆盖前面一个数字
	3.数字的总长度-1
	/
	
	int count = 5;
	double powers[] = {43222, 45771, 40907, 41234, 40767};
	double delete_power; //用户要删除的战力值
	int delete_index = -1;
	int i;
	double insert_power;

	printf("please enter the delete_power:");
	scanf("%lf", &delete_power);
	for (int i = 0; i < count; i++)
	{
		if(delete_power == powers[i])
		{
			delete_index = i;
			break;
		}
	}

	if (-1 == delete_index)
	{
		printf("未找到值");
	}
	else
	{
		for (int i = delete_index; i < count - 1; i++)
		{
			powers[i] = powers[i+1];
		}
		count--;
	}
	printf("%d\n", count);
	printf("delete answer is :\n");
	for(i = 0;i<count;i++)
	{
		printf("%.2lf\n", powers[i]);
	}

	printf("enter new power:\n");
	scanf("%lf",&insert_power);
	powers[count] = insert_power;
	count ++;
	printf("%d\n", count);
	printf("insert answer is :\n");
	for(i = 0;i<count;i++)
	{
		printf("%.2lf\n", powers[i]);
	}
	*/

	/*
	16 25 9 90 23
	降序排列 - 从大到小
	冒泡排序的基础原理：遍历和交换
	第一轮循环：某个数字小于后面的数字，那么就交换
		[25 16 9 90 23]
		[25 16 9 90 23]
		[25 16 90 9 23]
		[25 16 90 23 9] 最小的数字到最后
	1⃣️需要比较(n-1)轮
	2⃣️每一轮比较的次数比上一轮 -1 次
	（数组长度 - 1） - 当前轮数
	

int nums[n] = {16, 24, 9, 90, 23};
int i,j;
int temp; //临时变量
//外层循环控制轮数
for (int i = 0; i < n - 1; i++)
{
	//内层循环控制 每轮比较次数
	for (int j = 0; j < n - i - 1; j++)
	{
		//如果当前值小于后面一个值，则交换
		if(nums[j] < nums[j+1])
		{
			temp = nums[j];
			nums[j] = nums[j+1];
			nums[j+1] = temp;
		}
	}
}

printf("排序后的结果是：\n");
for (int i = 0; i < n; i++)
{
	printf("%d\t", nums[i]);
}*/

	/*
	逆序：
	12 3 44 23 2
	i 			N - i - 1
		i.  N - i - 1

	其中N为i < n/2
	*/

	return 0;
}