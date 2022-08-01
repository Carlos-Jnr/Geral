import platform
import getpass

from datetime import datetime


print("SO", platform.platform())
print("Versao Python", platform.python_version())

print("User ", getpass.getuser())
print("Data ",datetime.now())