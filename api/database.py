from mongoengine import connect

# TODO: Make more dynamic
def read_configuration():
    # expedcting file in format:
    # 1: hostname
    # 2: port number
    # 3: database
    # 4: user
    # 5: password

    with open('./api.conf') as file:
        lines = (line.rstrip() for line in file)
        lines = [x for x in lines]

    return {
        'hostname': lines[0], 
        'port': lines[1], 
        'database': lines[2],
        'user': lines[3], 
        'password': lines[4]
    }

conf_data = read_configuration()
print(conf_data)

user_ = conf_data['user']
password_ = conf_data ['password']
database_ = conf_data ['database']
host_ = conf_data['hostname']
port_ = conf_data['port']

host_data = 'mongodb://%s:%s@%s:%s/%s' %(user_, password_, host_, port_, database_)

# used for python3.x.x
# host_data = f'mongodb://{user_}:{password_}@{host_}:{port_}/{database_}'

# connect to mlab instance
connect(
    username = user_, 
    password = password_,
    host = host_data,
    port = int(port_),
    db=database_,
)
