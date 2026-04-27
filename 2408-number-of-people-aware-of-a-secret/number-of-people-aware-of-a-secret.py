class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        mod=10**9 +7
        dp=[0]*(n+1)
        dp[1]=1
        share=0
        for i in range(2,n+1):
            if i-delay >0:
                share=(share+dp[i-delay])%mod
            if i-forget >0:
                share=(share-dp[i-forget]+mod)%mod
            dp[i]=share

        tot_kn=0
        for i in range(n-forget+1,n+1):
            tot_kn=(tot_kn+dp[i])%mod
        return tot_kn


        