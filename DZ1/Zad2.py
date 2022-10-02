# Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


trigger = True 

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if not(x or y or z) != (not x and not y and not z) :
                print(f"Утверждение ложно {x} {y} {z}")
                trigger = False
                break

if trigger: print(f"Выражение верно {x} {y} {z}")



