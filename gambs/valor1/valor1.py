import re
import wget
import os
import datetime
now = datetime.datetime.now()
class Ator(object):
  """docstring for Autor"""
  def __init__(self, name,nr, pos=-1, segu=-1, segnd=-1):
    self.nome = name
    self.post = pos
    self.seg = segu
    self.segn = segnd
    self.real= nr
  def __repr__(self):
    return (self.nome, self.post, self.seg, self.segn, self.real)
  def  __str__(self):
    return str((self.nome, self.post, self.seg, self.segn, self.real))


# Ideia: ter uma hash pra mapear (nome_instagram => nome real)

# Funcao recebe uma url e retorna um objeto do tipo ator
def ator_from_url(url):
  try:
    ator = re.findall( r'\.com\/(.*)\/', url)[0]
  except:
    return False
  try:
    os.system("rm {}.html".format(ator.nome))  # Impedir que se use arquivo velho e apagar apohs o uso
  except:
    pass
  print("ator :: " + ator)
  try:
    html = open( wget.download(url=url, out=ator+".html" ), 'r').read()
  except:
    with open('atores_removidos', 'a') as f:
      f.write(url+'\n')
    return False
  seguidores = int(re.findall(r'edge_followed_by":\{"count":(\d+)',html)[0])
  posts = int(re.findall(r'"edge_owner_to_timeline_media":\{"count":(\d+)',html)[0])
  seguindo = int(re.findall(r'"edge_follow":\{"count":(\d+)',html)[0])
  nomereal = str(re.findall(r'"full_name":"(.+)",',html)[0])
  return Ator(name=ator, pos=posts, segu=seguidores, segnd=seguindo, nr=nomereal)


# Monta a lista de urls usada para extrair as informcoes
def main(debug=False):
  os.system("rm *.html")
  urls = []
  valid_urls = []
  with open('atores_lista', 'r') as fp:
    for i in fp:
      urls.append(i[:-1])  # Retira a quebra de linha
  with open('atores_dados '+now.strftime("%d-%m-%y-%H:%M") +'.csv','w') as fp:
    fp.write('Nome da conta,Nome real da conta,Postagens,Seguidores,Seguindo\n')
    for url in urls:
      ator = ator_from_url(url)
      if ator:
        s = ator.nome +','+str(ator.real) +',' + str(ator.post) + ',' + str(ator.seg)+',' + str(ator.segn)+'\n'
        fp.write(ator.nome + ',' +str(ator.real) +',' + str(ator.post) + ',' + str(ator.seg)+ ','+str(ator.segn) +'\n')
        valid_urls.append(url)
  with open('atores_lista', 'w') as fp:  # Atualizar a lista mantendo APENAS os links validos
    for url in valid_urls:
      fp.write(url+'\n')
  if(not debug): # Nao remover se quiser debugar :)
    os.system("rm *.html")  # Impedir que se use arquivo velho e apagar apohs o uso


# Nao faz sentido: melhor deixar pra debug
# os.system("rm *.html")  # Impedir que se use arquivo velho e apagar apohs o uso
main()
