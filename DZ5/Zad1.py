# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

list_user = "58абв8 45абв44 ооооабв 87654 !!!"
new_list = list_user.split(" ")
result = ""
for i in new_list:
    if "абв" not in i:
        result += i + ""
print(result)