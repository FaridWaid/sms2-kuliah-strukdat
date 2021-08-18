import turtle
def tree(branch_len, t):
    t.speed('slowest')
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

def main():
    my_win = turtle.Screen()
    t = turtle.Turtle()
   
    t.shape("turtle")
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(60, t)
    my_win.exitonclick()
main()
