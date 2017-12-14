// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <math.h>
#include <cstdlib>
#include <time.h>
#include <conio.h>
#include <cstring>
#include <stdlib.h>
#include <windows.h>


using namespace std;

#include <stdio.h>
#include <conio.h>
#include <math.h>

void main()
{

	setlocale(LC_ALL, "Russian");
	srand(time(NULL));

	float a[5][5] = {                             //����� ����� ����
		{ 0.945,-0.5882,0,0,0 },
		{ -0.017,0.9806,-0.0114,0,0 },
		{ 0,-0.0153,0.9876,-0.0107,0 },
		{ 0,0,-0.1111,0.9188,-0.5 },
		{ 0,0,0,-0.75,0.9378 },
	};
	float d[5] = { 50,-15.2371,-14.2308,0,-48 };    //������ ����� ����
	float x[5] = { 0 };                             //������ ����������� ��������
	float b[5][5] = { 0 };
	float g[5] = { 0 };
	float x1[5] = { 0 };
	int i, j;
	int k;
	int y = 0;
	float z;
	float xk[5] = { 0 };
	float e;                                  //�����������
	system("cls");
	k = 0;
	printf("�������� �������, ���������� ������ ������ ����:\n\n");
	for (i = 0; i<5; i++)
	{
		for (j = 0; j<5; j++)
			printf("%.4f   ", a[i][j]);
		printf("\n");
	}
	printf("\n������ ����� ����:\n\n");
	for (i = 0; i<5; i++)
		printf("%.4f  ", d[i]);
	printf("\n\n");
	printf("������� ��������� ����������� ���������� �����������:");

	cin >> e; //scanf("%f", &e);

	printf("\t%.5f\n\n", e);
	//�������������� ��������������
	for (j = 0; j<5; j++)
	{
		g[j] = d[j];
		x[j] = g[j];
		x1[j] = x[j];
		for (i = 0; i<5; i++)
		{
			if (i == j)   b[j][i] = 1 - a[j][i];
			else       b[j][i] = -a[j][i];
		}
	}
	printf("��������������� �������:\n\n");
	for (i = 0; i<5; i++)
	f
	{
		for (j = 0; j<5; j++)
			printf("%.4f   ", b[i][j]);
		printf("\n");
	}
	printf("\n");
	//����������� ������������� �������� (����� �������)
	do
	{
		y = 0;
		k = k + 1;
		printf("�������� ����� %d\t\n", k);
		for (j = 0; j<5; j++)
		{
			xk[j] = g[j];
			for (i = 0; i<5; i++)
			{
				xk[j] += b[j][i] * x1[i];
			}
			x1[j] = xk[j];
		}
		//�������� ������������ �������� ����������� �������� ��������
		for (j = 0; j<5; j++)
		{

			z = fabs(xk[j] - x[j]);
			printf("x[%d]: %.4f, xk[%d]: %.4f\n", j, x[j], j, xk[j]);
			printf("|x[%d]-xk[%d]|=%.4f", j, j, z);
			x[j] = xk[j];
			if (z<e)
			{
				y = y + 1;
			}
			printf("\n");
		}
		printf("\n");
	} while (y != 5);
	printf("����� ��������:\t");
	printf("%d\n\n", k);
	//Printing the result
	printf("���������, ��������� � ������������ %.5f:\n\n", e);
	for (i = 0; i<5; i++)
	{
		printf("%.4f   ", x[i]);
	}
	system("pause");
}