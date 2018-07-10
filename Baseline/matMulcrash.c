#include <stdio.h>
#include <stdlib.h>

#define N 10000





int main(int argc, char* argv[]){

	const int n = atoi(argv[1]);

	float m1[N][N], m2[N][N];
	float res[N][N];

	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			m1[i][j] = (float)i+(float)j*(0.1);
			m2[i][j] = (float)i+(float)j*(0.2);
			// printf("%f ",m1[i][j]);
		}
		// printf("\n");
	}

	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			for(int k=0;k<n;k++){
				res[i][j] += m1[i][k] * m2[k][j];
			}
		}
	}


	return 0;
}