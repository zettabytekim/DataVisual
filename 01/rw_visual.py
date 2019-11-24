import matplotlib.pyplot as plt
from random_walk import RandomWalk
plt.style.use(['dark_background'])

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    plt.figure(figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, 
                cmap=plt.cm.Blues, edgecolor='none', s=1)
    
    # 시작과 끝점 강조
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolor='none', s=100)
    
    # 축 없애기
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break