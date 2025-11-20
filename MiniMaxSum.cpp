void miniMaxSum(vector<int> arr) {
    int n = arr.size();
    long long min, max;
    min = max = 0;
    for(int i = 0; i < n; i++){
        min += arr[i];
    }
    for(int i = 0; i < n; i++){
        long long sum = 0;
        for(int j = 0; j < n; j++){
            if(j != i)
                sum += arr[j];
        }
        if(sum > max)
            max = sum;
        if (sum < min)
            min = sum;
    }
    cout << min << " " << max;
}