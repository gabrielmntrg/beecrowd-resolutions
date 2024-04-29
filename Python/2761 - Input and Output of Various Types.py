import struct

inputs = input().split(' ', maxsplit=3)
a = int(inputs[0])
b = float(inputs[1])
b = struct.unpack('f', struct.pack('f', b))[0] # Não sei como isso funciona
c = inputs[2]
d = inputs[3]

print('%d%f%c%s' % (a, b, c, d))
print('%d\t%f\t%c\t%s' % (a, b, c, d))
print('%10d%10.6f%10c%10s' % (a, b, c, d))