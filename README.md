# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

profitable path: tokenB->tokenA->tokenD->tokenC->tokenB

* tokenB->tokenA
    * amountIn: 5 tokenB, amountOut: 5.655321988655321988 tokenA
* tokenA->tokenD
    * amountIn: 5.655321988655321988 tokenA, 2.458781317097933552 tokenD
* tokenD->tokenC
    * amountIn: 2.458781317097933552 tokenD, 5.088927293301515695 tokenC
* tokenC->tokenB
    * amountIn: 5.088927293301515695 tokenC, 20.129888944077446732 tokenB

final reward: 20.129888944077446732 tokenB

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

Slippage in AMM happens when traders pay/receive a different price than what they initially requested due to a price movement. We can mitigate slippage through adjusting slippage tolerance.

In function: `swapTokensForExactTokens`, there is a argument called `amountInMax` that can let us adjust slippage tolerance. The prototype of the function is as below:

```solidity
function swapTokensForExactTokens(
  uint amountOut,
  uint amountInMax,
  address[] calldata path,
  address to,
  uint deadline
) external returns (uint[] memory amounts);
```


## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

Upon initial liquidity minting, Uniswap V2 uses geometric mean of the amount deposited. If there is no minimum liquidity burned, attacker can control the value of the minimum quantity of liquidity token shares by manipulating the initial liquidity minting. Attackers could make the minimum quantity of liquidity token shares value so high by performing donations to the pool to make it infeasible for small liquidity providers to provide liquidity.

By minimum liquidity, Uniswap V2 can ensure that there is at least quite a number of minimum liquidity tokens, and thus make it harder for attacker to perform the attack.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

The formula is: 

`liquidity = min(amount0 / reserve0, amount1 / reserve1) * totalSupply`

The intention is to maintain the ratio of the two tokens (the relative prices) in the pool. With the specific formula, when liquidity providers provide liquidity that are not of the same ratio of the tokens currently in liquidity pool, liquidity providers will lose money (receive less liquidity token) due to the formula.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

The following scenario shows a sandwich attack.

Suppose the victim is swapping A token for B token.

Attacker detects the victim's transaction in the mempool, and swap A token for B token before the victim (front running, possibly by giving higher priority fee), then the amount of token B that one unit of token A will become lower. (value of token A increases). Leading to victim will have a slippage. Then, after the victim's swap transaction, A token's value would raise again. This time, attacker can swap B token for A token, and get more A token then initial.
