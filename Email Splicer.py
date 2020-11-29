#Given an Email return username & directory
#Hint: username@directory.com

def splice(email):
    username = email[:email.index("@")]
    directory = email[email.index("@")+1:]
    return (username,directory)
email = 'test@sample.com'
username,directory = splice(email)
print("Username: {user} Directory: {dir}".format(user=username,dir=directory))