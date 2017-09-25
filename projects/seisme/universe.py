from importlib.machinery import SourceFileLoader
import os
import sys
import io

ORIGIN_PATH = os.getcwd()
os.chdir(os.path.dirname(__file__))
import settings

cd_view_pointMap = SourceFileLoader("plugins.cd_view_pointMap", settings.PLUGINS_PATHS[0] + "/cd_view_pointMap/cd_view_pointMap.py").load_module()
cd_import_csv = SourceFileLoader("plugins.cd_import_csv", settings.PLUGINS_PATHS[0] + "/cd_import_csv/cd_import_csv.py").load_module()

os.chdir(ORIGIN_PATH)

class sing:
    class __sing:
        def __init__(self):
            pass

        def __str__(self):
            return repr(self)

        data = {}
        @cd_import_csv.plugin(0, line_sep = '\n', col_sep = ',', header = True, file = 'earthquake.csv')
        def imp(self, position):
            data = {}
            return [data]

        def proc(self, position, data):
            return data

        @cd_view_pointMap.plugin(0, table = 'earthquake.csv', longitude = 'Longitude', latitude = 'Latitude', popup = '')
        def exp(self, position, data):
            pass

        def run(self, func = ['imp', 'proc', 'exp'], api = "", pos = 0):
            result = {}
            data = []
            for f in func:
                position = -1
                if api == f:
                    position = pos
                out = io.StringIO()
                sys.stdout = out
                if f == 'imp':
                    data = self.imp(position)
                if f == 'proc':
                    data = self.proc(position, data)
                if f == 'exp':
                    data = self.exp(position, data)
                sys.stdout = sys.__stdout__
                result[f] = out.getvalue()
                if api == f:
                    return data
            return {'data': data, '__stdout__': result}

    instance = None

    def __init__(self, refresh=False):
        if not sing.instance or refresh:
            sing.instance = sing.__sing()

    def __getattr__(self, name):
        return getattr(self.instance, name)

singleton = sing()
