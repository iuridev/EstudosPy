import os

print('#'*60)
ip_or_host = input('Digite um endereço IP: ')

print('-'*60)
os.system('ping -n 10 {}'.format(ip_or_host))
print('-'*60)
