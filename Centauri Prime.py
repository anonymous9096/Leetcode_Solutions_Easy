kingdom = ['Mollaristan', 'Auritania', 'Zizily']
ruler = 'is ruled by'
Vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for i in range(len(kingdom)):
    if kingdom[i][-1] == any(str(tup)):
        print(kingdom[i][-1])
        print(f"Case #{i+1}:", f"{kingdom[i]}", ruler, "Bob.")


    elif kingdom[i][-1] != any(str(tup)):
        print(kingdom[i][-1])
        print(f"Case #{i+1}:", f"{kingdom[i]}", ruler, "Alice.")

    elif kingdom[i][-1] == "y":
        print(kingdom[i][-1])
        print(f"Case #{i + 1}:", f"{kingdom[i]}", ruler, "Nobody.")

    else:
        pass
