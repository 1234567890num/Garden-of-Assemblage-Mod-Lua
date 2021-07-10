import sys
print('Converter by Num.')
print('Credits to SonicShadowSilver2 for GoA, Valaxor for Randomizer, and TopazTK for LuaBackend.')
print('Special thanks to OpenKH for documentation, Tommadness for guidance,')
print('Jmari49, Key, SPTKira, and Tommadness for GoA Lua Early Testing.')
print('CJ2123, SonicShadowSilver2 & Soraalam1 for Converter Early Testing.\n')

#Manage files
try:
    file = sys.argv[1]
except:
    file = input('Enter Filename: ')
try:
    try:
        pnach = open(file,'r',encoding='UTF-8')
    except:
        pnach = open(file+'.pnach','r',encoding='UTF-8')
except:
    print('Error: File Not Found.')
    input('Press Enter to close.')
    sys.exit()

lua = open(file+'.lua','w',encoding='UTF-8')

#Write some initial variables
lua.write('function _OnInit()\n')
lua.write('if GAME_ID == 0xF266B00B or GAME_ID == 0xFAF99301 then\n')
lua.write("\tPlatform = 'PS2'\n")
lua.write('\tNow  = 0x032BAE0\n')
lua.write('\tSave = 0x032BB30\n')
lua.write('\tSys3 = 0x1CCB300\n')
lua.write('\tBtl0 = 0x1CE5D80\n')
lua.write("elseif ENGINE_TYPE == 'BACKEND' then\n")
lua.write("\tPlatform = 'PC'\n")
lua.write('\tNow  = 0x0714DB8 - 0x56450E\n')
lua.write('\tSave = 0x09A7070 - 0x56450E\n')
lua.write('\tSys3 = 0x2A59DB0 - 0x56450E\n')
lua.write('\tBtl0 = 0x2A74840 - 0x56450E\n')
lua.write('end\nend\n\n')
lua.write('function _OnFrame()\n')

def day5():
    lua.write('--Shorter Day 5\n')
    lua.write('if ReadShort(Now+0) == 0x0B02 and ReadShort(Now+8) == 0x0C then\n')
    lua.write('\tWriteShort(Save+0x034C,0x02)\n')
    lua.write('\tWriteShort(Save+0x0350,0x0D)\n')
    lua.write('\tWriteShort(Save+0x0356,0x13)\n')
    lua.write('\tWriteShort(Save+0x0358,0x03)\n')
    lua.write('\tWriteShort(Save+0x035C,0x01)\n')
    lua.write('\tWriteShort(Save+0x03E8,0x03)\n')
    lua.write('\tWriteShort(Save+0x03EC,0x00)\n')
    lua.write('\tWriteByte(Save+0x2394,0x1E)\n')
    lua.write('\tWriteShort(Save+0x2110,0x00)\n')
    lua.write('\tWriteByte(Save+0x1CDD,ReadByte(Save+0x1CDD)|0xC0)\n')
    lua.write('\tWriteByte(Save+0x1CDE,ReadByte(Save+0x1CDE)|0x07)\n')
    lua.write('\tWriteByte(Save+0x1CEF,ReadByte(Save+0x1CEF)|0x80)\n')
    lua.write('end\n\n')

def oogie():
    lua.write('--Oogie Boogie HP Barrier Removal\n')
    lua.write('if ReadShort(Now+0) == 0x090E and ReadShort(Now+8) == 0x37 then\n')
    lua.write("\tif Platform == 'PS2' then\n")
    lua.write('\t\tWriteInt(0x1C6C4F0,0)\n')
    lua.write('\t\tWriteInt(0x1C6C288,0)\n')
    lua.write('\t\tWriteInt(0x1C6C020,0)\n')
    lua.write("\telseif Platform == 'PC' then\n")
    lua.write('\t\tWriteInt(0x2A209E8-0x56450E,0)\n')
    lua.write('\t\tWriteInt(0x2A20770-0x56450E,0)\n')
    lua.write('\t\tWriteInt(0x2A204F8-0x56450E,0)\n')
    lua.write('\tend\n')
    lua.write('end\n\n')

