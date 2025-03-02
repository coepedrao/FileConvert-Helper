file_conversion_map = {

    "jpeg": ["png", "webp", "bmp", "tiff"],
    "png": ["jpeg", "webp", "bmp", "tiff"],
    "webp": ["jpeg", "png", "bmp", "tiff"],
    "bmp": ["jpeg", "png", "webp", "tiff"],
    "tiff": ["jpeg", "png", "webp", "bmp"],

    "mp4": ["avi", "mkv", "mov", "webm"],
    "mkv": ["mp4", "avi", "mov", "webm"],
    "avi": ["mp4", "mkv", "mov", "webm"],
    "mov": ["mp4", "mkv", "avi", "webm"],
    "webm": ["mp4", "mkv", "avi", "mov"],

    "mp3": ["wav", "flac", "aac", "ogg"],
    "wav": ["mp3", "flac", "aac", "ogg"],
    "flac": ["mp3", "wav", "aac", "ogg"],
    "aac": ["mp3", "wav", "flac", "ogg"],
    "ogg": ["mp3", "wav", "flac", "aac"],

    "pdf": ["docx", "txt", "epub"],
    "docx": ["pdf", "txt", "epub"],
    "txt": ["pdf", "docx", "epub"],
    "epub": ["pdf", "docx", "txt"]
}

file_format = input("Digite a extensão do arquivo (sem ponto, ex: jpeg, mp4, pdf): ").strip().lower()

if file_format in file_conversion_map:
    print(f"O formato '{file_format}' pode ser convertido para: {', '.join(file_conversion_map[file_format])}")
else:
    print(f"Nenhuma opção de conversão disponível para '{file_format}'.")
