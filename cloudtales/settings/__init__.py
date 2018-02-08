try:
    from .local_settings import *
except ImportError:
    raise Exception("A local_settings.py file must be present to run this project")

exec("from .%s import *" % local_environment)