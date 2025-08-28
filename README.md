# Barcode Generator Application

## Overview
The Barcode Generator Application is a Python-based GUI tool developed using Tkinter and PIL (Pillow) libraries. It allows users to generate barcodes (EAN13, Code128, Code39) with customizable text inputs such as product name, price, and count. The application supports Persian text rendering using the Arial font and handles Arabic/Persian text direction correctly with `arabic_reshaper` and `bidi`. Generated barcodes can be displayed on the GUI and saved as PNG or JPEG files.

## Features
- **Barcode Types**: Supports EAN13, Code128, and Code39 barcode formats.
- **Custom Inputs**: Users can input a code, product name, price, and count to be displayed on the barcode image.
- **Persian Language Support**: Properly displays Persian text with correct text direction and font rendering.
- **Image Output**: Barcodes are generated as high-quality images (300 DPI) and can be saved in PNG or JPEG formats.
- **User-Friendly Interface**: A clean Tkinter-based GUI with input validation and error handling.

## Requirements
To run the application, you need the following Python libraries:
- `tkinter` (usually included with Python)
- `Pillow` (PIL fork)
- `python-barcode`
- `arabic_reshaper`
- `python-bidi`

Install the dependencies using pip:
```bash
pip install Pillow python-barcode arabic_reshaper python-bidi
```

Additionally, ensure the Arial font (`arial.ttf`) is installed on your system for proper Persian text rendering.

## Usage
1. Run the script (`4.py`) using Python 3.x.
2. Enter the barcode code, select the barcode type (EAN13, Code128, or Code39), and provide optional details like product name, price, and count.
3. Click "Generate Barcode" to create and display the barcode image.
4. Click "Save Image" to save the generated barcode as a PNG or JPEG file.

## File Structure
- `4.py`: The main Python script containing the Barcode Generator Application code.

## Notes
- The application requires the Arial font to render Persian text correctly. If Arial is not found, an error message will be displayed, and the program will exit.
- Ensure the input code matches the selected barcode type's requirements (e.g., EAN13 requires exactly 12 numeric digits).
- The generated barcode image is 300x700 pixels, with the barcode centered and text details displayed below it.

## License
This project is licensed under the MIT License.

---

# برنامه تولیدکننده بارکد

## بررسی اجمالی
برنامه تولیدکننده بارکد یک ابزار گرافیکی مبتنی بر پایتون است که با استفاده از کتابخانه‌های Tkinter و PIL (Pillow) توسعه یافته است. این برنامه به کاربران امکان می‌دهد بارکدهایی (EAN13، Code128، Code39) با ورودی‌های متنی قابل تنظیم مانند نام محصول، قیمت و تعداد تولید کنند. این برنامه از نمایش متن پارسی با استفاده از فونت Arial پشتیبانی می‌کند و جهت‌گیری صحیح متن عربی/پارسی را با استفاده از `arabic_reshaper` و `bidi` مدیریت می‌کند. بارکدهای تولید شده می‌توانند در رابط کاربری نمایش داده شوند و به‌صورت فایل‌های PNG یا JPEG ذخیره شوند.

## ویژگی‌ها
- **انواع بارکد**: پشتیبانی از فرمت‌های بارکد EAN13، Code128 و Code39.
- **ورودی‌های سفارشی**: کاربران می‌توانند کد، نام محصول، قیمت و تعداد را برای نمایش روی تصویر بارکد وارد کنند.
- **پشتیبانی از زبان پارسی**: نمایش صحیح متن پارسی با جهت‌گیری مناسب و رندر فونت.
- **خروجی تصویر**: بارکدها به‌صورت تصاویر با کیفیت بالا (300 DPI) تولید شده و می‌توانند در فرمت‌های PNG یا JPEG ذخیره شوند.
- **رابط کاربری ساده**: رابط کاربری مبتنی بر Tkinter با اعتبارسنجی ورودی و مدیریت خطاها.

## پیش‌نیازها
برای اجرای برنامه، به کتابخانه‌های پایتون زیر نیاز دارید:
- `tkinter` (معمولاً همراه با پایتون ارائه می‌شود)
- `Pillow` (شاخه‌ای از PIL)
- `python-barcode`
- `arabic_reshaper`
- `python-bidi`

