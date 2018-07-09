#include <stdio.h>
#include <stdlib.h>


int main(int argc, char* argv[]){

	const int n = atoi(argv[1]);

	float m1[n][n], m2[n][n];

	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			m1[i][j] = (float)i+(float)j*(0.1);
			m2[i][j] = (float)i+(float)j*(0.2);
			// printf("%f ",m1[i][j]);
		}
		// printf("\n");
	}

	float res[n][n];
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			for(int k=0;k<n;k++){
				res[i][j] += m1[i][k] * m2[k][j];
			}
		}
	}


	return 0;
}