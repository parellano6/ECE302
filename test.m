K = 50;
N = 10000;
X = randi(365,[N,K]);
Y = sort(X,2,'ascend');
dY = abs(Y(:,2:K) - Y(:,1:K-1))
Output = sum(dY==0,2);
Prob_est = sum(Output>0)/N
