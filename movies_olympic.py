episode = int(input())
episode_price = []
episode_price2 = []
price_left = 0
price_ls = []
customer_price = int(input())

for i in range(episode):
    price_ep = int(input())
    episode_price.append(price_ep)
    episode_price2.append(price_ep)

for i in episode_price2:
    if i < 0:
        episode_price2.remove(i)

min_ls = min(episode_price2)
if customer_price < min_ls:
    print("0")
else:
    for i in episode_price:
        price_left += i
        price_ls.append(price_left)

    price_ls.reverse()


    for i in price_ls:
        if i > customer_price:
            price_ls.pop(0)
        elif i <= customer_price:
            break
            
    for i in price_ls:
        if i <= customer_price:
            break
        else:
            price_ls.pop(0)

    print(len(price_ls))