def gift():
    lua.write('--Fast Gift Wrapping\n')
    lua.write("if Platform == 'PS2' then\n")
    lua.write('\tObj0 = 0x1C94100\n')
    lua.write("elseif Platform == 'PC' then\n")
    lua.write('\tObj0 = 0x2A22B90 - 0x56450E\n')
    lua.write('end\n')
    lua.write("WriteString(Obj0+0xED70,'F_NM170_XL')\n")
    lua.write("WriteString(Obj0+0xED90,'F_NM170_XL.mset')\n")
    lua.write("WriteString(Obj0+0xEDD0,'F_NM170_XL')\n")
    lua.write("WriteString(Obj0+0xEDF0,'F_NM170_XL.mset')\n")
    lua.write("WriteString(Obj0+0xEE30,'F_NM170_XL')\n")
    lua.write("WriteString(Obj0+0xEE50,'F_NM170_XL.mset')\n\n")

def dash():
    lua.write('--Start with Dash\n')
    lua.write('WriteShort(Btl0+0x31A6C,0x0000820E)\n')
    lua.write('if ReadShort(Now+0) == 0x030A then\n')
    lua.write("\tif Platform == 'PS2' then\n")
    lua.write('\t\tWriteShort(0x1C567C4,0x1E)\n')
    lua.write('\t\tWriteShort(0x1C567C8,0x00)\n')
    lua.write('\t\tif ReadShort(Now+8) == 0x3E then WriteByte(0x035DE08,1) end\n')
    lua.write("\telseif Platform == 'PC' then\n")
    lua.write('\t\tWriteShort(0x29EACA4-0x56450E,0x1E)\n')
    lua.write('\t\tWriteShort(0x29EACA8-0x56450E,0x00)\n')
    lua.write('\t\tif ReadShort(Now+8) == 0x3E then WriteByte(0x0B6275C-0x56450E,1) end\n')
    lua.write('\tend\n')
    lua.write('end\n\n')

def hyenas():
    lua.write('--Fast Hyenas II\n')
    lua.write('if ReadShort(Now+0) == 0x050A and ReadShort(Now+8) == 0x39 then\n')
    lua.write("\tif Platform == 'PS2' then\n")
    lua.write('\t\tWriteInt(0x1C4EDB4,0)\n')
    lua.write('\t\tWriteInt(0x1C4EDF4,0)\n')
    lua.write('\t\tif ReadInt(0x1D48EFC) == 135 then WriteInt(0x1D48EFC,236) end\n')
    lua.write("\telseif Platform == 'PC' then\n")
    lua.write('\t\tWriteInt(0x29E32A0-0x56450E,0)\n')
    lua.write('\t\tWriteInt(0x29E32E0-0x56450E,0)\n')
    lua.write('\t\tif ReadInt(0x2A0D108-0x56450E) == 135 then WriteInt(0x2A0D108-0x56450E,236) end\n')
    lua.write('\tend\n')
    lua.write('end\n\n')

def dragon():
    lua.write('--Skip Dragon Xemnas\n')
    lua.write('if ReadShort(Now+0) == 0x1D12 then\n')
    lua.write("\tif Platform == 'PS2' then\n")
    lua.write('\t\tWriteInt(0x1C4A648,0x5C)\n')
    lua.write("\telseif Platform == 'PC' then\n")
    lua.write('\t\tWriteInt(0x29DEAD8-0x56450E,0x5C)\n')
    lua.write('\tend\n')
    lua.write('end\n\n')

