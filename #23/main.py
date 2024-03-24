class Square:
    ct = 0

    @staticmethod
    def sq_square(a):
        Square.__count()
        return a**2
    
    @staticmethod
    def sq_geron(a, b, c):
        Square.__count()
        p = (a + b + c) / 2
        return (p*(p-a)*(p-b)*(p-c))**(1/2)
    
    @staticmethod
    def sq_rect(a, b):
        Square.__count()
        return a * b
    
    @staticmethod
    def sq_triangle(a, b):
        Square.__count()
        return 1/2 * a * b
    
    @staticmethod
    def __count():
        Square.ct += 1
    
    @staticmethod
    def count():
        return Square.ct
    

sq = Square
print(f"Площадь треугольника по формуле Герона: {sq.sq_geron(3, 4, 5)}")
print(f"Площадь треугольника через основание и высоту: {sq.sq_triangle(6, 7)}")
print(f"Площадь квадрата: {sq.sq_square(7)}")
print(f"Площадь прямоугольника: {sq.sq_rect(2, 6)}")
print(f"Количество подсчётов площади: {sq.count()}")
