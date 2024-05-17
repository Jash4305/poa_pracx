#include <stdlib.h>
#include <stdio.h>

typedef struct Process {int size, id, blockId;}Process;
typedef struct Block {int id, capacity, interFrag;}Block;

int findBestBlockId(Process p, Block * b, int numBlock) {
    int bestBlockId = -1;
    int minDiff = INT_MAX;
    int diff = 0;
    for(int i = 0; i < numBlock; i++) {
        if(p.size <= b[i].capacity && p.size <= b[i].interFrag) {
            diff = b[i].interFrag - p.size;
            if(diff < minDiff) {
                minDiff = diff;
                bestBlockId = b[i].id;
            }
        }
    }
    return bestBlockId;
}

void bestFit(Process * p, Block * b, int numProcess, int numBlock) {
    for(int i = 0; i < numProcess; i++) {
        if(p[i].blockId == -1) {
            int bestBlockId = findBestBlockId(p[i], b, numBlock);
            p[i].blockId = bestBlockId;
            b[bestBlockId - 1].interFrag -= p[i].size;
        }
    }
    printf("Process Id\tProcess Size\tAllocated Block\n");
    for(int i = 0; i < numProcess; i++) {
        printf("%8d\t%8d\t", p[i].id, p[i].size);
        if(p[i].blockId == -1)
            printf("Not Allocated\n");
        else
            printf("%8d\n", p[i].blockId);
    }
}

int main() {
    int numProcess, numBlocks;
    
    printf("Enter number of process : ");
    scanf("%d", &numProcess);
    printf("Enter number of memory blocks : ");
    scanf("%d", &numBlocks);

    Process p[numProcess];
    Block b[numBlocks];

    for(int i = 0; i < numProcess; i++) {
        printf("Enter the Process %d Size : ", i + 1);
        scanf("%d", &p[i].size);
        p[i].blockId = -1;
        p[i].id = i+1; 
    }
    printf("\n");

    for(int i = 0; i < numBlocks; i++) {
        printf("Enter the Block %d Size : ", i + 1);
        scanf("%d", &b[i].capacity);
        b[i].interFrag = b[i].capacity;
        b[i].id = i+1;
    }
    printf("\n");

    bestFit(p, b, numProcess, numBlocks);

    return 0;
}