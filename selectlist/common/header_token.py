import yaml
import os


class YamlHander:
    def __init__(self, filename='E:\\pypro\\APItest2\\selectlist\\common\\token.yml'):
        self.filename = filename

    # def write_yaml(token):
    #     t_data = {"token": token}
    #     with open("../common/token.yml", "w", encoding="utf-8") as f:
    #         yaml.dump(data=t_data, stream=f, allow_unicode=True)

    def read_yaml(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        tokenid = result["token"]
        print(tokenid)
        return tokenid


if __name__ == '__main__':
    # file_path = os.path.join(os.path.dirname(os.path.abspath("__file__")), r"token.yml")
    # tokens = YamlHander().read_yaml()
    # print(tokens)
    YamlHander().read_yaml()


