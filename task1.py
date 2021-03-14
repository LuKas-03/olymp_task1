from scipy.misc import derivative

# шаг 
step = 0.0001

# определяем функцию
def f(x, y):
    return (1-x)**2 + (100*((y-x**2)**2))

# начальн. значение
xn = -1
yn = -1
N = f(xn, yn)
change_x = True;
change_y = True;

# заводим словарь, где будем хранить все найденные значения функции
Y = {N: (xn, yn)}

# по формуле градиентного спуска получаем все значения x y
for iteri in range(5000):
    xn_new = xn + step*diff((1-x)**2 + (100*(y-x**2)**2), x).subs({x:xn, y:yn})
    yn_new = yn + step*diff((1-x)**2 + (100*(y-x**2)**2), y).subs({x:xn, y:yn})
    
    N = round(f(xn_new, yn_new), 2)
    Y[N] = (xn_new, yn_new)
    if_change_x = False;
    
    if ((xn_new > -3 and xn_new < 3) and abs(xn_new - xn) >= 0.01):
        xn = xn_new
        if_change = True
        
    if ((yn_new > -3 and yn_new < 3) and abs(yn_new - yn) >= 0.01):
        yn = yn_new
        if_change = True
