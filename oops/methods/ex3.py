#class method:
class milestone:
    myname='jagadeesh'
    @classmethod
    def friends(cls):
        friendname='hari'
        print(cls.myname,'and',friendname,'are best friends')
m=milestone()
m.friends()