# PopClip Extension Builder

A simple Python tool to batch generate `.popclipext` extensions from
multiple source folders.

一个简单的 Python 工具，用于从多个源文件夹批量生成 `.popclipext` 插件。

---

## 📁 Project Structure

    OBTEXT/
    ├── Sources/
    │   ├── CN/
    │   │   ├── config.js
    │   │   ├── Config.plist
    │   │   └── obtext.png
    │   ├── International/
    │   │   ├── config.js
    │   │   ├── Config.plist
    │   │   └── obtext.png
    │   ├── Invest/
    │   │   ├── config.js
    │   │   ├── Config.plist
    │   │   └── obtext.png
    ├── Outputs/
    ├── popclip_generate.py
    └── README.md

---

## 🚀 Features

- Automatically scans all subfolders under `Sources/`
- Creates one `.popclipext` extension per folder
- Copies required files:
  - `config.js`
  - `Config.plist`
  - `obtext.png`
- Outputs extensions into `Outputs/`

功能说明：

- 自动扫描 `Sources/` 下所有子文件夹
- 每个子文件夹生成一个 `.popclipext` 插件
- 自动复制以下文件：
  - `config.js`
  - `Config.plist`
  - `obtext.png`
- 输出到 `Outputs/` 目录

---

## ▶️ Usage

### 1️⃣ Prepare source folders

Each subfolder under `Sources/` must contain:

    config.js
    Config.plist
    obtext.png

每个 `Sources/` 子文件夹必须包含以上三个文件，否则插件不完整。

---

### 2️⃣ Run the script

    python3 popclip_generate.py

---

### 3️⃣ Check output

Generated extensions will appear in:

    Outputs/

Example:

    Outputs/
    ├── CN.popclipext
    ├── International.popclipext
    └── Invest.popclipext

You can double-click `.popclipext` files to install them into PopClip.

你可以双击 `.popclipext` 文件直接导入到 PopClip。

---

## ⚠️ Notes

- Existing output folders will be **deleted and recreated**
- Missing files will trigger warnings but will not stop execution
- Extension name is based on the source folder name

注意事项：

- 如果输出目录已存在，会被**删除并重新创建**
- 如果缺少文件，会提示警告，但不会中断程序
- 插件名称自动使用源文件夹名称

---

## 🧠 Design Idea

This tool treats each folder as a **template** and converts it into a
PopClip extension.

核心思路：

将每个文件夹视为一个"模板"，自动构建插件，而不是手动重复创建。

This reduces manual work and ensures consistency.

减少重复劳动，并保证结构一致性。

---

## 🧩 Requirements

- Python 3.x
- macOS (for PopClip usage)

---

## 📦 Future Improvements (Optional)

- Auto zip `.popclipext` for sharing
- Validate config consistency (name / identifier)
- Add logging system
- Add CLI arguments (custom paths)

可扩展方向：

- 自动压缩 `.popclipext` 方便分享
- 校验 config 一致性（名称、identifier）
- 增加日志系统
- 支持命令行参数（自定义路径）

---

## 🏁 Summary

You now have a reusable workflow to build PopClip extensions in batch.

你现在已经拥有一个可复用的 PopClip 插件批量构建流程。
