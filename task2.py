# Попросить пользователя ввести слова через пробел. Отсортировать слова по количеству
# символов и вывести на экран результат.
source_text=list(input("Please,enter any text separated by spaces:").lower().split())
print(sorted(source_text))
