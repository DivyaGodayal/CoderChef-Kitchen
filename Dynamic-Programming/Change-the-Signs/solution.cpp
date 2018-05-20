#include <unordered_map>
#include <vector>
#include <limits>
#include <cmath>
#include <iostream>
#include <utility>

using namespace std;
typedef long long LL;

LL INF = numeric_limits<long>::max();
vector<vector<LL> > memo (100005, vector<LL>(2, INF));
vector<vector<LL> > parent (100005, vector<LL>(2, 0));

LL recurse(vector<LL>& numbers, int i, bool is_prev_negated) {
    if(i >= numbers.size()) {
        return 0;
    }

    if(memo[i][is_prev_negated] != INF) {
        return memo[i][is_prev_negated];
    }

    LL pos = recurse(numbers, i + 1, false) + numbers[i];
    LL neg = INF;
    if (is_prev_negated) {
      if(numbers[i] < (numbers[i-1] - numbers[i-2]) && (i == numbers.size() - 1 || numbers[i] < numbers[i + 1])) {
          neg = recurse(numbers, i + 2, true) - numbers[i] + (i < numbers.size() - 1 ? numbers[i + 1] : 0);
      }
    } else {
        if(numbers[i] < numbers[i-1] && (i == numbers.size() - 1 || numbers[i] < numbers[i + 1])) {
          neg = recurse(numbers, i + 2, true) - numbers[i] + (i < numbers.size() - 1 ? numbers[i + 1] : 0);
        }
    }

    memo[i][is_prev_negated] = min(pos, neg);
    parent[i][is_prev_negated] = min(pos, neg) == pos ? 1 : -1;
    return min(pos, neg);
}

void retrace(int N, vector<LL>& numbers, bool initial_positive) {
    bool p;
    int start = 1;
    if(initial_positive == true) {
        cout << numbers[0] << " ";
    } else {
        cout << -1 * numbers[0] << " " << numbers[1] << " ";
        start = 2;
    }

    for(int i = start; i < N; ) {
        if (parent[i][is_prev_negated] > 0) {
          is_prev_negated = false;
          cout << numbers[i] << " ";
          i += 1;
        } else {
          is_prev_negated = true;
          cout << -1 * numbers[i] << " ";

          if(i <  N - 1) {
              cout << numbers[i + 1] << " ";
          }
          i += 2;
        }
    }

    cout << endl;
}


int main() {
    int T, N;
    LL x;
    cin >> T;

    while(T--) {
        cin >> N;
        vector<LL> numbers;

        for(int i = 0; i < N; i++) {
            cin >> x;
            numbers.push_back(x);
        }

        if(N == 1) {
            cout << (-1 * numbers[0]) << endl;
            continue;
        }

        for(int i = 0; i < N; i++) {
           for(int j = 0; j < 2; j++) {
              memo[i][j] = INF;
              parent[i][j] = 0;
           }
        }

        bool initial_positive = false;
        LL ans = INF, pos = INF, neg = INF;
        if(numbers[0] < numbers[1]) {
            pos = recurse(numbers, 1, false) + numbers[0];
            neg = recurse(numbers, 2, true) - numbers[0] + numbers[1];

            if(pos < neg) {
               initial_positive = true;
            }

        } else {
            recurse(numbers, 1, false) + numbers[0];
            initial_positive = true;
        }

        retrace(N, numbers, initial_positive);
    }
}

