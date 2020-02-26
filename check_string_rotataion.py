def check_string_rotation(s1,s2):
    if len(s1) != len(s2):
        return False
    temp = s1 + s1
    if temp.count(s2) > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    s1 = "AACD"
    s2 = "ACDA"
    if check_string_rotation(s1,s2):
        print("Strings are rotation of each other")
    else:
        print("Strings are not rotation of each other")