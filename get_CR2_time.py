# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:28:23 2017

@author: vinicius

O arquivo deve estar na mesma pasta que contem as .CR2
"""

import pyexiv2 #biblioteca para ler a metadata da raw
import glob # biblioteca para listar os arquivos da pasta


FileNames = glob.glob("*.CR2") #lista os arquivos CR2 da pasta local

FileNames.sort() #organiza a lista em ordem alfabetica


i = 0 #contador das fotos

initime = 0 #tempo inicial

clock = []

for f in FileNames:
        metadata = pyexiv2.ImageMetadata(f) #le a metadata
        metadata.read()
        
        tag = metadata['Exif.Image.DateTime'] #pega a tag com a data e horario da foto
        
        clock.append(tag.raw_value)
        
with open(FileNames[0][0:3] + '_time' + '.txt', 'wb') as fout: #cria arquivo com as iniciais do nome das fotos
    s = "{:^10} {:^10} {:^10} {:^10}\n".format("Photo", "Date", "Raw time", "time [s]") #escreve o cabecalho
    fout.write(s)
        
    for c in clock:
        
        time = int(c[8:10])*24*60*60 + int(c[-8:-6])*60*60 + int(c[-5:-3])*60 + int(c[-2:]) #transforma o horario em segundos totais
        
        if i == 0:
            initime = time # salva o tempo inicial para ser descontado abaixo
            

        delta_t = time-initime
        
        l = "{:^10.0f} {:^10} {:^10} {:^10.0f}\n".format(i, c[0:10], c[10:], 
                delta_t) #escreve as informacoes de cada foto em cada linha
        fout.write(l)
        i += 1 # atualiza o contador de fotos
