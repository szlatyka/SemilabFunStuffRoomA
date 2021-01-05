import Api

print(Api.Group.All())

Api.Group.Create('Sorter')
print(Api.Group.All())

Api.Group.Create('Analysis')
print(Api.Group.All())

