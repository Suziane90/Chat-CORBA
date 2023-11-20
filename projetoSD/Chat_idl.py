# Python stubs generated by omniidl from Chat.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "Chat"
#
__name__ = "Chat"
_0_Chat = omniORB.openModule("Chat", r"Chat.idl")
_0_Chat__POA = omniORB.openModule("Chat__POA", r"Chat.idl")


# interface ChatServer
_0_Chat._d_ChatServer = (omniORB.tcInternal.tv_objref, "IDL:Chat/ChatServer:1.0", "ChatServer")
omniORB.typeMapping["IDL:Chat/ChatServer:1.0"] = _0_Chat._d_ChatServer
_0_Chat.ChatServer = omniORB.newEmptyClass()
class ChatServer :
    _NP_RepositoryId = _0_Chat._d_ChatServer[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Chat.ChatServer = ChatServer
_0_Chat._tc_ChatServer = omniORB.tcInternal.createTypeCode(_0_Chat._d_ChatServer)
omniORB.registerType(ChatServer._NP_RepositoryId, _0_Chat._d_ChatServer, _0_Chat._tc_ChatServer)

# ChatServer operations and attributes
ChatServer._d_sendMessage = (((omniORB.tcInternal.tv_string,0), ), (), None)
ChatServer._d_receiveMessage = ((), ((omniORB.tcInternal.tv_string,0), ), None)

# ChatServer object reference
class _objref_ChatServer (CORBA.Object):
    _NP_RepositoryId = ChatServer._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def sendMessage(self, *args):
        return self._obj.invoke("sendMessage", _0_Chat.ChatServer._d_sendMessage, args)

    def receiveMessage(self, *args):
        return self._obj.invoke("receiveMessage", _0_Chat.ChatServer._d_receiveMessage, args)

omniORB.registerObjref(ChatServer._NP_RepositoryId, _objref_ChatServer)
_0_Chat._objref_ChatServer = _objref_ChatServer
del ChatServer, _objref_ChatServer

# ChatServer skeleton
__name__ = "Chat__POA"
class ChatServer (PortableServer.Servant):
    _NP_RepositoryId = _0_Chat.ChatServer._NP_RepositoryId


    _omni_op_d = {"sendMessage": _0_Chat.ChatServer._d_sendMessage, "receiveMessage": _0_Chat.ChatServer._d_receiveMessage}

ChatServer._omni_skeleton = ChatServer
_0_Chat__POA.ChatServer = ChatServer
omniORB.registerSkeleton(ChatServer._NP_RepositoryId, ChatServer)
del ChatServer
__name__ = "Chat"

#
# End of module "Chat"
#
__name__ = "Chat_idl"

_exported_modules = ( "Chat", )

# The end.
