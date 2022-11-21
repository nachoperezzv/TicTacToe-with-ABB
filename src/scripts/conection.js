const ips = [
    "127.0.0.1"
];

const ports = [
    "5000", 
    "5005",
    "5050",
    "5055",
    "5500",
    "5555",
    "8000"
];

let select_ip = document.querySelector('#select_ip');
let select_port = document.querySelector('#select_port');

for (let i = 0; i < ips.length; i++) {
    select_ip.options = new Option(ips[i], i);
}

for (let i = 0; i < ports.length; i++) {
    select_port.options = new Option(ports[i], i);
}
 
select_ip.selectedIndex = 1
select_port.selectedIndex = 3



