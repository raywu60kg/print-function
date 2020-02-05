import pprint
import random
import sys
random_candidate = [
    '如',
    '來',
    '佛',
    '祖',
    '玉',
    '皇',
    '大',
    '帝',
    '觀',
    '音',
    '菩',
    '薩',
    '指',
    '定',
    '取',
    '西',
    '經',
    '特',
    '派',
    '使',
    '者',
    '花',
    '果',
    '山',
    '水',
    '簾',
    '洞',
    '美',
    '猴',
    '王',
    '齊',
    '天',
    '大',
    '聖'
]
def print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    if flush == True:
        str_len = len(str(*objects))
        blank_str = "            "
        line_str = ""
        for _ in range(str_len):
            line_str += "─" 

        pprint.pprint(blank_str + "╭" + line_str + "╮")
        pprint.pprint(blank_str + "|" + str(*objects) + "|")
        pprint.pprint(blank_str + "╯" + line_str + "╯")
        pprint.pprint("       ███]▄▄▄▄▄▄▄▃～～～")
        pprint.pprint(" ▂▄▅█████████▅▄▃▂")
        pprint.pprint("[████████████████]")
        pprint.pprint("◥ ⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙ ◤ ")

    else:
        pprint.pprint("".join(random.sample(random_candidate,5)).encode("utf-8"))   
