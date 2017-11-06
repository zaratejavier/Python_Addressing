import ipaddress

ip = input("Enter an IP Address(V4 or V5) in CIDR notation:")
ip_int = ipaddress.ip_interface(ip)

if ip_int.is_private:
    print(ip, "That is a private address")

if ip_int.is_global:
    print(ip, "That is a Global address")

if ip_int.is_loopback:
    print(ip, "That is a loop back address")

if ip_int.is_multicast:
    print(ip, "That is a multicast address")

if ip_int.is_reserved:
    print(ip, "That is a reserved address")

if ip_int.is_unspecified:
    print(ip, "That is a unspecified address")


print("IP network address", ip_int.network.network_address)
print("IP broadcast address", ip_int.network.broadcast_address)
print("Total number of addresses", ip_int.network.num_addresses)
print("Number of usable addresses", len(list(ip_int.network.hosts())))

if ip_int.network.num_addresses < 32:
    for address in ip_int.network:
        print(address)