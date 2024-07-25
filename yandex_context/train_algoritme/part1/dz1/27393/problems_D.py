

NO_SOLUTION = 'NO SOLUTION'
MANY_SOLUTIONS = 'MANY SOLUTIONS'

def print_sol(a, b, c): #линейное ур
	def print_x(x):
		int_x = int(x)
		if int_x == x:
			return int_x
		else:
			return "NO SOLUTION"

	if c < 0:
		return "NO SOLUTION"
	elif c == 0:
		if a == 0:
			if b == 0:
				return "MANY SOLUTIONS"
			else:
				return "NO SOLUTION"
		else:
			print_x(-b/a)
	else:
		if a == 0:
			if b == 0:
				return "NO SOLUTION"
			else:
				if c*c == b:
					return "MANY SOLUTIONS"
				else:
					return "NO SOLUTION"
		else:
			return print_x((c*c - b)/a)

def solve(a:int,b:int,c:int):
    if c < 0:
        return NO_SOLUTION
    if a == 0 and b>=0:
        if c*c == b:
            return MANY_SOLUTIONS
        return NO_SOLUTION
    if a!=0:
        x = (c**2 - b) / a
        if c != 0:
            v1 = (a * x) + b
            left = v1 ** 0.5
            if left == c and x.is_integer():
                return int(x)
        elif x == int(x):
            return int(x)

        return NO_SOLUTION
    return NO_SOLUTION



if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    result = solve(a,b,c)
    print(result)



