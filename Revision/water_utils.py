def above_target(data, target):
    counter = 0
    for i in data:
        if i > target:
            counter = counter + 1
    return counter