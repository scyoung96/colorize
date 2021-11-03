def colorize(string, *args):
    colors = {'blue': '027', 'cyan': '045', 'green': '048', 'lime': '154', 'yellow': '011', 'orange': '202', 'red': '124', 'pink': '213', 'purple': '129', 'violet': '055'}
    string = str(string)
    str_len = len(string)
    split_len = int(str_len / len(args))

    if len(args) == 1:
        # if args[0] == "end=''":
        #     print(string)
        # else:
        return f'\033[38;5;{colors[args[0]]}m{string}\033[0;0m'

    else:
        ret_str = ''

        for i in args:
            ret_str += f'\033[38;5;{colors[i]}m{string[:split_len]}\033[0;0m'
            string = string[split_len:]

        if split_len * len(args) != str_len:
            ret_str += f'\033[38;5;{colors[i]}m{string}\033[0;0m'

    return ret_str

def printc(string, *args):
    if len(args) == 1:
        print(colorize(string, args[0]))

    else:
        str_len = len(string)
        split_len = int(str_len / len(args))
        ret_str = ''

        for i in args:
            ret_str += colorize(string[:split_len], i)
            string = string[split_len:]
        
        if split_len * len(args) != str_len:
            ret_str += colorize(string, i)

        else:
            print(ret_str)
