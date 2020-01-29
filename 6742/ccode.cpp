#include<iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

float abs(float x){
    if (x>0)
        return x;
    else
        return -1. * x;
}

int main(int argc, char** argv){
    int test_case = 0;
    int T = 0;
    freopen("sample_input.txt", "r", stdin);
    cin >> T;

    for (test_case = 1; test_case <= T; ++test_case){
        int cnt = 0;
        int N = 0;
        int A = 0;
        int B = 0;
        cin >> N >> A >> B;

        int X[2000] = {0};
        int Y[2000] = {0};
        for (int n = 0; n < N; n++)
            cin >> X[n] >> Y[n];

        vector<bool> v(N);
        fill(v.begin(), v.begin() + 3, true);
        do {
            int xs[3] = {0,0,0};
            int ys[3] = {0,0,0};
            int _i = 0;
            int S = 0;
            int s1, s2;
            for (int i=0; i<N; i++){
                if (v[i]) {
                    xs[_i] = X[i];
                    ys[_i] = Y[i];
                    _i += 1;
                }
            }
            S = abs( (xs[0]*ys[1] + xs[1]*ys[2] + xs[2]*ys[0]) - (xs[0]*ys[2] + xs[2]*ys[1] + xs[1]*ys[0]));
//            for (int i=0;i<3;i++)
//                cout << xs[i] << "," << ys[i] << " | ";
//            cout << "  || S " << S << endl;
//            if (S >= A && S <= B)
//                cnt++;

        } while (prev_permutation(v.begin(), v.end()));
        cout << "#" << test_case << " " << cnt << endl;
    }

}
