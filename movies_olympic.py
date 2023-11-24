episode_n_person = input()
ep_ps_ls_raw = episode_n_person.split()
ep_ps_ls_edit = [] # use
for i in ep_ps_ls_raw:
    ep_ps_ls_edit.append(int(i))

price_episode = input()
price_episode_raw = price_episode.split()
price_episode_edit = [] # use

for i in price_episode_raw:
    price_episode_edit.append(int(i))

money_ls = []

for i in range(ep_ps_ls_edit[1]):
    money = int(input())
    money_ls.append(money)

episode_ls_debug = []
debug_1 = 0

for j in price_episode_edit:
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

