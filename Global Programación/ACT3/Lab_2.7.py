import ncclient 
from cclient import manager 

m = manager.conect(
    host="10.10.20.48"
    port=830,
    username="develope"
    password="C1sco0123"
    hostkey_verify=False
)