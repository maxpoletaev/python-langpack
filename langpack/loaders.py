from importlib.machinery import SourceFileLoader
from importlib import import_module


class BaseLoader:
    def load_file(self, file_path):
        with open(file_path, 'r') as fp:
            return self.load_contents(fp.read())

    def load_contents(self, contents):
        raise NotImplementedError()


class JsonLoader(BaseLoader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.json = import_module('json')

    def load_contents(self, contents):
        return self.json.loads(contents)


class YamlLoader(BaseLoader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            self.yaml = import_module('yaml')
        except ImportError:
            err = 'Install pyyaml package for using YamlLoader or disable this loader.'
            raise ImportError(err)

    def load_contents(self, contents):
        return self.yaml.load(contents)


class PythonLoader(BaseLoader):
    def __init__(self, module_name='export', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module_name = module_name

    def load_file(self, file_path):
        return SourceFileLoader(self.module_name, file_path)
