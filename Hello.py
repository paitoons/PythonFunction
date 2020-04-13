# สร้างฟังค์ชั่นแบบไม่มี return
def hello(name):
    print("Hello %s" % name)


# การเรียกใช้งานฟังค์ชั่น
hello("Python")


# สร้างฟังค์ชั่นแบบมี return
def area(width, height):
    total = width * height
    return total


# การเรียกใช้งานฟังค์ชั่น
print(area(10, 20))


# Default value function
def show_info(name, salary =0.00, lang="not define"):
    print("Name : %s" % name)
    print("Salary : %s" % salary)
    print("Language : %s" % lang)


show_info("Mono")
show_info("Mono", 25000)
show_info("Mono", 25000, "Python")