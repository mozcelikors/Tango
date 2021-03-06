rover_id = 1
topic_control = "rover/{}/RoverDriving/control".format(rover_id)
topic_telemetry = "rover/{}/telemetry".format(rover_id)
hostname = "bcx-hono.eastus.cloudapp.azure.com"
port = 1883
keepalive = 60
username = "rover{}@DEFAULT_TENANT".format(rover_id)
password = "hono-rover{}".format(rover_id)
auth = {'username': username,
        'password': password}
