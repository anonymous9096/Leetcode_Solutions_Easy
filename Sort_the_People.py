def STP(names, heights):
    nm = names
    hm = heights
    nm_new = []
    hm_sort = sorted(hm)
    hm_sort.reverse()
    for i in range(len(nm)):
        z = hm_sort.index(hm[i])
        nm_new.append(nm[z])

    return print(nm_new)


if __name__=="__main__":
    names =["GXLVEHVABFOGSFXUYYR","TUHxnsxmu","X","OOYBLVKmzlaeaxbprc","ARNLAPtfvmutkfsa","XPMKPDUWOQEEILtbdjip","QICEutjbr","R"]
    heights = [11578,89340,73785,12096,55734,89484,59775,72652]
    STP(names, heights)
