#!/usr/bin/env python3

from PIL import Image, ImageDraw


def safe_int_input(prompt):
    try:
        return int(input(prompt))
    except Exception:
        return None


def main():
    square_size = safe_int_input("Enter square size [70]: ") or 70
    num_rows = safe_int_input("Enter number of rows [50]: ") or 50
    num_cols = safe_int_input("Enter number of columns [50]: ") or 50

    img_x_size = square_size * num_cols
    img_y_size = square_size * num_rows

    print(f"x size: {img_x_size}, y size: {img_y_size}")

    # Create empty image
    img = Image.new(mode="RGB", size=(img_x_size, img_y_size),
                    color=(255, 255, 255))

    # Draw grid
    draw = ImageDraw.Draw(img)
    x, y = 0, 0
    while x < num_cols:
        draw.line((square_size * (x+1), 0,
                   square_size * (x+1), img_y_size), fill=(127, 127, 127))

        x += 1
    while y < num_rows:
        draw.line((0, square_size * (y+1),
                   img_x_size, square_size * (y+1)), fill=(127, 127, 127))

        y += 1

    img.save(f"grid-{num_cols}x{num_rows}.png")


if __name__ == "__main__":
    main()
