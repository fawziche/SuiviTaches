class Utilitaires:
    def estUnFloat (arValue):
        try:
            float(arValue)
            return True
        except Exception as err:
            return False