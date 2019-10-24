def func(pedras, joia):
  numPedras = 0
  for i in range(len(pedras)):
    numPedras = numPedras + joia.count(pedras[i])
  print("func(pedras = \"{}\", joia = \"{}\") == {}".format(pedras, joia, numPedras))

pedras = input("Quais são as pedras?")
joia = input("Qual é a joia?")

func(pedras, joia)