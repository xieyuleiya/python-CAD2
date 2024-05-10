#  ===================
#  @Time :2024/5/10
#  @by   :leilei
#  ===================


import ezdxf
from openpyxl import Workbook


# 从CAD图纸中获取指定图层上的所有圆的中心点坐标和半径
def get_circle_data(file_path, layer_name):
    circle_data = []
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()
    circles = msp.query('CIRCLE[layer=="{}"]'.format(layer_name))

    for circle in circles:
        center = circle.dxf.center
        print("Center point:", center)  # 添加这一行
        center_point = (center[0], center[1])  # 仅考虑X和Y坐标，忽略Z坐标
        radius = circle.dxf.radius
        circle_data.append((center_point, radius))

    return circle_data


# 将圆形数据写入到Excel文件中
def write_to_excel(circle_data, excel_file):
    wb = Workbook()
    ws = wb.active
    ws.append(['Center X', 'Center Y', 'Radius'])

    for center, radius in circle_data:
        ws.append([center[0], center[1], radius])

    wb.save(excel_file)


# 主函数
def main():
    cad_file = '电力平面图布局.dxf'
    excel_file = 'circle_data.xlsx'
    layer_name = '雨水检查井'
    circle_data = get_circle_data(cad_file, layer_name)
    write_to_excel(circle_data, excel_file)


if __name__ == "__main__":
    main()