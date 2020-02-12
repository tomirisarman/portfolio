#include <stdio.h>
#include <string.h>
struct dict{
	char word[50];
	int frequency;
};

void QuickSort(dict Text[],int low, int high);
int partition(dict Text[],int low, int high);
void MergeSort(dict Tex[],dict aux[],int low, int high);
void merge(dict Tex[],dict aux[],int low, int middle,int high);

int main(void){
	
	//saving words of the file into 2D-array
	FILE* inp;
    inp = fopen("text.txt","r");
    char arr[1000][50];
    int i = 0;
    int size;
    while(1){
        char r = (char)fgetc(inp);
        int k = 0;
        while(r!=' ' && r!=',' && r!='.' && r!='!' && r!='?' && r!='\n' && !feof(inp))
		{
			arr[i][k++] = r;
            r = (char)fgetc(inp);
        }
        
        arr[i][k]=0;  
        if(feof(inp))
		{
            break;
        }
        i++;
    }
    
    size=i;				//saving the size
    dict Text[size];	//creating a dict array of this size 
    
    //copying words from 2D-array to Text, initial frequency of each word is 1
    for (int n=0; n<size; n++){
		strcpy(Text[n].word, arr[n]);
		Text[n].frequency=1;
	}
	
	//changing all the letters to lowercase
	for (int i=0; i<size; i++)
	{
		int j=0;
		while (Text[i].word[j]!=0)
		{
			if (Text[i].word[j]>='A' && Text[i].word[j]<='Z') 
			Text[i].word[j] = ('a'+ Text[i].word[j] - 'A');
			j++;
		}
	}
    
    //deleting duplicates and modifying the frequency of each word
    for (int i=0; i<size; i++)
    {
    	for (int j=i+1; j<size; j++)
    	{
    		if ( strcmp(Text[i].word, Text[j].word)==0)
    		{
    			Text[i].frequency++;
    			for (int k=j; k<size; k++)
    			{
    				strcpy(Text[k].word, Text[k+1].word);
				}
				size--;
				j--;
			}
    		
		}
	}

	printf("\n\n---------------- QUICK SORT (alphabetical order) -----------------\n");
	
	QuickSort(Text,0, size-1);
	
    for (int i=1; i<size; i++)
	{
    	printf("\n\t%-30s %d", Text[i].word, Text[i].frequency);
	}
	
	dict aux[size];
    
    MergeSort(Text, aux, 0, size-1);
    printf("\n\n---------------- MERGE SORT (descending order of frequency) -----------------\n");
    for (int i=1; i<size; i++)
	{
    	printf("\n\t%-30s %d", Text[i].word, Text[i].frequency);
	}
	
	getchar();
	return 0;
	
}


void QuickSort(dict Text[], int low, int high)
{
	if(high<=low) return;
	int j=partition(Text, low, high);
	QuickSort(Text, low, j-1);
	QuickSort(Text, j+1, high);
}


int partition(dict Text[],int low, int high)
{
	int i=low,j=high+1;
	dict dummy;
	while (true)
	{
		while (Text[++i].word[0]<Text[low].word[0])
		{
			if (i==high) break;
		}
		
		while (Text[low].word[0]<Text[--j].word[0])
		{
			if (j==low) break;
		}
		
		if (i>=j) break;
		
		dummy=Text[i];
		Text[i]=Text[j];
		Text[j]=dummy;
	}

	dummy=Text[low];
	Text[low]=Text[j];
	Text[j]=dummy;
	return j;
}


void MergeSort(dict Text[],dict aux[],int low, int high)
{
	if(high<=low)
	{
		return;
	}
	int mid = low + (high-low)/2;
    MergeSort(Text, aux, low, mid); //left
    MergeSort(Text, aux, mid+1, high); // right
    merge(Text, aux, low, mid, high);

}


void merge(dict Text[],dict aux[],int low, int middle,int high)
{

	for (int k=low; k<=high; k++)
	{
		aux[k]=Text[k];
	}

	  int i=low, j=middle+1;
	  for (int k=low; k<=high; k++)
	  {
	  	if (i>middle)
		{
			Text[k]=aux[j++];
		}
	  	else if (j>high) 
		{
		  	Text[k]=aux[i++];
		}
	  	else if (aux[j].frequency>aux[i].frequency)
		{
		  	Text[k]=aux[j++];
		} 
	  	else
		{
		  	Text[k]=aux[i++];
		}
	  }

}








