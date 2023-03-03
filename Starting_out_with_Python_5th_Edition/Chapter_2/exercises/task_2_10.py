# Задание #10 к главе 2
# Текст задания находится в файле tasks_ru.txt
#
# Task #10 to chapter 2
# The text of the task is in the file tasks_en.txt

base_bun = 48
sugar_base_bun = 1.5
sugar_one_bun = sugar_base_bun / base_bun
oil_base_bun = 1
oil_one_bun = oil_base_bun / base_bun
flour_base_bun = 2.75
flour_one_bun = flour_base_bun / base_bun

bun_n = int(input(f'Сколько булочек вы хотите приготовить?: '))
print(f'Для вашего количества булочек потребуется: \n'
      f'Сахар:\t{bun_n * sugar_one_bun:.2f} стакан(а)\n'
      f'Масло:\t{bun_n * oil_one_bun:.2f} стакан(а)\n'
      f'Мука:\t{bun_n * flour_one_bun:.2f} стакан(а)')
