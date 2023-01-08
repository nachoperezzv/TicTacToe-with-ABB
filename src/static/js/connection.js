const ips = [
    "0.0.0.0",
    "127.0.0.0",
    "127.0.0.1"
];

const ports = [
    "4000",
    "5000", 
    "5005",
    "5050",
    "5055",
    "5500",
    "5555",
    "8000",
    "8888"
];

let select_ip = document.querySelector('#select_ip');
let select_port = document.querySelector('#select_port');

for (let i = 0; i < ips.length; i++) {
    select_ip.options[i] = new Option(ips[i]);
}

for (let i = 0; i < ports.length; i++) {
    select_port.options[i] = new Option(ports[i]);
}
 
select_ip.selectedIndex = 3;
select_port.selectedIndex = 1;
updateABBconfig();

function updateABBconfig() {
    let data = {
                'ip': ips[select_ip.selectedIndex],
                'port': ports[select_port.selectedIndex]
            };

    fetch(
        '/configuracion/setABBconfig', 
        {
            method: 'POST',
            body: JSON.stringify(data)
        }
    );
}