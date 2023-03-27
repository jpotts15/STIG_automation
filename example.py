from netmiko import ConnectHandler

# Define the commands to execute
commands = [
    "show version",
    "show interfaces",
    "show ip route",
]

# Read the device list from a file
with open("device_list.txt") as f:
    devices = [line.strip() for line in f]

# Loop over each device and execute the commands
for device in devices:
    # Define the connection parameters for Netmiko
    net_device = {
        "device_type": "cisco_ios",
        "ip": device,
        "username": "my_username",
        "password": "my_password",
    }

    # Connect to the device using Netmiko
    with ConnectHandler(**net_device) as conn:
        print(f"Connected to {device}")
        # Execute each command and print the output
        for command in commands:
            output = conn.send_command(command)
            print(f"Command: {command}\n{output}")