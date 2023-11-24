# person = int(input())
# customer_price = []

# for i in range(person):
#     money = int(input())
#     customer_price.append(money)

episode = int(input())
person = int(input())
episode_price = []
episode_price2 = []
price_left = 0
price_ls = []
customer_price = []

for i in range(episode):
    price_ep = int(input())
    episode_price.append(price_ep)
    episode_price2.append(price_ep)

for i in range(person):
    money = int(input())
    customer_price.append(money)

for customer_pr in customer_price:
    for i in episode_price2:
        if i < 0:
            episode_price2.remove(i)
    min_ls = min(episode_price2)
    if customer_pr < min_ls:
        print("0")
    else:
        for i in episode_price:
            price_left += i
            price_ls.append(price_left)

        price_ls.reverse()

        for i in price_ls:
            if i > customer_pr:
                price_ls.pop(0)
            elif i <= customer_pr:
                break
                
        for i in price_ls:
            if i <= customer_pr:
                break
            else:
                price_ls.pop(0)

        print(len(price_ls))
        print(price_ls)

print(episode_price)
print(customer_price)
