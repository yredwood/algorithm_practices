#include<iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int min(int a, int b)
{
    if (a < b)
        return a;
    else
        return b;
}

void print(int arr[], int n)
{
    for (int i=0; i<n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int get_profit_from_block(int mblock[], int M, int C)
{
    int max_profit = 0;
    for (int m=1; m<M+1; m++)
    {
        vector<bool> v(M);
        fill(v.begin(), v.begin() + m, true);
        do
        {
            int comb[m];
            int _c = 0;
            for (int i=0; i<M; i++)
            {
                if (v[i])
                {
                    comb[_c++] = mblock[i];
                    // comb: (3,6,4) for mblock (1,3,6,4)
                }
            }
            int sum = 0;
            for (int i=0; i<m; i++)
                sum += comb[i];
            if (sum > C)
                continue;

            int profit = 0;
            for (int i=0; i<m; i++)
                profit += comb[i] * comb[i];
            if (profit > max_profit)
                max_profit = profit;

        } while (prev_permutation(v.begin(), v.end()));
    }
    return max_profit;
}

int main(int argc, char** argv)
{   
    int test_case;
    int T;
    freopen("sample_input.txt", "r", stdin);

    cin >> T;
    for (test_case = 1; test_case <= T; ++test_case)
    {
        // get inputs
        int N, M, C;
        cin >> N >> M >> C;
        int honey_map[N][N] = {0};

        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                cin >> honey_map[i][j];

        int max_profit = 0;
        
        // 1. different row 
        int line_max_profits[N] = {0};
        int profit = 0;
        for (int n = 0; n < N; n++)
        {
            for (int start_point = 0; start_point < N-M+1; start_point++)
            {
                int mblock[M];
                int _m = 0;
                for (int m=start_point; m<start_point+M; m++)
                {
                    mblock[_m++] = honey_map[n][m];
                }
                int p = get_profit_from_block(mblock, M, C);
                if (p > line_max_profits[n])
                    line_max_profits[n] = p;
            }
        }
        sort(line_max_profits, line_max_profits+N, greater<int>());
        profit = line_max_profits[0] + line_max_profits[1];


        cout << "#" << test_case << " " << profit << endl;

        
        
    }

    return 0;
}

