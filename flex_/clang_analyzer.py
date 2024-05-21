from clang.cindex import Index

index = Index.create()
file_path = 'easy_main.c'
translation_unit = index.parse(file_path)

for i in translation_unit.get_tokens(extent=translation_unit.cursor.extent):
    print (i.kind)