lst = [input() for _ in range(3)]

for i in range(3):
    if lst[i].isdigit():
        ans = int(lst[i]) + 3 - i
        if ans % 3 == 0 and ans % 5 == 0:
            print('FizzBuzz')
        elif ans % 3 == 0 and ans % 5 != 0:
            print('Fizz')
        elif ans % 3 != 0 and ans % 5 == 0:
            print('Buzz')
        else:
            print(ans)

        break