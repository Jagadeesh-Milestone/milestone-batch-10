def d1(func):
    def login(username,password):
        return 'user details are ',func(username,password)
    return login
@d1
def d3(username,password):
    return username,password
print(d3('jagadeesh',6789))