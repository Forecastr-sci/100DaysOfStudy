-- Given a number n, print Fibonacci Sequence up to n-th number.

Fibo = function(n)
	local memo = {}
	local function helper(n, memo)
		if n < 0 then
			return 0
		elseif n == 1 or n == 2 then
			return 1
		elseif memo[n] ~= nil then
			return memo[n]
		else
			local one_less = helper(n - 1, memo)
			local two_less = helper(n - 2, memo)
			memo[n] = one_less + two_less
			return memo[n]
		end
	end
	return helper(n, memo)
end

Fibo_seq = function(n)
	local first = 0
	local second = 1
	if n < 0 then
		print(first)
		return
	elseif n == 1 then
		print(second)
		return
	end
	for _ = 1, n do
		local new = first + second
		print(new)
		first = second
		second = new
	end
end
-- print(Fibo(tonumber(arg[1])))
print(Fibo_seq(tonumber(arg[1])))
