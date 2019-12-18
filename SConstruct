# Some dependent packages
import os.path
import os
import toolchain
# Give a name for the project
tar = 'myapp'
# Application some variables
src = []
path = []
subsrc = []
subsrctype = type(subsrc)
srctype = type(src)

# Set the runtime environment
env = Environment(
    tools=['mingw'],
    AS=toolchain.AS, ASFLAGS=toolchain.AFLAGS,
    CC=toolchain.CC, CCFLAGS=toolchain.CFLAGS,
    AR=toolchain.AR, ARFLAGS='-rc',
    CXX=toolchain.CXX, CXXFLAGS=toolchain.CXXFLAGS,
    LINK=toolchain.LINK, LINKFLAGS=toolchain.LFLAGS,
    CCCOMSTR="Compiling $TARGET", LINKCOMSTR="Linking $TARGET",
)

build_dir = 'build/' + str(env['PLATFORM']) + '/'
# Search all SConscript file
for root, dirs, files in os.walk(str(Dir('#'))):
    for item in files:
        if item == 'SConscript':
            temp = SConscript(os.path.join(
                root, item), variant_dir=build_dir + root, duplicate=0)
            if isinstance(temp, subsrctype):
                subsrc += temp

# Add all h files to CPPPATH and add all c files to src
for item in subsrc:
    if isinstance(item, str):
        path.append(item)
    elif isinstance(item, srctype):
        src += item
# Building
out = env.Program(tar, src, CPPPATH=path)
# env.AddPostAction(tar, toolchain.POST_ACTION)
out_dir = 'out/$PLATFORM/' + str(out[0])
Command(out_dir, out, Move('$TARGET', '$SOURCE'))
