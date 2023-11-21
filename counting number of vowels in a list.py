def count_vowel(str_value):
    total_vowels=0
    for i in str_value:
        if i in "aeiou":
            total_vowels+=1
    print(f"given string {str_value}")
    print(f"{total_vowels=}")
count_vowel((input(">")))
          
    
