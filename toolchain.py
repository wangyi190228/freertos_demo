import os
import sys

# toolchains options
# ARCH = 'arm'
# CPU = 'cortex-m3'
ARCH = 'PC'
CPU = 'generic'

PLATFORM = 'gcc'
EXEC_PATH = sys.executable[0:2] + '/work_tools/arm_gcc/bin'
BUILD = 'debug'

if PLATFORM == 'gcc':
    # toolchains
    # PREFIX = 'arm-none-eabi-'
    PREFIX = ''
    CC = PREFIX + 'gcc'
    AS = PREFIX + 'gcc'
    AR = PREFIX + 'ar'
    CXX = PREFIX + 'g++'
    LINK = PREFIX + 'gcc'
    # TARGET_EXT = 'elf'
    SIZE = PREFIX + 'size'
    OBJDUMP = PREFIX + 'objdump'
    OBJCPY = PREFIX + 'objcopy'

    DEVICE = '-mtune=generic'
    # DEVICE = ' -mcpu=cortex-m3 -mthumb -ffunction-sections -fdata-sections'
    CFLAGS = DEVICE + ' -Dgcc'
    # AFLAGS = ' -c' + DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '
    # LFLAGS = DEVICE + ' -Wl,--gc-sections,-Map=rt-thread.map,-cref,-u,Reset_Handler -T board/linker_scripts/link.lds'
    AFLAGS = ' -c' + DEVICE + ' -x assembler-with-cpp -Wa '
    LFLAGS = 'C:/Windows/System32/winmm.dll',

    if BUILD == 'debug':
        CFLAGS += ' -O0 -gdwarf-2 -g'
        AFLAGS += ' -gdwarf-2'
    else:
        CFLAGS += ' -O2'

    CXXFLAGS = CFLAGS
    # POST_ACTION = OBJCPY + ' -O binary $TARGET rtthread.bin\n' + SIZE + ' $TARGET \n'
