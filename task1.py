from scipy.misc import derivative

# шаг и ограничение циклом
step = 0.0001
max_iterations = 5000

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

# градиентный спуск
for iteri in range(max_iterations):
	if (change_x):
		xn_new = xn + step*diff((1-x)**2 + (100*(y-x**2)**2), x).subs({x:xn, y:yn})
    if (change_y):
	yn_new = yn + step*diff((1-x)**2 + (100*(y-x**2)**2), y).subs({x:xn, y:yn})
    
    N = round(f(xn_new, yn_new), 2)
    Y[N] = (xn_new, yn_new)
    
    if ((xn_new < -3 or xn_new > 3) or abs(xn_new - xn) < 0.01):
        xn = xn_new
        change_x = False
        
    if ((yn_new < -3 or yn_new > 3) or abs(yn_new - yn) < 0.01):
        yn = yn_new
        change_y = False
		
	if (not change_x and not change_y): break