def growth(): #Remove Growth Abilities
    lua.write('--Remove Growth Abilities\n')
    for i in range(35): #Remove Growth Abilities
        value = 0x344A5 + 8*i
        value = hex(value)[2:].upper()
        lua.write('WriteByte(Btl0+0x'+value+',0x00000000)\n')
    lua.write('ValorLv = ReadByte(Save+0x32F6)\n')
    lua.write('WisdmLv = ReadByte(Save+0x332E)\n')
    lua.write('LimitLv = ReadByte(Save+0x3366)\n')
    lua.write('MastrLv = ReadByte(Save+0x339E)\n')
    lua.write('FinalLv = ReadByte(Save+0x33D6)\n')
    lua.write('if ValorLv == 1 or ValorLv == 2 then WriteShort(Save+0x32FC,0x805E)\n')
    lua.write('elseif ValorLv == 3 or ValorLv == 4 then WriteShort(Save+0x32FC,0x805F)\n')
    lua.write('elseif ValorLv == 5 or ValorLv == 6 then WriteShort(Save+0x32FC,0x8060)\n')
    lua.write('elseif ValorLv == 7 then WriteShort(Save+0x32FC,0x8061) end\n')
    lua.write('if WisdmLv == 1 or WisdmLv == 2 then WriteShort(Save+0x3334,0x8062)\n')
    lua.write('elseif WisdmLv == 3 or WisdmLv == 4 then WriteShort(Save+0x3334,0x8063)\n')
    lua.write('elseif WisdmLv == 5 or WisdmLv == 6 then WriteShort(Save+0x3334,0x8064)\n')
    lua.write('elseif WisdmLv == 7 then WriteShort(Save+0x3334,0x8065) end\n')
    lua.write('if LimitLv == 1 or LimitLv == 2 then WriteShort(Save+0x336C,0x8234)\n')
    lua.write('elseif LimitLv == 3 or LimitLv == 4 then WriteShort(Save+0x336C,0x8235)\n')
    lua.write('elseif LimitLv == 5 or LimitLv == 6 then WriteShort(Save+0x336C,0x8236)\n')
    lua.write('elseif LimitLv == 7 then WriteShort(Save+0x336C,0x8237) end\n')
    lua.write('if MastrLv == 1 or MastrLv == 2 then WriteShort(Save+0x33A4,0x8066)\n')
    lua.write('elseif MastrLv == 3 or MastrLv == 4 then WriteShort(Save+0x33A4,0x8067)\n')
    lua.write('elseif MastrLv == 5 or MastrLv == 6 then WriteShort(Save+0x33A4,0x8068)\n')
    lua.write('elseif MastrLv == 7 then WriteShort(Save+0x33A4,0x8069) end\n')
    lua.write('if FinalLv == 1 or FinalLv == 2 then WriteShort(Save+0x33DC,0x806A)\n')
    lua.write('elseif FinalLv == 3 or FinalLv == 4 then WriteShort(Save+0x33DC,0x806B)\n')
    lua.write('elseif FinalLv == 5 or FinalLv == 6 then WriteShort(Save+0x33DC,0x806C)\n')
    lua.write('elseif FinalLv == 7 then WriteShort(Save+0x33DC,0x806D) end\n\n')

pnach = pnach.readlines()
line  = 0
cheat = ['//Shorter Day 5','//Oogie Boogie HP Barrier Removal 1',
         '//Fast Gift Wrapping','// Start with Dash (Lion Sora)',
         '//Fast Hyenas II 1','//Skip Dragon Xemnas',
         '//Remove High Jump LV1','//Remove High Jump MAX 1']
cline = [18,21,10,4,10,8,105,35]

while line < len(pnach):
    data = pnach[line].strip()
    try:
        cnum = cheat.index(data)
        line += cline[cnum]
        if cnum == 0:
            day5()
        elif cnum == 1:
            oogie()
        elif cnum == 2:
            gift()
        elif cnum == 3:
            dash()
        elif cnum == 4:
            hyenas()
        elif cnum == 5:
            dragon()
        elif cnum == 6:
            growth()
        continue
    except:
        pass
    if line == 0:
        lua.write('--Seed: '+data[3:]+'\n')
    elif data != '':
        if data[:2] == '//':
            lua.write('--'+data[2:]+'\n')
        elif data[11] == 'E':
            if data[29:37] == '0032BAE0':
                lua.write('if ReadShort(Now+0) == 0x2002 and ReadShort(Now+8) == 0x01 then ')
                lua.write('WriteShort(Save+0x041A4,0x')
                lua.write(pnach[line+4][34:37])
                lua.write(') end\n')
                line += 5
            else:
                line += int(data[13:15],16)
            continue
        else:
            datype  = 'Write' + ['Byte','Short','Int'][int(data[11])] + '('
            address = int(data[12:19],16)
            value   = ',0x'+data[29:37]
            if address - 0x032BB30 < 0x10FC0: #Save file
                file   = 'Save+'
                offset = address - 0x032BB30
                offset = '0x'+hex(offset)[2:].upper().zfill(5)
            elif address - 0x1CCB300 < 0x1AA68: #03system.bin
                file   = 'Sys3+'
                offset = address - 0x1CCB300
                offset = '0x'+hex(offset)[2:].upper().zfill(5)
            elif address - 0x1CE5D80 < 0x354D0: #00battle.bin
                file   = 'Btl0+'
                offset = address - 0x1CE5D80
                offset = '0x'+hex(offset)[2:].upper().zfill(5)
            lua.write(datype+file+offset+value+')\n')
    line += 1

lua.write('end\n')
lua.close()
print('Converted!')
input('Press Enter to close.')
