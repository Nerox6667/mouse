# Fichier packaging.py de secours complet pour la NSI
class Version:
    def __init__(self, version_str):
        self.version_str = version_str
        self.version = tuple(int(x) for x in version_str.split('.') if x.isdigit())
    def __str__(self): return self.version_str
    def __repr__(self): return f"<Version('{self.version_str}')>"
    def __eq__(self, other): return self.version == other.version
    def __lt__(self, other): return self.version < other.version
    def __le__(self, other): return self.version <= other.version
    def __gt__(self, other): return self.version > other.version
    def __ge__(self, other): return self.version >= other.version

def parse(version_str):
    return Version(version_str)

# Cette ligne manquait pour résoudre l'ImportError
version = sys = type('Module', (), {'parse': parse, 'Version': Version})
