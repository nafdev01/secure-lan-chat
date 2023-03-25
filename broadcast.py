import netifaces
import socket

def get_ip_address():
    # Get default gateway interface
    gateway_interface = netifaces.gateways()["default"][netifaces.AF_INET][1]

    # Get interface details
    interface_details = netifaces.ifaddresses(gateway_interface)

    # Get IP address
    ip_address = interface_details[netifaces.AF_INET][0]["addr"]

    return f"{ip_address}"


def get_broadcast_address():
    # Get default gateway interface
    gateway_interface = netifaces.gateways()["default"][netifaces.AF_INET][1]

    # Get interface details
    interface_details = netifaces.ifaddresses(gateway_interface)

    # Get broadcast address
    broadcast_address = interface_details[netifaces.AF_INET][0]["broadcast"]

    return f"{broadcast_address}"


def find_device(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return None


if __name__ == "__main__":
    # Example usage
    device_ip = find_device("kalijel")
    if device_ip:
        print("Found device at IP address:", device_ip)
    else:
        print("No device found")
