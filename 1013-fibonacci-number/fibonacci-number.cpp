class Solution {
public:
    int fibonacci[30]={0,1};
    int fib(int n) {
        if(n<=0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        long long int first=0,second=1,next=0;
        for(int i=2;i<=n;i++){
          next = first+second;
          first= second;
          second= next;
        }
        return next;
    }
};