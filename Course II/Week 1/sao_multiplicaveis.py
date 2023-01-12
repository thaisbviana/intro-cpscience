def sao_multiplicaveis(m1,m2):
    columns_m1 = len(m1[0])
    rows_m2 = len(m2)
    if columns_m1 == rows_m2:
        return True
    else:
        return False