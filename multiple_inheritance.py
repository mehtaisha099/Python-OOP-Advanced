class Father:
    def show_father(self):
        print("This is Father class")


class Mother:
    def show_mother(self):
        print("This is Mother class")


class Child(Father, Mother):
    def show_child(self):
        print("This is Child class")


child = Child()

child.show_father()
child.show_mother()
child.show_child()