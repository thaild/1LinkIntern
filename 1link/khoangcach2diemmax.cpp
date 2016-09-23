#include<stdio.h>
#include<conio.h>
#include<math.h>

float x[100], y[100];
float do_dai(int i, int j){
	return sqrt(pow(x[i]-x[j],2)+pow(y[i]-y[j],2));
	
}

void nhap(int n){
	for(int i=1; i<=n; i++){
		printf(" Nhap toa do diem thu %d ",i); scanf("%f %f", &x[i], &y[i]);
	}
	printf("\n");
}

int main(){
	int n,i,j, imax, jmax;
	float d, dmax;
	printf("\n So diem n = : "); scanf("%d",&n);
	nhap(n);
	dmax = do_dai(1,2); imax=1; jmax = 2;
	for(i=1; i<n; i++){
		for(j = i+1; j<=n ; j++){
			d = do_dai(i,j);
			if(d>dmax){
				dmax = d;
				imax = i;
				jmax = j;
			}
		}
	}
	printf("\nDoan thang lon nhat co do dai bang: %0.2f", dmax);
	printf("\n Di qua 2 diem co chi so la %d va %d ", imax, jmax);
	getch();
}
