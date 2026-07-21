class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l = 0;
        int r = matrix.size() - 1;

        int mv = 0;
        while (l <= r) {
            mv = (r - l) + l;

            if (matrix[mv][0] == target) {
                return true;
            } else if (matrix[mv][0] > target) {
                r = mv - 1;
            } else {
                l = mv + 1;
            }
        }

        l = 0;
        r = matrix[0].size() - 1;

        while (l <= r) {
            int m = (r - l) + l;

            if (matrix[mv][m] == target) {
                return true;
            } else if (matrix[mv][m] > target) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return false;
    }
};
