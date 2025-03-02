# FileConvert Helper

## Descrição
O **FileConvert Helper** é um script em Python que permite identificar o formato de um arquivo e listar as possíveis opções de conversão. Ele suporta formatos comuns de imagens, vídeos, áudios e documentos.

## Funcionalidades
- Identifica a extensão de um arquivo digitado pelo usuário.
- Exibe os formatos disponíveis para conversão.
- Suporte para imagens, vídeos, áudios e documentos.

## Formatos Suportados
### Imagens
- JPEG → PNG, WEBP, BMP, TIFF
- PNG → JPEG, WEBP, BMP, TIFF
- WEBP → JPEG, PNG, BMP, TIFF
- BMP → JPEG, PNG, WEBP, TIFF
- TIFF → JPEG, PNG, WEBP, BMP

### Vídeos
- MP4 → AVI, MKV, MOV, WEBM
- MKV → MP4, AVI, MOV, WEBM
- AVI → MP4, MKV, MOV, WEBM
- MOV → MP4, MKV, AVI, WEBM
- WEBM → MP4, MKV, AVI, MOV

### Áudio
- MP3 → WAV, FLAC, AAC, OGG
- WAV → MP3, FLAC, AAC, OGG
- FLAC → MP3, WAV, AAC, OGG
- AAC → MP3, WAV, FLAC, OGG
- OGG → MP3, WAV, FLAC, AAC

### Documentos
- PDF → DOCX, TXT, EPUB
- DOCX → PDF, TXT, EPUB
- TXT → PDF, DOCX, EPUB
- EPUB → PDF, DOCX, TXT

## Como Usar
1. Certifique-se de ter o Python instalado em seu sistema.
2. Execute o script `file_conversion_options.py`.
3. Digite a extensão do arquivo (sem ponto, por exemplo: `jpeg`, `mp4`, `pdf`).
4. O script exibirá as opções disponíveis para conversão.

## Requisitos
- Python 3.x

## Contribuição
Sinta-se à vontade para sugerir novas funcionalidades ou adicionar mais formatos de conversão!

## Licença
Este projeto é distribuído sob a licença MIT.

