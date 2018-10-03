#include<stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 10000




float m1[N][N], m2[N][N];
float res[N][N];


void baseMult(int l1, int l2, int l3, int n){
	for(int i=l1;i<l1+n;i++){
		for(int j=l2;j<l2+n;j++){
			for(int k=l3;k<l3+n;k++){
				res[i][j] += m1[i][k] * m2[k][j];
			}
		}
	}
}

int main(int argc, char* argv[]){

	const int bs = atoi(argv[1]);
	int n =  1500;
	// int n = 8;

	clock_t initial,final;


	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			m1[i][j] = (float)i+(float)j*(0.1);
			m2[i][j] = (float)i+(float)j*(0.2);
			// printf("%f ",m1[i][j]);
		}
		// printf("\n");
	}


	initial = clock();
	
	for(int i=0;i<n;i+=bs){
		for(int j=0;j<n;j+=bs){
			for(int k=0;k<n;k+=bs){
				baseMult(i,j,k,bs);
			}
		}
	}
	final = clock() - initial;

	// for(int i=0;i<n;i++){	
// 	for(int j=0;j<n;j++){
	// 		printf("%f ",res[i][j]);
	// 	}
	// 	printf("\n");
	// }


    double time_taken = ((double)final)/CLOCKS_PER_SEC; 
    printf("%f\n", time_taken);

	return 0;
}