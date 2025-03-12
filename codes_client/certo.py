from autolimpa import clear_terminal
from separa import separa
from datagramas import datagrama

def check_h0(datagrama: bytes, num: int) -> bool:
    return datagrama[0] == num

def certo(datagrama: bytes, num: int) -> bool:
    return datagrama[7] == 1

if False:
    data = b'\x10]\xe9q\x12U\x1c\x12&9\xc0\xf1\x947\xb4\xb6\xc0\xcc\xd1\xc7\x90\x03\xc1\xd4v(\xa7o\x9e\\o\x08e;\x13\xdd\xe4+s\xe0\x99\x01\xaf\x8e\',\x06\x85\xedLi\xd2V\x91/\x8f\x1b9\x9b@\xa5\x11\xbb@\xa3\x96A@6\x118o\xc0\x7fo\x1b\xba\x1f\xa8\xe7\xbb\xc7\xc2\xf9\x8e\xec\xf1\t\x0e\x9d\xf9\\\xcdA\x17I\xb2.\x96^\x9f\xfc\x1eN\xa9\xb8\xbb\x90Z\xd3\x07\xdf\x8d\xab\n77\x9fQ\x84\x9eC\xa9\xceL\xf9\xf6\x9eM\xc9\x131\xfa:J\xb2\x88\x8bw\xf6~\x0eR\x91\xc3\xa0\xeb\xa9n\xb2\xf4\xb8*:\x9b\xe3\xa4\x0e\xf6@\xa2\xe4\xea\x97\xdc\xb0d\x00\x87\x03\xce\xa6\xee\xf1\xa0\x01\x95\xb4\xedUi\x13\xb3Fzr\x0b\xce\xf6l\xea\xd8/\xd6\xf4\xde\xae\xe6aW\x04!\xaa\xd4Q\xe9\x18S\x10\x18p\xd2\xbf:\xdb\noGX\xff\x81\xce/\x03Kk0y\xe6\xe2\xd6qa\x11\x1d\xa0Y\xe2\x98\x9c\xf6\\\x97'

    parte = (separa(data))[0]

    final = datagrama(parte,1,1,0,4)

    print(check_h0(final,4))