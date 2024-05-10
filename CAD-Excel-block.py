#  ===================
#  @Time :2024/5/9
#  @by   :leilei
#  ===================

import ezdxf
from openpyxl import Workbook


# 获取CAD图纸中指定名称的块信息
def get_block_data(file_path, block_name):
    block_data = []
    doc = ezdxf.readfile(file_path)

    # 遍历模型空间中的块实体
    for entity in doc.modelspace():
        if entity.dxftype() == 'INSERT' and entity.dxf.name == block_name:
            block_data.append(entity)

    return block_data


# 将块信息写入Excel文件
def write_to_excel(block_data, excel_file):
    wb = Workbook()
    ws = wb.active
    ws.append(['Layer', 'Color', 'Linetype',  'Insertion Point'])

    for entity in block_data:
        layer = entity.dxf.layer
        color = entity.dxf.color
        linetype = entity.dxf.linetype

        insertion_point = f"{entity.dxf.insert[0]}, {entity.dxf.insert[1]}, {entity.dxf.insert[2]}"
        ws.append([layer, color, linetype,  insertion_point])

    wb.save(excel_file)


# 主函数
def main():
    cad_file = '电力平面图布局.dxf'
    excel_file = 'block_data.xlsx'
    block_name = 'A$C41BB26E9'
    block_data = get_block_data(cad_file, block_name)
    write_to_excel(block_data, excel_file)


if __name__ == "__main__":
    main()

