void plusMinus(vector<int> arr) {
    int precision_level = 6;
    float po, ne, ze;
    po = ne = ze = 0;
    int n = arr.size();
    for(int i = 0; i < n; i++){
        if (arr[i] > 0)
            po++;
        else if (arr[i] < 0)
            ne ++;
        else ze++;
    }
    cout << fixed << setprecision(precision_level);
    cout << po/n << endl;
    cout << ne/n << endl;
    cout << ze/n << endl;
}

