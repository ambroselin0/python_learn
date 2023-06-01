def anagram_1(s1: str, s2: str) -> bool:
    # 检查长度
    if len(s1) != len(s2):  # 1
        return False

    # 检查每个字符
    alist = list(s2) # 1
    pos1 = 0 # 1
    still_ok = True # 1

    while pos1 < len(s1) and still_ok: # n
        pos2 = 0 # 1
        found = False # 1
        while pos2 < len(alist) and not found: # n
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            still_ok = False
        pos1 += 1
    return still_ok
print(anagram_1('python', 'typhon'))