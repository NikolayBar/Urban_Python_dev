import inspect
from module_11 import exsample_11_03

def get_signature(obj):
    try:
        return inspect.signature(obj)
    except (ValueError, TypeError):
        doc_str = inspect.getdoc(obj)
        doc_str = doc_str.split('\n')
        return doc_str[0] + '...'


def introspection_info(obj=None):
    obj_list = [x for x in dir(obj) if not x.startswith('__')]

    for obj_name in obj_list:
        ob = getattr(obj, obj_name)
        if inspect.ismodule(ob):
            sig = get_signature(ob)
            print(f'модуль  {obj_name},   info: {sig}')
        elif inspect.isfunction(ob):
            sig = get_signature(ob)
            print(f'функция {obj_name}, params: {sig}')
        elif inspect.isbuiltin(ob):
            sig = get_signature(ob)
            print(f'{obj_name} (builtin), {sig}')
        elif inspect.isclass(ob):
            sig = get_signature(ob)
            print(f'класс {obj_name}, params: {sig}')
        else:
            print(f'{obj_name}, {type(ob)}')

if __name__ == '__main__':
    obj = exsample_11_03
    introspection_info(obj)
