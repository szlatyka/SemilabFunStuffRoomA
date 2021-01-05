Api.Group.Create('Analysis')


for group in Api.Group.All():
    print(group.name())