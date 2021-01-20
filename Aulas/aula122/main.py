
# redimensionando várias imagens ao mesmo tempo.

import os
from PIL import Image
# instalar o pillow para redimensionar as imagens.
# pip install pillow

def main(main_images_folder, new_width=500):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não exite.')

    for root, dir, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extention = os.path.splitext(file)

            converted_tag = '_CONVERTED'

            new_file = file_name + converted_tag + extention
            new_file_full_path = os.path.join(root, new_file)

            # O codigo a baixo serve para apagar os arquivos que foram redimensionados, caso for utilizar
            # não esqueça de comentar a linha 60.

            #if converted_tag in file_full_path:
            #    os.remove(file_full_path)
            #    continue

            if os.path.isfile(new_file_full_path):
                print(f'Arquivo {new_file_full_path} já existe.')
                continue

            if converted_tag in file_full_path:
                print('Imagem já convertida')
                continue

            img_pillow = Image.open(file_full_path)



            width, height = img_pillow.size
            new_height = round(new_width * height / width)  # a nova altura será baseado na NOVA LARGURA.
            new_image = img_pillow.resize(
                (new_width, new_height),
                Image.LANCZOS
            )

            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=70,  # 1 ruim e 100 otima
                # exif=img_pillow.info['exif']  # migrar os dados da imagem original para a atual.
                # ATENÇÃO: Utilizar o comando a cima se somente existir EXIF
                # print(img_pillow.getexif()) comando para verificar se existe EXIF
            )

            print(f'{file_full_path} convertido com sucesso!')
            new_image.close()
            img_pillow.close()
            os.remove(file_full_path)  # CUIDADO: este código irá apagar os arquivos originais.


if __name__ == '__main__':
    main_images_folder = r'C:\Users\kelvin\Desktop\imagens'
    main(main_images_folder, new_width=400)  # passar o valor da NOVA LARGURA da imagem.
