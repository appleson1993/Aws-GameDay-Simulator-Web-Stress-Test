# GameDay Simulator (SQL Version)

🎮 **AWS GameDay 機制模擬工具**  
此工具模擬 AWS GameDay 中的任務機制，基於 Python 開發，支援 SQL 操作，可跨平台執行。

---

## 🔧 特點 Features

- ✅ 支援 SQL 資料互動
- ✅ 跨平台執行（Linux / macOS / Windows）
- ✅ 單一可執行檔部署（使用 PyInstaller）
- ✅ 適合用於訓練、教學、比賽模擬

---

## 🚀 如何執行 How to Run

### 1. 打包成單一執行檔

請先安裝 [PyInstaller](https://pyinstaller.org/en/stable/):

pip install pyinstaller
接著執行以下指令來產出可執行檔：
pyinstaller --onefile main.py
完成後會在 dist/ 目錄下產生 main 可執行檔案。

2. 在 Linux / macOS 上執行
3. 
請先賦予執行權限並啟動程式：
chmod +x dist/main
./dist/main

3. Windows 用戶
執行 dist/main.exe 即可。

📁 專案結構 Project Structure
├── main.py          # 主程式入口，模擬 GameDay 任務流程
├── requirements.txt # 所需套件列表
└── README.md        # 使用說明文件

📌 備註 Notes
若有需要模擬更多 AWS GameDay 模組，請於 main.py 中擴充任務邏輯。

建議搭配 PostgreSQL 或 SQLite 使用，根據場景可切換資料庫連線設定。

📤 聯絡方式 / Contact
如需協助或回報錯誤，歡迎建立 issue 或聯絡開發者。
