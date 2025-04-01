def str_to_col(str):
    rgb_list=[]
    num_str=""
    for char in str:
        if char == "," or char == ")":
            rgb_list.append(int(num_str))
            num_str=""
        elif char != "(" and char != " ":
            num_str+=char
    return tuple(rgb_list)