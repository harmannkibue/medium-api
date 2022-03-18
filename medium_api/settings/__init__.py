from .common import *

try:
    from .local import *
    print(">>> LOCAL SERVER RUNNING")

except Exception as e:
    print(">>> PRODUCTION SERVER RUNNING", e)
    from .production import *
