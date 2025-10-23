device_info = {}
num_friends = 6
for _ in range(num_friends):
    friend_name = input()
    device_name = input()
    price_str = input()
    price = int(price_str)
    if device_name in device_info:
        device_info[device_name][0] += 1
        if price < device_info[device_name][1]:
            device_info[device_name][1] = price
    else:
        device_info[device_name] = [1, price]
best_device_name = ""
max_popularity = -1
min_price_for_max_popularity = float('inf')
for device_name, data in device_info.items():
    current_popularity = data[0]
    current_min_price = data[1]
    if current_popularity > max_popularity:
        max_popularity = current_popularity
        min_price_for_max_popularity = current_min_price
        best_device_name = device_name
    elif current_popularity == max_popularity:
        if current_min_price < min_price_for_max_popularity:
            min_price_for_max_popularity = current_min_price
            best_device_name = device_name
print(best_device_name)
