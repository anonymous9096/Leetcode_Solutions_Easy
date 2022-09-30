def ReverseString(s):
    getset = []
    ls = list(s)
    rtf = []
    laststopage = 0
    for i in range(len(ls)+1):
        if i == len(ls):
            rtf.append(s[laststopage:i])
            fire = []
            for k in range(len(rtf)+1):
                if k == len(rtf):
                    print(*fire)
                else:
                    fire.append((rtf[k][::-1]).replace(" ", ""))


        elif ls[i] == " ":
            rtf.append(s[laststopage:i])
            laststopage = i


if __name__=="__main__":
    words = "Himu Rupa Dhorsok"
    ReverseString(words)

"""

Explanation
st="Hello Shagufta"
**split function break the string into words. **
eg: print(st.split(" "))-----['Hello', 'Shagufta']

If we use [::-1] it will revese the element of list
eg: print(st.split(" ")[::-1])----['Shagufta', 'Hello']

if we use [: : -1] with join function, it will reverse the element of list as well as letters of element.
eg: print(" ".join(st.split(" "))[::-1])----atfugahS olleH
so we apply two times [: : -1] to replace the elements to the oriinal index
eg: print(" ".join(st.split(" ")[::-1])[::-1]) ------olleH atfugahS

"""