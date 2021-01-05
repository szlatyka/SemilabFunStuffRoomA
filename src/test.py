import Api

#Api.User.Create("gábor", "absc")
usr = Api.User.ByName("gábor")
isr2 = Api.User(1);

print("#ID: " + str(isr2.name()))

#Api.Group.Create("Test csopi")
grp = Api.Group(1);

grp.assign(usr)
print();
grp.remove(usr)
print("#ID: " + str(usr.group()));
print("#ID: " + str(usr.group()));



print(Api.Group.All())

Api.Group.Create('Sorter')
print(Api.Group.All())

Api.Group.Create('Analysis')
print(Api.Group.All())

