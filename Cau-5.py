---
[R]
R1 ansible_host=10.215.26.220
R2 ansible_host=10.215.26.221
[R:vars]
ansible_become_password=vnpro#321
ansible_user=vnpro
ansible_password=vnpro#123
ansible_connection=network_cli
ansible_become="yes"
ansible_become_method="enable"
ansible_network_OS=ios

- name: enable int
ios_interfaces:
    config:
        - name: "{{item.name}}"
        enabled: yes
with_items:
    - { name: Ethernet0/1 }
    - { name: Ethernet0/2 }
    
- name: setip
  ios_l3_interfaces:
      config:
          - name: "{{tem.name}}"
            ipv4:
            -  address: "{{item.ip}}"
        state: merged
with_items:
    - { name: Ethernet0/1 ,ip: 192.168.1.1/24, host: R1 }
    - { name: Ethernet0/2 ,ip: 192.168.12.1/24, host: R1 }
    - { name: Ethernet0/1 ,ip: 192.168.2.1/24, host: R2 }
    - { name: Ethernet0/1 ,ip: 192.168.12.2/24, host: R2 }
    
when: inventory_hostname == item.host

- name: config static route
cisco.ios.ios_static_routes: 
    config:
      - address_families:
        - afi: ipv4
        routes:
            - dest: "{{ item.prefix }}" 
               next_hops:
               - forward_router_address: "{{ item.next_hop }}"
with_items: 
    - { prefix: 192.168.2.0/24 , next_hop: 192.168.12.2 , host: R1 }
    - { prefix: 192.168.1.0/24 , next_hop: 192.168.12.1 , host: R2 } 
when: inventory_hostname == item.host
 - name: show route
ios_command: 
	commands:
	- show ip route 
	register: show_route
- debug: var=show_route.stdout_lines