# minuscule(salut())

def minuscule(fonc):
  def wrapper():
    texte = fonc()
    if not isinstance(texte, str):
      raise TypeError("type non adapté")
    return texte.lower()
  return wrapper

@minuscule
def salut():
  return "Hello G"

salut()


def adresse_pro(fonc):
  def wrapper():
    texte = fonc()
    res = "".join([texte], "@entreprise.com")
    print(res)
    return res
  return wrapper


@adresse_pro
@minuscule

def utilisateur():
    return "Tasnime"

utilisateur()
