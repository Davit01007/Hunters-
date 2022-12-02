# Հրաձիգներ

1. Ստեղծել ծրագիր, որտեղ հրաձիգները կրակում են թիրախներին:
Յուրաքանչյուր մարդ ունի իր անունը, տարիքը (տարիներով) և կրակելու փորձը (տարիներով)(стаж):

2. Հրաձիգները բաժանվում են 3 խմբի՝ նորեկ, փորձառու և գիտակ (որորնք բոլորը հրաձիգ դասի ժառանգներ են):
Յուրաքանչյու հրաձիգի համար գրել պոլիմորֆ մեթոդ «կրակել»՝ առանձ պառամետրերի, որը պետք է
վերադարձնի bool արժեք (կպել եմ – true, չեմ կպել – false):

3. Թիրախին կպնելը որոշվում է պատահական սկզբունքով: Նորեկի համար կպնելու հավանականությունը հավասար է 0,01*փորձ, փորձառուի
համար՝ 0,05*փորձ, գիտակի համար՝ 0,9 – 0,01* տարիք:

4. Հրաձիգները կրակում են թիրախին հերթով՝ մինչև նրանցից մեկն կպնի թիրախին: Հրաձգությունը կավարտվի այն ժամանակ,
երբ ինչ-որ մեկը կպնի թիրախին, կամ նրանցից ոչ մեկ չի կպնի:

5. Յուրաքանչյուր կրակոցից հետո կրակողի մասին ինֆորմացիան (անուն, տարիք, փորձ) և կրակոցի արդյունքը (խոցել է թիրախը թե վրիպել)
գրանցել "shooting_results_log.txt" ֆայլում (ֆայլի պարունակությունը պետք է լինի մաքուր՝ յուրաքանչյուր տողի վրա մեկական ինֆորմացիա):

6. Յուրաքանչյուր դաս պետք է հայտարարվի առանձին ֆայլում: Արդյունքում պետք է ունենանք 5 Python ֆայլ(դասերը և main ֆայլը) և մեկ տեքստային ֆայլ:

7. Գլխավոր ֆայլում ստեղծել զանգված հետևյալ հերթականությամբ՝ սկսնակ, փորձառու, պռոֆեսիոնալ, փորձառու, սկսնակ:

8. Հրաձգության արդյունքը պետք է տեսնենք տեքստային ֆայլում:

9. Կիրառել OOP main concepts (Encapsulation, Inheritance, Polymorphism):


#Importing our files for usage
from Beginner import *
from Experienced import *
from Skilled_hunter import *

# give a name and numeric values to our modules
beginner = Beginner(input("Name of beginner hunter\t"), int(input("Age\t")), float(input("Experience\t")))
print(beginner.shoot())
experienced = Experienced(input("Name of experienced hunter\t"), int(input("Age\t")), float(input("Experience\t")))
print(experienced.shoot())
skilled_hunter = SkilledHunter(input("Name of professional hunter\t"), int(input("Age\t")), float(input("Experience\t")))
print(skilled_hunter.shoot())


#To internalize the modules in a loop and write it to another 'txt' file
def shoot_result():
    for give_only_True in (beginner, experienced, skilled_hunter):
        file = open("Shooting_result_log.txt", "a", encoding="utf = 8")
        file.write(give_only_True.show())
        if give_only_True.shoot():
            file.write(f"The True result {give_only_True}\n")
        else:
            file.write(f"The False result {give_only_True}\n")
        file.close()


shoot_result()