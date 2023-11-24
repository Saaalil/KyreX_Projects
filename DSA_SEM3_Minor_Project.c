#include <stdio.h>

#define N 9

void printGrid(int grid[N][N])
{
    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
            printf("%2d ", grid[row][col]);
        printf("\n");
    }
}

int isSafe(int grid[N][N], int row, int col, int num)
{

    for (int x = 0; x < N; x++)
        if (grid[row][x] == num || grid[x][col] == num)
            return 0;

    int startRow = row - row % 3, startCol = col - col % 3;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (grid[i + startRow][j + startCol] == num)
                return 0;

    return 1;
}

// backtracking code
int solveSudoku(int grid[N][N])
{
    int row, col;

    // to find empty cell
    int isEmpty = 1;
    for (row = 0; row < N; row++)
    {
        for (col = 0; col < N; col++)
        {
            if (grid[row][col] == 0)
            {
                isEmpty = 0;
                break;
            }
        }
        if (!isEmpty)
            break;
    }

    if (isEmpty)
        return 1;

    for (int num = 1; num <= 9; num++)
    {
        if (isSafe(grid, row, col, num))
        {

            grid[row][col] = num;

            if (solveSudoku(grid))
                return 1;

            grid[row][col] = 0;
        }
    }

    return 0;
}

int main()
{
    int grid[N][N] = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}};

    if (solveSudoku(grid))
    {
        printGrid(grid);
        printf("Project by: Salil Hiremath, Yash Pathak IoT-A\n");
    }
    else
    {
        printf("No solution exists.\n");
    }

    return 0;
}
