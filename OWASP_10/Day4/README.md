XML External Entity, XXE
Vulnerability that abuses xml parser/data feature. Can cause DoS attack or SSRF, port scanning and remote code execution
Attacks: in-band and out-of-band (OOB-XXE)
An in-band XXE attack is the one in which the attacker can receive an immediate response to the XXE payload.
out-of-band XXE attacks (also called blind XXE), there is no immediate response from the web application and attacker has to reflect the output of their XXE payload to some other file or their own server.

XML -> extensible markup language, used for storing and transporting data recognized by both humans and machines
* Platform or programmming independent
* DTD and Schema validations
* Data can be changed at any time 

XML prolog -> <?xml version="1.0" encoding="UTF-8"?>
Root Element is a must, case sensitive

DTD -> Document Type Definition -> defines the structure and legal elements and attributes of an XML document.

name: falcon
ssh key at: /home/falcon/.ssh/id_rsa
first 18 key: MIIEogIBAAKCAQEA7b
