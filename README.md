<div align="center">

# ShowImageWeb

</div>

<div align="center">

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Vercel](https://img.shields.io/badge/Vercel-Ready-black.svg)
![Docker](https://img.shields.io/badge/Docker-20.10+-blue.svg)

</div>

AI图像生成网页交互平台 - 支持 Vercel 一键部署，提供简洁的用户界面和实用的图像生成功能 - **对手机UI界面进行了优化**

## 应用预览

![ShowImageWeb Demo](assets/showimage-web-demo.png)
![ShowImageWeb Demo](assets/showimage-web-demo1.png)

## 项目结构

```
showimageweb/
├── api/
│   └── generate.py          # Vercel Serverless Function (API代理)
├── public/
│   ├── index.html           # 前端页面
│   └── assets/              # 静态资源
├── app.py                   # Streamlit版本 (Docker部署用)
├── vercel.json              # Vercel部署配置
├── Dockerfile               # Docker构建配置
├── requirements.txt         # Python依赖包
├── docker-compose.yml       # Docker Compose配置
├── LICENSE                  # MIT许可证
└── README.md                # 项目文档
```

## 技术栈

- **前端**: 纯 HTML/CSS/JavaScript (Vercel版本)
- **后端**: Python Serverless Functions
- **部署**: Vercel / Docker
- **核心依赖**: requests

## 特性

- **高性能**: 基于 Serverless 的快速响应
- **美观UI**: 现代化的卡片式设计，玻璃态效果
- **响应式**: 自适应不同屏幕尺寸，适配移动端
- **历史记录**: 自动保存生成记录（会话内）
- **配置选项**: 支持随机/固定种子，自定义API配置
- **实时状态**: 生成进度实时显示，带有时间统计
- **一键下载**: PNG图片直接下载，自动命名
- **通用API**: 兼容多种AI图像生成服务

## 快速开始

## 使用方式

### 方式一：Vercel 部署（推荐）⚡

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/kaima2022/showimageweb)

**一键部署步骤：**

1. 点击上方 "Deploy with Vercel" 按钮
2. 登录/注册 Vercel 账号
3. 选择仓库名称，点击 "Deploy"
4. 等待部署完成，即可访问

**手动部署：**

```bash
# 安装 Vercel CLI
npm i -g vercel

# 克隆项目
git clone https://github.com/kaima2022/showimageweb.git
cd ShowImageWeb

# 部署到 Vercel
vercel
```

### 方式二：Docker 部署（灵活）

```bash
# 克隆项目
git clone https://github.com/kaima2022/showimageweb.git
cd ShowImageWeb

# 使用 Docker Compose 启动
docker compose up -d
```

### 方式三：本地开发

```bash
# 克隆项目
git clone https://github.com/kaima2022/showimageweb.git
cd ShowImageWeb

# 安装依赖
pip install -r requirements.txt

# Streamlit 版本启动
streamlit run app.py --server.address=0.0.0.0 --server.port=8501
```

### 访问应用

- **Vercel**: 部署后自动生成域名
- **Docker/本地**: `http://localhost:8501`

## API配置

应用支持任意兼容的AI图像生成API：

### 支持的API格式
- **请求方式**: POST
- **认证方式**: Bearer Token
- **请求格式**: `{"prompt": "...", "seed": ...}`
- **响应格式**: `{"base64": "..."}`

### 配置说明
1. **API URL**: 完整的API接口地址（如：`https://api.example.com/v1/generate`）
2. **API Key**: 您的API密钥
3. **种子设置**: 支持随机种子或固定种子复现结果

### 兼容的服务
- OpenAI DALL-E API
- Stable Diffusion API
- 自建AI图像服务
- 任何支持标准格式的图像生成API

## Vercel 部署说明

### 项目结构

| 文件/目录 | 用途 |
|-----------|------|
| `vercel.json` | Vercel 部署配置文件 |
| `api/generate.py` | Python Serverless Function，处理图像生成请求 |
| `public/index.html` | 前端静态页面 |
| `public/assets/` | 静态资源文件 |

### 环境要求

- Vercel 账号
- Python 3.9+ (Serverless Function)

### 自定义域名

1. 在 Vercel Dashboard 中选择项目
2. 进入 Settings → Domains
3. 添加自定义域名并配置 DNS

## 配置选项

### 界面设置
- **画廊列数**: 1-4列可调
- **随机种子模式**: 开启后每次生成使用不同种子

### API设置
- **API超时**: 默认60秒
- **图片格式**: PNG格式输出
- **文件命名**: 时间戳自动命名

## 贡献指南

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

---
