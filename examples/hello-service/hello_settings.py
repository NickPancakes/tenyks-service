DEBUG = True
SERVICE_NAME = 'hello'
SERVICE_VERSION = '0.1.1'
SERVICE_UUID = '273b62ad-a99d-48be-8d80-ccc55ef688b4'

##############################################################################
# The following setting defines a dictionary containing Redis connection
# information used when connecting to the Redis server.
#
# This setting is required.

REDIS_CONNECTION = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'password': None,
}
##############################################################################


##############################################################################
# The following channel settings are for when you need to change the default
# Redis channel key for each pipe respectively. BROADCAST_SERVICE_CHANNEL
# is used for messages going from Tenyks to Redis for the clients.
# BROADCAST_ROBOT_CHANNEL is used for messages going from clients to Tenyks
# for IRC.
#
# These are namespaced, so you shouldn't need to change them.
#
# These settings are optional

BROADCAST_SERVICE_CHANNEL = 'tenyks.service.broadcast'
BROADCAST_ROBOT_CHANNEL = 'tenyks.robot.broadcast'
##############################################################################
