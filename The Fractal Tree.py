import turtle as tu
branchs = 5
def draw_tree(t, branch_length, s, a):
    # s=  shorten by
    # a= angle
    if branch_length > branchs:
        t.forward(branch_length)
        new_length = branch_length - s
        t.left(a)
        draw_tree(t, new_length, s, a)
        t.right(a * 2)
        draw_tree(t, new_length, s, a)
        t.left(a)
        t.backward(branch_length)
tree = turtle.Turtle()
tree.hideturtle()
tree.setheading(90)
tree.color('green')
draw_tree(tree, 50, 5, 30)
turtle.mainloop()
