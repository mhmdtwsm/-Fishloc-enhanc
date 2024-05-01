import subprocess

import geocoder


def get_location_from_ip(ip_address):
    g = geocoder.ip(ip_address)
    return f"{g.country}, {g.city}" if g.ok else "Location not found"


print(
    subprocess.Popen("figlet Fishloc", shell=True, stdout=subprocess.PIPE)
    .communicate()[0]
    .decode("utf-8")
)
ip = input("\n\nEnter the IP address: ")
print(get_location_from_ip(ip))
