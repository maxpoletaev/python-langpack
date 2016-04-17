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


class HjsonLoader(BaseLoader):
    def __init__(self, *args, **kwargs):
        try:
            self.hjson = import_module('hjson')
        except ImportError:
            err = 'Install hjson package for using HjsonLoader or disable this loader.'
            raise ImportError(err)

    def load_contents(self, contents):
        return self.hjson.loads(contents)


class PythonLoader(BaseLoader):
    def __init__(self, module_name='translations', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module_name = module_name

    def load_file(self, file_path):
        module = dict()
        with open(file_path) as f:
            exec(f.read(), module)
        return module[self.module_name]
