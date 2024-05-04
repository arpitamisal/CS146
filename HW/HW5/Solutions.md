Problem 1:
T(N)=2T(N−1)+1

    Method: Recursion Tree.
    Analysis: Each level doubles the number of calls, but each call only adds a constant amount of work (+1+1). This leads to a sequence where each level contributes an increasingly larger amount. The depth of the recursion is NN, and the total work is dominated by the terms on the last level.
    Solution: Approximately 2N2N.

T(N)=3T(N−1)+NT(N)=3T(N−1)+N

    Method: Recursion Tree.
    Analysis: This recurrence also deeply nests calls (triples at each level). The additive term NN increases with the depth, so its contribution cannot be ignored.
    Solution: Approximately 3N3N, as the tripling effect dominates the linear growth of NN.

T(N)=9T(N/2)+N2T(N)=9T(N/2)+N2

    Method: Master Theorem.
    Form: T(N)=aT(N/b)+f(N)T(N)=aT(N/b)+f(N) where a=9a=9, b=2b=2, and f(N)=N2f(N)=N2.
    Master Theorem Cases: a=9>b2=4a=9>b2=4, thus f(N)f(N) is polynomially smaller than Nlog⁡ba=Nlog⁡29Nlogb​a=Nlog2​9.
    Solution: T(N)=Θ(Nlog⁡29)T(N)=Θ(Nlog2​9).

T(N)=100T(N/2)+Nlog⁡2c+1T(N)=100T(N/2)+Nlog2​c+1

    Method: Master Theorem.
    Form: T(N)=aT(N/b)+f(N)T(N)=aT(N/b)+f(N) where a=100a=100, b=2b=2, and f(N)=Nlog⁡2c+1f(N)=Nlog2​c+1 simplifies to O(N)O(N).
    Master Theorem Cases: a=100>b=2a=100>b=2, and f(N)f(N) is polynomially smaller than Nlog⁡ba=Nlog⁡2100Nlogb​a=Nlog2​100.
    Solution: T(N)=Θ(Nlog⁡2100)T(N)=Θ(Nlog2​100).

T(N)=4T(N/2)+N2log⁡NT(N)=4T(N/2)+N2logN

    Method: Master Theorem.
    Form: T(N)=aT(N/b)+f(N)T(N)=aT(N/b)+f(N) where a=4a=4, b=2b=2, and f(N)=N2log⁡Nf(N)=N2logN.
    Master Theorem Cases: f(N)=N2log⁡Nf(N)=N2logN grows slower than Nlog⁡ba=N2Nlogb​a=N2.
    Solution: T(N)=Θ(N2log⁡N)T(N)=Θ(N2logN).

T(N)=5T(N/2)+N2log⁡NT(N)=5T(N/2)+logNN2​

    Method: Master Theorem.
    Form: T(N)=aT(N/b)+f(N)T(N)=aT(N/b)+f(N) where a=5a=5, b=2b=2, and f(N)=N2log⁡Nf(N)=logNN2​.
    Master Theorem Cases: f(N)f(N) is smaller than Nlog⁡ba=Nlog⁡25Nlogb​a=Nlog2​5, though it's a non-standard form for Master Theorem.
    Solution: Likely T(N)=Θ(Nlog⁡25)T(N)=Θ(Nlog2​5).

Problem 2:

yetAnotherFunc(n):
if n > 1:
for(i = 0; i < 10n; i++)
doSomething;
yetAnotherFunc(n/2);
yetAnotherFunc(n/2);

Recurrence Relation:

    The loop runs 10n10n times performing a constant amount of work, let’s say cc.
    The function is called recursively twice on n/2n/2.

Recurrence Relation: T(n)=2T(n/2)+10nT(n)=2T(n/2)+10n

Solving Using Master Theorem:

    Form: T(n)=aT(n/b)+f(n)T(n)=aT(n/b)+f(n) where a=2a=2, b=2b=2, and f(n)=10nf(n)=10n.
    Master Theorem Cases: f(n)=10nf(n)=10n matches nlog⁡ba=nlog⁡22=nnlogb​a=nlog2​2=n.
    Solution: T(n)=Θ(nlog⁡n)T(n)=Θ(nlogn) since f(n)f(n) matches nlog⁡banlogb​a.
