input_file = '港澳电视源.txt'
output_file = '港澳电视源.m3u'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile
    outfile.write(#EXTM3Un)
    for line in infile
        if ',' in line
            name, url = line.strip().split(',')
            outfile.write(f'#EXTINF-1 tvg-id={name} group-title=港澳,{name}n')
            outfile.write(f'{url}n')