نصب وابستگی‌ها با استفاده از pip:
```bash
pip install Pillow python-barcode arabic_reshaper python-bidi
```

همچنین، اطمینان حاصل کنید که فونت Arial (`arial.ttf`) روی سیستم شما نصب شده است تا متن پارسی به درستی نمایش داده شود.

## نحوه استفاده
1. اسکریپت (`4.py`) را با استفاده از پایتون 3.x اجرا کنید.
2. کد بارکد را وارد کرده، نوع بارکد (EAN13، Code128 یا Code39) را انتخاب کنید و جزئیات اختیاری مانند نام محصول، قیمت و تعداد را وارد کنید.
3. روی دکمه "تولید بارکد" کلیک کنید تا تصویر بارکد ایجاد و نمایش داده شود.
4. روی دکمه "ذخیره تصویر" کلیک کنید تا بارکد تولید شده به‌صورت فایل PNG یا JPEG ذخیره شود.

## ساختار فایل
- `4.py`: اسکریپت اصلی پایتون حاوی کد برنامه تولیدکننده بارکد.

## نکات
- این برنامه برای نمایش صحیح متن پارسی به فونت Arial نیاز دارد. اگر فونت Arial یافت نشود، پیام خطایی نمایش داده شده و برنامه بسته می‌شود.
- اطمینان حاصل کنید که کد ورودی با الزامات نوع بارکد انتخاب شده مطابقت دارد (مثلاً EAN13 نیاز به دقیقاً 12 رقم عددی دارد).
- تصویر بارکد تولید شده 300x700 پیکسل است، با بارکد در مرکز و جزئیات متنی در زیر آن نمایش داده می‌شود.

## مجوز
این پروژه تحت مجوز MIT منتشر شده است.

---

# 条形码生成器应用程序

## 概述
条形码生成器应用程序是一个基于 Python 的图形用户界面工具，使用 Tkinter 和 PIL (Pillow) 库开发。它允许用户生成条形码（EAN13、Code128、Code39），并支持自定义文本输入，例如产品名称、价格和数量。该应用程序支持使用 Arial 字体渲染波斯语文本，并通过 `arabic_reshaper` 和 `bidi` 正确处理阿拉伯语/波斯语文本方向。生成的条形码可以在图形界面上显示，并保存为 PNG 或 JPEG 文件。

## 功能
- **条形码类型**：支持 EAN13、Code128 和 Code39 条形码格式。
- **自定义输入**：用户可以输入代码、产品名称、价格和数量以显示在条形码图像上。
- **波斯语支持**：正确显示波斯语文本，包含适当的文本方向和字体渲染。
- **图像输出**：条形码生成高质量图像（300 DPI），并可以保存为 PNG 或 JPEG 格式。
- **用户友好界面**：基于 Tkinter 的简洁图形界面，包含输入验证和错误处理。

## 要求
运行该应用程序需要以下 Python 库：
- `tkinter`（通常随 Python 一起提供）
- `Pillow`（PIL 的分支）
- `python-barcode`
- `arabic_reshaper`
- `python-bidi`

使用 pip 安装依赖项：
```bash
pip install Pillow python-barcode arabic_reshaper python-bidi
```

另外，确保系统中安装了 Arial 字体 (`arial.ttf`)，以正确渲染波斯语文本。

## 使用方法
1. 使用 Python 3.x 运行脚本 (`4.py`)。
2. 输入条形码代码，选择条形码类型（EAN13、Code128 或 Code39），并提供可选的详细信息，如产品名称、价格和数量。
3. 点击“生成条形码”按钮以创建并显示条形码图像。
4. 点击“保存图像”按钮以将生成的条形码保存为 PNG 或 JPEG 文件。

## 文件结构
- `4.py`：包含条形码生成器应用程序代码的主 Python 脚本。

## 注意事项
- 该应用程序需要 Arial 字体来正确渲染波斯语文本。如果未找到 Arial 字体，将显示错误消息并退出程序。
- 确保输入的代码符合所选条形码类型的要求（例如，EAN13 需要正好 12 个数字）。
- 生成的条形码图像为 300x700 像素，条形码居中，文本详细信息显示在其下方。

## 许可证
本项目采用 MIT 许可证发布。