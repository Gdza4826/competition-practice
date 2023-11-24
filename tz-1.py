episode_n = int(input()) #thon
episode_ls = [] # list01
episode_ls_debug = [] # list02
person_n = int(input())
money_ls = [] #raca
debug_1 = 0

for i in range(episode_n):
    price_episode = int(input())
    episode_ls.append(price_episode)

for i in range(person_n):
    money_each = int(input())
    money_ls.append(money_each)

for j in episode_ls:
    debug_1 = debug_1 + j
    episode_ls_debug.append(debug_1)

episode_ls_debug.reverse()

for raca in money_ls:
    debug_2 = 0
    for l in range(len(episode_ls_debug)):
        if episode_ls_debug[l] > raca:
            debug_2 = debug_2 + 1
    if debug_2 == len(episode_ls_debug):
        print("0 debug")
    for k in range(len(episode_ls_debug)):
        if episode_ls_debug[k] <= raca:
            print(len(episode_ls_debug) - (k))
            break

