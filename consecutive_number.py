n = int(input())
if n == 1:
    print('1')
else:
    result = ""
    for i in range(1, n + 1):  # Цикл от 1 до n включительно
        result += str(i) * i  # Добавляем число i, повторенное i раз
    print(result)