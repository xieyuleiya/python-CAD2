#  ===================
#  @Time :2024/5/10
#  @by   :leilei
#  ===================



import ezdxf
from openpyxl import Workbook

# 读取CAD文件
def read_cad_data(file_path):
    cad_data = []
    doc = ezdxf.readfile(file_path)
    modelspace = doc.modelspace()
    for entity in modelspace:
        if entity.dxftype() == 'LINE':
            start_point = entity.dxf.start
            end_point = entity.dxf.end
            cad_data.append({'Type': 'Line', 'Start': start_point, 'End': end_point})
        # 可以根据需要添加其他类型的实体处理
    return cad_data

# 写入Excel文件
# 写入Excel文件
def write_to_excel(cad_data, excel_file):
    wb = Workbook()
    ws = wb.active
    ws.append(['Type', 'Start X', 'Start Y', 'Start Z', 'End X', 'End Y', 'End Z'])  # 添加表头
    for data in cad_data:
        start_point = data['Start']
        end_point = data['End']
        ws.append([data['Type'], start_point[0], start_point[1], start_point[2],
                   end_point[0], end_point[1], end_point[2]])
    wb.save(excel_file)


# 主函数
def main():
    cad_file = 'try2.dxf'
    excel_file = 'output_excel.xlsx'
    cad_data = read_cad_data(cad_file)
    write_to_excel(cad_data, excel_file)

if __name__ == "__main__":
    main()
