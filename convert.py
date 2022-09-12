num = '10011010.000000000001(2)'


def extract(num):
    try:
        inteiro = num[:num.index('.')]
        fracionario = "0." + num[num.index('.') + 1:num.index('(')]
    except:
        inteiro = num[:num.index('(')]
        fracionario = 0
    base = num[num.index('(') + 1: num.index(')')]
    return inteiro, fracionario, base


def nDecimalFracionario(base, fracionario):  # retornar o flutuante em decimal
    if int(base) != 10:
        num_ = str(fracionario)[str(fracionario).index(".") + 1:]
        # print(num_[0],type(num_))
        len_ = len(num_) - 1
        exp = -1
        r = 0
        i = 0
        while (len_ >= 0):
            try:
                r += int(num_[i]) * int(base) ** exp
            except:
                hex_ = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
                #print(num_[i])
                r += int(hex_[num_[i]]) * int(base) ** exp
            #print(f"{num_[i]} * {base} ** {exp} = {r}")
            i += 1
            exp += -1
            len_ -= 1
        # print(r)
    else:
        r = fracionario
    return r


def convert(num_, b):

    # Trasnformar para decimal para poder usar os recursos do nativos do python
    len_ = len(num_) - 1
    i = 0
    r = 0

    if int(b) != 10:
        while (len_ >= 0):
            try:
                numOp = int(num_[i])
            except:
                hex_ = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
                numOp = hex_[num_[i].lower()]

            r += numOp * int(b) ** len_
            len_ -= 1
            i += 1
    else:
        r = int(num_)

    msg = f"Decimal: 0d{str(r)} \nBinario: {bin(r)} \nOctal: {oct(r)} \nHexadecimal: {hex(r)}"
    dictd = {"Decimal": "0d" + str(r), "Binario": bin(r), "Octal": oct(r), "Hexadecimal": hex(r)}
    # print(msg)
    # print(dictd)
    return dictd, msg

def fracStg(num):
    num_ = str(num)
    try:
        return num_[num_.index("."):]
    except:
        return "." + num_

def convertFracionario(decimal):
    limit = 0
    res = [fracStg(decimal)]
    baseC = [2,8,16]
    for base in baseC:
        decFracionario = decimal
        r = ''
        limit = 0
        while(1):
            if decFracionario == 0 or limit == 20:
                break
            v = float(decFracionario) * int(base)
            #print(f"{decFracionario} * {base} = {v}")
            decFracionario = v - int(v)
            if base == 16:
                hex_ = {10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
                try:
                    r += str(hex_[int(v)])
                except:
                    r += str(int(v))
            else:
                r += str(int(v))

            limit += 1
        res.append(fracStg(r))
    return res


def opInit(num):
    inteiro, fracionario, base = extract(num)
    if fracionario == 0:
        msg = convert(inteiro, base)[1]
    else:
        a = convert(inteiro, base)[0]
        decimalFracionario = nDecimalFracionario(base, fracionario)
        frac = convertFracionario(decimalFracionario)
        msg = f"Decimal: 0d{a['Decimal'] + frac[0]} \nBinario: {a['Binario'] + frac[1]} \nOctal: {a['Octal'] + frac[2]} \nHexadecimal: {a['Hexadecimal']+ frac[3]}"
    return msg


#opInit(num)
