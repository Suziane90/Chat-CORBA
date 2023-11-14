from omniORB import CORBA, PortableServer
import HelloApp, HelloApp__POA

class Hello_i(HelloApp__POA.Hello):
    def sayHello(self):
        return "Hello, World!"

orb = CORBA.ORB_init()
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()

helloObj = Hello_i()
helloObjRef = helloObj._this()

ior = orb.object_to_string(helloObjRef)

with open("hello_server.ior", "w") as iorFile:
    iorFile.write(ior)

print(f"Servidor pronto. IOR salvo em hello_server.ior: {ior}")

orb.run()
