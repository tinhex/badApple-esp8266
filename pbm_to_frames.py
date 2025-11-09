import glob

def read_pbm_rawbytes(filename):
    with open(filename, 'rb') as f:
        header = f.readline().strip()
        if header != b'P4':
            raise ValueError("Only P4 raw PBM supported")
        while True:
            line = f.readline().strip()
            if not line.startswith(b'#'):
                width, height = map(int, line.split())
                break
        data = f.read()
    if width != 128 or height != 64:
        raise ValueError("Only 128x64 supported")
    if len(data) != 1024:
        raise ValueError(f"Expected 1024 bytes, got {len(data)}")
    return data

def main():
    pbm_files = sorted(glob.glob("pbms/frame*.pbm"))
    if not pbm_files:
        print("No PBM files found!")
        return

    frame_count = len(pbm_files)
    print(f"Converting {frame_count} frames...")

    with open("frames.h", "w") as out:
        out.write("#ifndef FRAMES_H\n#define FRAMES_H\n\n")
        out.write("#include <Arduino.h>\n\n")
        out.write("#define FPS 13\n")
        out.write(f"const uint16_t frameCount = {frame_count};\n\n")

        for idx, fname in enumerate(pbm_files):
            print(f"  {fname}")
            data = read_pbm_rawbytes(fname)
            out.write(f"const uint8_t frame{idx}[] PROGMEM = {{\n  ")
            for i, b in enumerate(data):
                if i > 0 and i % 16 == 0:
                    out.write("\n  ")
                out.write(f"0x{b:02X},")
            out.write("\n};\n\n")

        out.write("const uint8_t* const frames[] PROGMEM = {\n  ")
        for i in range(frame_count):
            if i > 0 and i % 10 == 0:
                out.write("\n  ")
            out.write(f"frame{i}, ")
        out.write("\n};\n\n")
        out.write("#endif // FRAMES_H\n")

    print("✅ Done!")

if __name__ == "__main__":
    main()