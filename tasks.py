'''
ЛЕКЦІЯ 16

Завдання 1. Отримати всі відомості про співробітників.
SELECT *
FROM employees;

Відповідь MySQL (перші п’ять рядків сюди скопіював):
100	Steven	King	SKING	515.123.4567	1987-06-17	AD_PRES	24000.00	0.00	0	90
101	Neena	Kochhar	NKOCHHAR	515.123.4568	1987-06-18	AD_VP	17000.00	0.00	100	90
102	Lex	De Haan	LDEHAAN	515.123.4569	1987-06-19	AD_VP	17000.00	0.00	100	90
103	Alexander	Hunold	AHUNOLD	590.423.4567	1987-06-20	IT_PROG	9000.00	0.00	102	60
104	Bruce	Ernst	BERNST	590.423.4568	1987-06-21	IT_PROG	6000.00	0.00	103	60

Завдання 2. Отримати імена та прізвища співробітників, їх зарплату та податки.
SELECT first_name, last_name, salary, salary*.15 PF
FROM employees;

Відповідь MySQL (перші п’ять рядків сюди скопіював):
Steven	King	24000.00	3600.0000
Neena	Kochhar	17000.00	2550.0000
Lex	De Haan	17000.00	2550.0000
Alexander	Hunold	9000.00	1350.0000
Bruce	Ernst	6000.00	900.0000


Завдання 3. Отримати суму заробітної плати усіх співробітників.
SELECT sum(salary)
FROM employees;

Відповідь MySQL;
'691400.00'


Завдання 4. Отримати максимальну та мінімальну заробітну плати.
SELECT max(salary), min(salary)
FROM employees;

Відповідь MySQL:
'24000.00', '2100.00'


Завдання 5. Отримати середню заробітну плату та кількість працівників у таблиці.
SELECT avg(salary), count(employee_id)
FROM employees;

Відповідь MySQL:
'6461.682243', '107'
'''
