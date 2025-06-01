# FastAPITemplate4Javaer

本项目是一个面向 Java 开发者的 FastAPI 后端模板，目录结构和分层思想对标主流 Java Web 项目（如 Spring Boot），便于 Javaer 快速上手 Python/FastAPI。适合中小型项目的快速开发和学习。

当前为 blank 分支，仅包含基础分层结构和最小功能示例，未包括认证、数据库、异常处理等其他功能。

## 🗂️ 目录结构与 Java 对应关系

```
FastAPITemplate4Javaer/
├── app/
│   ├── controller/    # 控制器层（对应 Java 的 controller 包）
│   │   └── item_controller.py
│   ├── service/       # 业务逻辑层（对应 Java 的 service 包）
│   │   └── item_service.py
│   ├── model/         # 数据模型层（对应 Java 的 entity/model 包）
│   │   └── item_model.py
│   ├── schemas/       # 数据结构校验（对应 Java 的 DTO/VO）
│   │   └── item_schema.py
│   ├── config/        # 配置（对应 Java 的 config 包）
│   │   └── app_config.py
│   ├── common/        # 通用工具/响应/常量（对应 Java 的 util/common/constant 包）
│   │   └── response.py
│   └── main.py        # 应用入口（对应 Java 的 Application.java）
├── docs/              # 项目文档
├── tests/             # 测试用例
├── requirements.txt   # Python 依赖（对应 Java 的 pom.xml）
└── README.md          # 项目说明
```

## 📝 主要分层说明

- **controller**：接口路由层，处理 HTTP 请求，调用 service 层，返回统一响应。类似 Java 的 Controller。
- **service**：业务逻辑层，处理具体业务，调用 model 层。类似 Java 的 Service。
- **model**：数据模型层，定义实体结构。类似 Java 的 Entity/Model。
- **schemas**：Pydantic 数据校验层，定义请求/响应的数据结构。类似 Java 的 DTO/VO。
- **config**：配置相关，集中管理项目配置。类似 Java 的 config 包或 application.yml。
- **common**：通用工具、统一响应、常量等。类似 Java 的 util/common/constant 包。
- **main.py**：应用启动入口。类似 Java 的 Application.java。

## 🚀 快速开始

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 启动项目：
   ```bash
   uvicorn app.main:app --reload
   ```
3. 访问接口文档：
   http://127.0.0.1:8000/docs

---

如需扩展更多分层（如 repository/dao、middleware、exception、utils 等），可参考 Java 项目分层方式进行补充。
