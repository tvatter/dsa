# languages where classes and functions can’t be passed
# as parameters or stored as attributes

# https://python-patterns.guide/gang-of-four/factory-method/

# https://www.geeksforgeeks.org/factory-method-python-design-patterns/


class FrenchLocalizer:
  """ it simply returns the french version """
  def __init__(self):

    self.translations = {
        "car": "voiture",
        "bike": "bicyclette",
        "cycle": "cyclette"
    }

  def localize(self, message):
    """change the message using translations"""
    return self.translations.get(msg, msg)


class SpanishLocalizer:
  """it simply returns the spanish version"""
  def __init__(self):

    self.translations = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}

  def localize(self, msg):
    """change the message using translations"""
    return self.translations.get(msg, msg)


class EnglishLocalizer:
  """Simply return the same message"""
  def localize(self, msg):
    return msg


def Factory(language="English"):
  """Factory Method"""
  localizers = {
      "French": FrenchLocalizer,
      "English": EnglishLocalizer,
      "Spanish": SpanishLocalizer,
  }

  return localizers[language]()


if __name__ == "__main__":

  f = FrenchLocalizer()
  e = EnglishLocalizer()
  s = SpanishLocalizer()

  message = ["car", "bike", "cycle"]

  for msg in message:
    print(f.localize(msg))
    print(e.localize(msg))
    print(s.localize(msg))

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    for msg in message:
      print(f.localize(msg))
      print(e.localize(msg))
      print(s.localize(msg))
