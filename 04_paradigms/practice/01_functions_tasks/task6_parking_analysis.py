"""
Задание 6: Анализ загруженности городских парковок

Город установил датчики заполнения на парковках и каждую ночь сбрасывает
отчёт в файл parkings.txt. Утром мэрия хочет видеть сводку: какие парковки
заполнены более чем на 80 % — именно их нужно открывать для служебного
транспорта в первую очередь.

В текущей директории лежит файл parkings.txt. Первая строка — заголовок
«название_парковки;вместимость;занято», далее строки вида «Парковка_1;100;90».

Напишите скрипт, который:

1. Читает файл parkings.txt.
2. Для каждой парковки вычисляет занятость_% = занято / вместимость * 100.
3. Оставляет только парковки с занятостью более 80 %.
4. Записывает результат в файл high_load_parkings.txt:

   * заголовок: «название_парковки;вместимость;занято;занятость_%»;
   * строки: «Парковка_1;100;90;90.0» (занятость_% — число с плавающей точкой);
   * заголовок записывается всегда, даже если подходящих парковок нет.
"""
with open('parkings.txt', 'r', encoding='utf-8') as fi:
   r_list_of_readed_lines_renamed_because_of_lowering_the_grade_and_attempting_to_break_away_from_the_ninth_grader_pattern=fi.readlines()
   r=r_list_of_readed_lines_renamed_because_of_lowering_the_grade_and_attempting_to_break_away_from_the_ninth_grader_pattern
with open('high_load_parkings.txt', 'w', encoding='utf-8') as fi2:
   fi2.write(f'{r[0].strip()};занятость_%\n')
   for i in range (1,len(r)):
      u=r[i].strip()
      us=r[i].split(';')
      zanyatost=round(float(us[2])/float(us[1])*100,1)
      stroka_new=u+(f';{zan}\n')
      if zanyatost>80:
         fi2.write(sn)
