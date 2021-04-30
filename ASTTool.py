import copy

# 生成统一的node格式，方便传输
def make_node(name: str, attrs_dict: dict):
    result = dict()
    result['name'] = name
    result['attrs'] = attrs_dict
    return result

# 删除包围string的单引号, 如果有
def del_single_quo(string: str):
    if len(string) >= 3 and string[0] == "\'" and string[-1] == "\'":
        return string[1:-1]
    else:
        return string

#整理并生成重定向语句的node
def make_redirect_node(redirect_tok: str):
    node = make_node('redirect',
                    {
                        'type': int(), # 0是重定向输入，1是重定向输出，2是追加输出
                        'from': str(),
                        'to': str()
                    })
    tok = copy.copy(redirect_tok)
    if tok[0].isnumeric():  # 指定了被重定向源，而且一定是重定向输出
        node['attrs']['from'] = copy.copy(tok[0])
        tok = tok[1:] # 截掉被重定向源，方便统一处理

    # 判断重定向类型
    if tok[0] == '>':
        re_type = 1 if (tok[1] != '>') else 2
        node['attrs']['type'] = re_type
        tok = tok[re_type:] # 截掉重定向符号
    else:
        node['attrs']['type'] = 0
        tok = tok[1:] # 截掉重定向符号

    # 剩下的tok必然是to
    node['attrs']['to'] = copy.copy(del_single_quo(tok))
    return node

    


if __name__ == '__main__':
    a = make_node('a', {'a1': 'a11', 'a2': 'a22'})
    print(a)
    b = make_node('b', {'b1': 'b11', 'b2': 'b22'})
    print(b)
    print(a)

    print(del_single_quo("'good '?' morning!'"))
    
    redirect_tok = "2>>'file'"
    print(redirect_tok)
    print(make_redirect_node(redirect_tok))