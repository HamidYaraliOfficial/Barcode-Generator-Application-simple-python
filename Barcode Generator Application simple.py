import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
from io import BytesIO
import barcode
from barcode.writer import ImageWriter
import arabic_reshaper
from bidi.algorithm import get_display

class BarcodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("تولیدکننده بارکد") # Barcode Generator
        master.geometry("500x800") # Adjust overall window size
        #master.resizable(False, False)

        self.current_barcode_pil_img = None # To hold the generated PIL image

        self._load_persian_font() # Load font for PIL
        self._setup_styles() # Configure Tkinter styles
        self._setup_widgets()

    def _load_persian_font(self):
        """Attempts to load Arial font for Persian text."""
        font_path = "arial.ttf"  # Explicitly use Arial for Persian support
        
        try:
            self.font_persian_large = ImageFont.truetype(font_path, 28)
            self.font_persian_medium = ImageFont.truetype(font_path, 20)
            self.font_persian_small = ImageFont.truetype(font_path, 16)
            print(f"Loaded font: Arial")  # Debugging info
        except IOError:
            messagebox.showerror(
                "خطای فونت",
                f"فونت Arial ('{font_path}') یافت نشد. "
                "لطفاً اطمینان حاصل کنید که فونت Arial روی سیستم شما نصب است. "
                "برنامه نمی‌تواند بدون فونت مناسب ادامه دهد."
            )
            self.font_persian_large = None
            self.font_persian_medium = None
            self.font_persian_small = None
            raise Exception("Arial font not found. Please ensure Arial is installed.")

    def _setup_styles(self):
        """Configure Tkinter styles to use Arial for Persian text."""
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 10), anchor="e")  # Right-align labels
        style.configure("TButton", font=("Arial", 10))
        style.configure("TCombobox", font=("Arial", 10))
        style.configure("TEntry", font=("Arial", 10))
        style.configure("TLabelframe.Label", font=("Arial", 10))

    def _setup_widgets(self):
        # Input Frame
        input_frame = ttk.LabelFrame(self.master, text="اطلاعات بارکد", labelanchor="ne") # Barcode Information
        input_frame.pack(pady=10, padx=10, fill="x")

        # Code
        ttk.Label(input_frame, text=":کد", anchor="e").grid(row=0, column=1, sticky="e", padx=5, pady=2) # Code
        self.code_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.code_var, width=40, justify="right").grid(row=0, column=0, padx=5, pady=2, sticky="e")

        # Barcode Type
        ttk.Label(input_frame, text=":نوع بارکد", anchor="e").grid(row=1, column=1, sticky="e", padx=5, pady=2) # Barcode Type
        self.barcode_type_var = tk.StringVar()
        self.barcode_types = ["EAN13", "Code128", "Code39"]
        self.barcode_combobox = ttk.Combobox(input_frame, textvariable=self.barcode_type_var, values=self.barcode_types, state="readonly", width=38, justify="right")
        self.barcode_combobox.grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.barcode_combobox.set(self.barcode_types[0]) # Default selection

        # Name
        ttk.Label(input_frame, text=":نام محصول", anchor="e").grid(row=2, column=1, sticky="e", padx=5, pady=2) # Product Name
        self.name_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.name_var, width=40, justify="right").grid(row=2, column=0, padx=5, pady=2, sticky="e")

        # Price
        ttk.Label(input_frame, text=":قیمت", anchor="e").grid(row=3, column=1, sticky="e", padx=5, pady=2) # Price
        self.price_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.price_var, width=40, justify="right").grid(row=3, column=0, padx=5, pady=2, sticky="e")

        # Count
        ttk.Label(input_frame, text=":تعداد", anchor="e").grid(row=4, column=1, sticky="e", padx=5, pady=2) # Count
        self.count_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.count_var, width=40, justify="right").grid(row=4, column=0, padx=5, pady=2, sticky="e")

        
        # Buttons
        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=5, padx=10, fill="x")

        generate_btn = ttk.Button(button_frame, text="تولید بارکد", command=self.generate_barcode_image) # Generate Barcode
        generate_btn.pack(side="left", padx=5, expand=True, fill="x")

        save_btn = ttk.Button(button_frame, text="ذخیره تصویر", command=self.save_barcode_image) # Save Image
        save_btn.pack(side="right", padx=5, expand=True, fill="x")

        # Barcode Image Display
        self.image_label = ttk.Label(self.master, borderwidth=2, relief="groove")
        self.image_label.pack(pady=10, padx=10)
        # Create a placeholder image
        placeholder = Image.new('RGB', (300, 700), color=(230, 230, 230))
        draw = ImageDraw.Draw(placeholder)
        placeholder_text = arabic_reshaper.reshape("بارکد اینجا نمایش داده می‌شود")
        placeholder_text = get_display(placeholder_text)
        draw.text((150, 350), placeholder_text, fill=(100, 100, 100), anchor="mm", font=self.font_persian_medium) # Barcode will be displayed here
        self.current_barcode_pil_img = placeholder # Store placeholder initially
        self._display_image(placeholder)

    def _display_image(self, pil_image):
        """Converts a PIL Image to ImageTk.PhotoImage and displays it."""
        img_tk = ImageTk.PhotoImage(pil_image)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk # Keep a reference!

    def generate_barcode_image(self):
        code = self.code_var.get()
        btype = self.barcode_type_var.get()
        name = self.name_var.get()
        price = self.price_var.get()
        count = self.count_var.get()

        if not code or not btype:
            messagebox.showwarning("ورودی ناقص", "لطفاً کد و نوع بارکد را وارد کنید.") # Incomplete Input, Please enter code and barcode type.
            return

        try:
            # Barcode specific validation
            if btype == "EAN13":
                if not code.isdigit() or len(code) != 12:
                    messagebox.showwarning("خطای EAN13", "کد EAN13 باید دقیقاً 12 رقم عددی باشد.") # EAN13 Error, EAN13 code must be exactly 12 numeric digits.
                    return
            elif btype == "Code39" and not all(c.isalnum() or c in '-.$/+%' for c in code):
                 messagebox.showwarning("خطای Code39", "کد Code39 می‌تواند شامل اعداد، حروف و نمادهای خاص (-.$/+%) باشد.") # Code39 Error, Code39 can include numbers, letters, and special symbols (-.$/+%).
                 return
            elif btype == "Code128" and not all(ord(c) >= 32 and ord(c) <= 126 for c in code):
                 messagebox.showwarning("خطای Code128", "کد Code128 می‌تواند شامل کاراکترهای ASCII از 32 تا 126 باشد.") # Code128 Error, Code128 can include ASCII characters from 32 to 126.
                 return

            # Generate actual barcode image using python-barcode
            BarcodeClass = barcode.get_barcode_class(btype)
            barcode_instance = BarcodeClass(code, writer=ImageWriter())

            # Buffer to store the barcode image temporarily
            fp = BytesIO()
            barcode_instance.write(fp, options={
                'module_height': 10.0, # Adjust height for better fit
                'text_distance': 5.0,  # Distance between barcode and text (if any generated by barcode lib)
                'font_size': 14,       # Font size for code text below barcode
                'quiet_zone': 10,      # Quiet zone around the barcode
                'dpi': 300             # Higher DPI for better quality
            })
            fp.seek(0) # Rewind the buffer
            raw_barcode_img = Image.open(fp).convert("RGBA")

            # Create the final combined image (300x700)
            final_img = Image.new('RGB', (300, 700), color=(255, 255, 255))
            draw = ImageDraw.Draw(final_img)

            # Resize barcode image to fit
            barcode_max_width = 280 # Slightly less than 300 to leave padding
            barcode_max_height = 200 # Max height for the barcode itself

            # Calculate aspect ratio and resize while maintaining it
            original_width, original_height = raw_barcode_img.size
            if original_width > barcode_max_width or original_height > barcode_max_height:
                ratio = min(barcode_max_width / original_width, barcode_max_height / original_height)
                barcode_width = int(original_width * ratio)
                barcode_height = int(original_height * ratio)
            else:
                barcode_width = original_width
                barcode_height = fifth
            resized_barcode_img = raw_barcode_img.resize((barcode_width, barcode_height), Image.LANCZOS)

            # Calculate positions
            x_center = final_img.width // 2
            y_pos = 30 # Initial Y position

            # Paste barcode
            barcode_x = x_center - (resized_barcode_img.width // 2)
            final_img.paste(resized_barcode_img, (barcode_x, y_pos), resized_barcode_img if resized_barcode_img.mode == 'RGBA' else None) # Use mask if RGBA

            y_pos += barcode_height + 25 # Move down after barcode

            # Add text details
            text_color = (0, 0, 0) # Black

            # Code
            text_to_draw = f"کد: {code}"
            reshaped_text = arabic_reshaper.reshape(text_to_draw)
            bidi_text = get_display(reshaped_text)
            draw.text((x_center, y_pos), bidi_text, font=self.font_persian_medium, fill=text_color, anchor="mm")
            # Calculate height for next item
            bbox = draw.textbbox((x_center, y_pos), bidi_text, font=self.font_persian_medium, anchor="mm")
            text_height = bbox[3] - bbox[1]
            y_pos += text_height + 15

            # Name
            text_to_draw = f"نام: {name}"
            reshaped_text = arabic_reshaper.reshape(text_to_draw)
            bidi_text = get_display(reshaped_text)
            draw.text((x_center, y_pos), bidi_text, font=self.font_persian_medium, fill=text_color, anchor="mm")
            bbox = draw.textbbox((x_center, y_pos), bidi_text, font=self.font_persian_medium, anchor="mm")
            text_height = bbox[3] - bbox[1]
            y_pos += text_height + 15

            # Price
            text_to_draw = f"قیمت: {price}"
            reshaped_text = arabic_reshaper.reshape(text_to_draw)
            bidi_text = get_display(reshaped_text)
            draw.text((x_center, y_pos), bidi_text, font=self.font_persian_medium, fill=text_color, anchor="mm")
            bbox = draw.textbbox((x_center, y_pos), bidi_text, font=self.font_persian_medium, anchor="mm")
            text_height = bbox[3] - bbox[1]
            y_pos += text_height + 15

            # Count
            text_to_draw = f"تعداد: {count}"
            reshaped_text = arabic_reshaper.reshape(text_to_draw)
            bidi_text = get_display(reshaped_text)
            draw.text((x_center, y_pos), bidi_text, font=self.font_persian_medium, fill=text_color, anchor="mm")
            bbox = draw.textbbox((x_center, y_pos), bidi_text, font=self.font_persian_medium, anchor="mm")
            text_height = bbox[3] - bbox[1]
            y_pos += text_height + 15

            self.current_barcode_pil_img = final_img
            self._display_image(final_img)

        except barcode.errors.BarcodeError as e:
            messagebox.showerror("خطای بارکد", f"خطا در تولید بارکد: {e}\nلطفاً از فرمت صحیح کد برای نوع بارکد انتخاب شده اطمینان حاصل کنید.") # Barcode Error, Error generating barcode... Please ensure correct code format for selected barcode type.
        except Exception as e:
            messagebox.showerror("خطا", f"خطایی رخ داد: {e}") # Error, An error occurred.

    def save_barcode_image(self):
        if self.current_barcode_pil_img is None:
            messagebox.showwarning("ذخیره تصویر", "ابتدا یک بارکد تولید کنید.") # Save Image, Please generate a barcode first.
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")],
            title="ذخیره تصویر بارکد" # Save Barcode Image
        )

        if file_path:
            try:
                self.current_barcode_pil_img.save(file_path)
                messagebox.showinfo("ذخیره شد", f"تصویر بارکد با موفقیت در '{file_path}' ذخیره شد.") # Saved, Barcode image successfully saved to...
            except Exception as e:
                messagebox.showerror("خطای ذخیره", f"خطا در ذخیره تصویر: {e}") # Save Error, Error saving image.

def main():
    root = tk.Tk()
    app = BarcodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()