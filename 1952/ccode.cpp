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


int main(int argc, char** argv)
{   
    int test_case;
    int T;
    freopen("sample_input.txt", "r", stdin);

    cin >> T;
    for (test_case = 1; test_case <= T; ++test_case)
    {
        // get inputs
        int day, month, month3, year;
        int plans[12];
        cin >> day >> month >> month3 >> year;
        for (int _i = 0; _i < 12; _i++)
            cin >> plans[_i];
        
        int min_cost = 0;
        for (int _i3 = 0; _i3 < 5; _i3++)
        {
            if (_i3==0)
            {
                // no month3 case
                int yearly_cost = year;
                int monthly_cost = 0;
                for (int d = 0; d < 12; d++)
                {
                    monthly_cost += min(month, day*plans[d]);
                }
                min_cost = min(yearly_cost, monthly_cost);
            }
            else if (_i3==4)
            {
                int cost = 4 * month3;
                if (cost < min_cost)
                    min_cost = cost;
            }
            else
            {   
                // permutations over start points
                vector<bool> v(12);
                fill(v.begin(), v.begin() + _i3, true); // 12 C _i13
                do
                {   
                    int comb[_i3]; // output combinations
                    int c = 0; // comb index
                    int flag = 1; // flag for 
                    for (int _i = 0; _i < 12; _i++)
                    {
                        if (v[_i])  // for all combinations
                        {
                            comb[c] = _i;
                            if (c > 0 && (_i - comb[c-1] <= 2))
                                flag = 0;
                            c++;
                        }
                    }
                    // here comes the combination
                    if (flag)
                    {
                        // calc costs
                        int cost = month3 * _i3;
                        for (int _i = 0; _i < 12; _i++)
                        {
                            bool cond = true; // if the month is not month3
                            for (int _ii = 0; _ii < _i3; _ii++)
                            {
                                if (comb[_ii] == _i || comb[_ii]+1 == _i || comb[_ii]+2 == _i)
                                {
                                    cond = false; 
                                    break;
                                }
                            }
                            if (cond)
                                cost += min(month, day*plans[_i]);
                        }
                        if (cost < min_cost)
                            min_cost = cost;

                    }
                } while (prev_permutation(v.begin(), v.end()));
            }
        }
        cout << "#" << test_case << " " << min_cost << endl;



    }

    return 0;
}

