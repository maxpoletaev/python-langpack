from langpack.loaders import JsonLoader, YamlLoader, PythonLoader
from nose import tools as test
import tempfile
import os


class TestJsonLoader:
    def setup(self):
        self.loader = JsonLoader()

    def test_load_contents(self):
        contents = self.loader.load_contents('{"key1": "value1"}')
        test.assert_equal(contents, {'key1': 'value1'})


class TestYamlLoader:
    def setup(self):
        self.loader = YamlLoader()

    def test_load_contents(self):
        contents = self.loader.load_contents('key1: value1')
        test.assert_equal(contents, {'key1': 'value1'})


class TestPythonLoader:
    def setup(self):
        self.loader = PythonLoader()

    def create_test_file(self):
        file_path = os.path.join(tempfile.gettempdir(), 'tets_python_loader.py')
        contents = '''translations = {'a': 'a!', 'b': 'b!'}'''
        with open(file_path, 'w') as fp:
            fp.write(contents)
        return file_path

    def test_load_file(self):
        file_path = self.create_test_file()
        result = self.loader.load_file(file_path)
        test.assert_equal(result, {'a': 'a!', 'b': 'b!'})
