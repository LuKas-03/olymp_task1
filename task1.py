from scipy.misc import derivative

# шаг и ограничение циклом
step = 0.0001
max_iterations = 5000

# определяем функцию
def f(x, y):
    return (1-x)**2 + (100*((y-x**2)**2))

# начальн. значение
xn = 0
yn = 0
N = f(xn, yn)
change_x = True;
change_y = True;

# словарь со всеми найденными значениями функции
values = {N: (xn, yn)}

# градиентный спуск
for iteri in range(max_iterations):
    if (change_x):
        xn_new = xn + step*diff((1-x)**2 + (100*(y-x**2)**2), x).subs({x:xn, y:yn})
    if (change_y):
        yn_new = yn + step*diff((1-x)**2 + (100*(y-x**2)**2), y).subs({x:xn, y:yn})
    
    if ((xn_new < -3 or xn_new > 3)):
        change_x = False
    else: 
        xn = xn_new
        
    if ((yn_new < -3 or yn_new > 3)):
        change_y = False
    else:
        yn = yn_new

    if (not change_x and not change_y): 
        break
        
    N = round(f(xn, yn), 2)
    values[N] = (xn, yn)
        
max_v = max(values.keys())
print("max:", max_v, values[max_v])
