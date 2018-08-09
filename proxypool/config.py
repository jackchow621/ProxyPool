# Redis数据库的地址和端口
HOST = '192.168.1.130'
PORT = 6379

# 如果Redis有密码，则添加这句密码，否则设置为None或''
PASSWORD = ''

# 获得代理测试时间界限
get_proxy_timeout = 10

# 代理池数量界限
POOL_MIN_THRESHOLD = 20
POOL_MAX_THRESHOLD = 100

# 检查周期
VALID_CHECK_TIME = 60
POOL_LEN_CHECK_TIME = 20

# 测试API，用百度来测试
TEST_API = 'http://www.baidu.com'
