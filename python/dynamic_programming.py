"""problems that can be solved using dynamic programming approach"""

import sys


# to solve something with dynamic programming, we need to look for a problem that:
# - can be divided in smaller similar subproblems (recursive approach is possible)
# - these subproblems should overlap and somehow interact with each other, solving a subproblem should bring us closer to the solution of big problem
def fibbonaci_nth(n: int) -> int:
    # base cases
    if n == 1 or n == 2:
        return 1

    return fibbonaci_nth(n - 1) + fibbonaci_nth(n - 2)


# this solution has exponential space and time complexity, however, by using memoization we can make it have linear complexity
def better_fibbonaci(n: int) -> int:
    # initialize memoization dictionary
    memo = {}

    def helper(n: int, memo: dict):
        if n == 1 or n == 2:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
        return memo[n]

    return helper(n, memo)


# let's solve maze problem. Question. How many ways can person travel from top left corner to bottom right corner?
# Only down and right moves are allowed, the size of the grid is n * m.
def grid_traveller_old(n: int, m: int) -> int:
    # we could say that after each movement we have a new problem with a smaller map, since we decrease either n or m.

    # base cases
    if n == 0 or m == 0:
        return 0  # empty grid, untraversable
    if n == 1 and m == 1:
        return 1  # in 1*1 grid we are already at start and finish, there is one possible way to do that (do nothing)

    # in other cases we either move down (and get to grid_traveller(n-1, m)) or right (and get to grid_traveller(n, m-1))
    return grid_traveller_old(n - 1, m) + grid_traveller_old(n, m - 1)


def grid_traveller_dp(n: int, m: int) -> int:
    memo: dict = {}

    def helper(n: int, m: int, memo: dict) -> int:
        # base cases
        if 0 in (n, m):
            return 0
        if n == 1 and m == 1:
            return 1

        # memo case
        if (n, m) in memo:
            return memo[(n, m)]
        if (m, n) in memo:
            return memo[(m, n)]

        memo[(n, m)] = helper(n - 1, m, memo) + helper(n, m - 1, memo)
        return memo[(n, m)]

    return helper(n, m, memo)


def can_sum_dp(s: int, val: list) -> bool:
    memo = {}

    def helper(s: int, val: list, memo: dict) -> bool:
        # base cases>
        if s == 0:
            return True  # we can always get a sum of 0 by not taking any 'coins'
        if s < 0:
            return False  # if we reach below 0, that means we overshoot our target

        if s in memo:
            return memo[s]

        memo[s] = any([helper(s - i, val, memo) for i in val])
        return memo[s]

    return helper(s, val, memo)


def how_sum_dp(s, val):
    memo = {}

    def helper(s, val, memo):
        if s == 0:
            return []
        if s < 0:
            return None

        if s in memo:
            return memo[s]

        memo[s] = None
        for n in val:
            rem = s - n
            remResult: list | None = how_sum_dp(rem, val)

            if remResult is not None:
                memo[s] = remResult + [n]
                break

        return memo[s]

    return helper(s, val, memo)


if __name__ == "__main__":
    match sys.argv[1]:
        case "fib":
            print(better_fibbonaci(int(sys.argv[2])))
        case "grid":
            print(grid_traveller_dp(int(sys.argv[2]), int(sys.argv[3])))
        case "cansum":
            values: list = [2, 3]
            print(f"we can only use following values: {values}")
            print(can_sum_dp(int(sys.argv[2]), values))
        case "howsum":
            values: list = [2, 3]
            print(how_sum_dp(int(sys.argv[2]), values))
