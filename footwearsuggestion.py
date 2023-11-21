def getting_user_input():
    print(" Footwear Suggestion")
    getting_input=input("What is the weather today! [Sunny!,Winter!,Rainy!] ")
    if getting_input.isalpha():
        def sunny():
            print(f"its {getting_input} today,its good to wear Sneaker")
        def winter():
            print(f"its {getting_input} today,its good to wear Boots")
        def rainy():
             print(f"its {getting_input} today,its good to wear gumboot")
        if getting_input.casefold()=="sunny":
            sunny()
        elif getting_input.casefold()=="winter":
            winter()
        elif getting_input.casefold()=="rainy":
            rainy()
        else:
            print(f"No footwear is available for this {getting_input} weather")
    else:
        print("type a valid input")
getting_user_input()
