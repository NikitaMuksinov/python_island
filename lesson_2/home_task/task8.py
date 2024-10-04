# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".
number=1223
print((bool(int(str(abs(number))[0]))==(int(str(abs(number))[3]))) and (int(str(abs(number))[1]))==(int(str(abs(number))[2])))
