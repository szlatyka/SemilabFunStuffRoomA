from Entities import *
from DbConnection import getDbSession

if __name__ == '__main__':
    sess = getDbSession()

    # user = User()
    # user.name = 'Adri'
    # user.password = '1234'
    #
    # sess.add(user)
    #
    # sess.commit()

    users = sess.query(User).all()
    for user in users:
        print(user.name, user.password)

    sess.close()