# fastapi-clean-starter

## 🗂️ 目录结构参考

```
fastapi-clean-starter/
├── backend/
│   ├── core/
│   ├── crud/
│   ├── models/
│   ├── routers/
│   │   ├── v1/
│   │   └── router.py
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 快速开始

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 启动项目：
   ```bash
   uvicorn backend.main:app --reload
   ```
3. 访问接口文档：
   http://127.0.0.1:8000/docs

---