from xmindparser import xmind_to_dict
import xlwt


def traversal_xmind(root, rootstring, lisitcontainer):
    """
    功能：递归dictionary文件得到容易写入Excel形式的格式。
    注意：rootstring都用str来处理中文字符
    @param root: 将xmind处理后的dictionary文件
    @param rootstring: xmind根标题
    """
    if isinstance(root, dict):
        if 'title' in root.keys() and 'topics' in root.keys():
            traversal_xmind(root['topics'], str(rootstring), lisitcontainer)
        if 'title' in root.keys() and 'topics' not in root.keys():
            traversal_xmind(root['title'], str(rootstring), lisitcontainer)
    elif isinstance(root, list):
        for sonroot in root:
            traversal_xmind(sonroot, str(rootstring) + "&" + sonroot['title'], lisitcontainer)
            if 'makers' in sonroot and 'callout' in sonroot:
                traversal_xmind(sonroot, str(rootstring) + "&" + sonroot['title'] + "&" + str(sonroot['makers'][0]) +
                                "&" + str(sonroot['callout'][0]), lisitcontainer)
            elif 'callout' in sonroot and 'makers' not in sonroot:
                traversal_xmind(sonroot, str(rootstring) + "&" + sonroot['title'] + "&" + str(sonroot['callout'][0]),
                                lisitcontainer)
            elif 'makers' in sonroot and 'callout' not in sonroot:
                traversal_xmind(sonroot, str(rootstring) + "&" + sonroot['title'] + "&" + str(sonroot['makers'][0]),
                                lisitcontainer)

    elif isinstance(root, str):
        # lisitcontainer.append(str(rootstring.replace('\n', '')))  # 此处是去掉一步骤多结果情况直接拼接
        lisitcontainer.append(str(rootstring))  # 此处是一步骤多结果时，多结果合并


def get_case(root):
    rootstring = root['title']
    lisitcontainer = []
    traversal_xmind(root, rootstring, lisitcontainer)
    # for lisitcontaine in lisitcontainer:
    #     print(lisitcontaine)
    return lisitcontainer


def maker_judgment(makers):
    maker = 4
    if '1' in makers:
        maker = "P0"
    elif '2' in makers:
        maker = "P1"
    elif '3' in makers:
        maker = "P2"
    return maker






def write_sheet(b, filename, name, maker, callout, step, result, state):
    worksheet.write(b, 0, filename)  # ，模块
    worksheet.write(b, 1, name)  # 用例名称
    worksheet.write(b, 2, callout)  # 前置条件
    worksheet.write(b, 3, step)  # 用例步骤
    worksheet.write(b, 4, result)  # 预期结果
    worksheet.write(b, 5, maker)  # 优先级
    worksheet.write(b, 6, state)  # 执行结果


def deal_with_list(list):
    '''
    处理从xmind转换过来的用例list，并写入Excel中
    :param list: 传入从xmind转换好的用例列表
    :return:
    '''
    b = 1  # 记录写了多少行
    for i in list:
        j = i.split("&")
        # print(j)
        if 'priority-1' in j or 'priority-2' in j or 'priority-3' in j:
            print(j)
            x = 0
            if 'priority-1' in j:
                x = j.index('priority-1')
            elif 'priority-2' in j:
                x = j.index('priority-2')
            elif 'priority-3' in j:
                x = j.index('priority-3')


            if j[-1] == j[x]:  #前置条件
                result = ""
                step = ""
                callout = ""
            else:
                result = j[-1]
                step = j[-2]
                if j[-2] == j[x + 1]:
                    callout = ""
                else:
                    callout = j[x + 1:x + 2]
            maker = maker_judgment(j[x])
            filename = j[1:x-1]
            # for filename in j[1:x-1]:
            #     filename = filename + '-'
            name = ''
            state = ''
            for a in j[x-1]:
                name += a
            # print(filename, name, maker, callout, step, result)
            write_sheet(b, filename, name.split("#")[0], maker, callout, step, result, state)  # 写入Excel
            b += 1



if __name__ == '__main__':
    #直接在这里换需要转换的文件即可
    root = xmind_to_dict("/Users/timothyfang/Desktop/收益月报.xmind")[0]['topic']
    # root = xmind_to_dict("C:/Users/92495/Desktop/123.xmind")[0]['topic']
    # get_case(root)
    row0 = ["测试模块", '用例名称', '前置条件', '操作步骤', '预期结果','用例级别', '测试环境验证结果']
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet(str(root["title"]), cell_overwrite_ok=True)
    for i in range(len(row0)):
        worksheet.write(0, i, row0[i])

    case = get_case(root)
    deal_with_list(case)
    workbook.save(root["title"] + ".xls")