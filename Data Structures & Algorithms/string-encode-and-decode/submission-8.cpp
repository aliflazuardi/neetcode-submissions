class Solution {
public:
    string encode(vector<string>& strs) {
        string encoded = "";

        for (const string& str : strs) {
            encoded += to_string(str.length()) + "#" + str;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> decoded;
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int l = stoi(s.substr(i, j-i));
            string t = s.substr(j+1, l);
            decoded.push_back(t);
            i = j + 1 + l;
        }

        return decoded;
    }
};
