from redis import StrictRedis


class Config:
	DEBUG=None
	SECRET_KEY="NciVoXZvm53HoX8RWwULCgbD4BMAaIPmDHumYuhlddZapLF7nrUkcQ=="

	# 配置数据库的连接
	SQLALCHEMY_DATABASE_URI="mysql://root:Mysql@123@localhost/info7"
	SQLALCHEMY_TRACK_MODIFICATIONS=False

	# redis配置
	REDIS_HOST="127.0.0.1"
	REDIS_PORT="6379"

	# 状态保持的 session 信息存储在 redis 数据库中

	SESSION_TYPE="redis"                                              # 指定 session 保持到 redis 中。
	SESSION_REDIS=StrictRedis (host=REDIS_HOST, port=REDIS_PORT)      # 使用 redis 的实例
	SESSION_USE_SIGNER=True                                           # 让 cookie 中的 session_id 被加密签名处理。
	PERMANENT_SESSION_LIFETIME=86400                                  # session 的有效期，单位是秒


# 开发模式下的配置
class developmentConfig (Config):
	DEBUG=True


# 生产模式下的配置
class productionConfig (Config):
	DEBUG=False

config={
	'development': developmentConfig,
	'production': productionConfig

}
