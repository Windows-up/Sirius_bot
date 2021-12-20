from config import alfabet, add


def toSecure(inp):
    result = ""

    for i in range(0, len(inp)):
        if inp[i] == '\n':
            result += "`"
        elif inp[i] not in alfabet:
            pass
        else:
            index = int(alfabet.index(inp[i])) + add
            if index >= len(alfabet):
                index -= len(alfabet)
            result += alfabet[index]

    return result


def deSecure(inp):
    result = ""

    for i in range(0, len(inp)):
        if inp[i] == "`":
            result += "\n"
        elif inp[i] not in alfabet:
            result += ""
        else:
            index = alfabet.index(inp[i]) - add
            if index < 0:
                index = len(alfabet) + index
            result += alfabet[index]

    return result
