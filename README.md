# AI Agent Skills Collection | AI Agent 技能合集 🤖

> **[English](README.md) | [简体中文](README_zh-CN.md)**

---

### 🌟 Introduction / 简介

**EN**: A curated collection of modular skills (tools) designed for AI agents. This repository hosts standardized tools that AI agents (like Large Language Models) can utilize to interact with the real world—fetching data, controlling software, or processing files.

**ZH**: 这是一个为 AI Agent 精心策划的模块化技能（工具）合集。本仓库托管了一组标准化的工具，AI Agent（如大型语言模型）可以利用这些技能与现实世界互动——获取数据、控制软件或处理文件。

---

## 📂 Available Skills / 可用技能

### 🌐 Information & Search
| Skill Name | Description (EN) | 描述 (ZH) |
| :--- | :--- | :--- |
| [**web-search-duckduckgo**](skills/web-search-duckduckgo/SKILL.md) | Perform anonymous web searches. | 执行匿名网络搜索以查找信息。 |
| [**weather-lookup**](skills/weather-lookup/SKILL.md) | Retrieve current weather conditions. | 查询特定城市的实时天气状况。 |

### 📊 Finance
| Skill Name | Description (EN) | 描述 (ZH) |
| :--- | :--- | :--- |
| [**stock-price**](skills/stock-price/SKILL.md) | Retrieve real-time stock market data. | 获取实时股票价格和市场数据。 |
| [**currency-converter**](skills/currency-converter/SKILL.md) | Real-time currency conversion. | 实时汇率转换。 |

### 📂 File & Media
| Skill Name | Description (EN) | 描述 (ZH) |
| :--- | :--- | :--- |
| [**pdf-text-extractor**](skills/pdf-text-extractor/SKILL.md) | Extract text from PDF files. | 从 PDF 文件中提取文本。 |
| [**youtube-info**](skills/youtube-info/SKILL.md) | Fetch YouTube video metadata. | 获取 YouTube 视频元数据。 |

### ⚙️ System
| Skill Name | Description (EN) | 描述 (ZH) |
| :--- | :--- | :--- |
| [**system-info**](skills/system-info/SKILL.md) | Check system resource usage. | 检查主机的 CPU、内存和磁盘使用情况。 |

### 🛠 Developer Tools
| Skill Name | Description (EN) | 描述 (ZH) |
| :--- | :--- | :--- |
| [**github-manager**](skills/github-manager/SKILL.md) | Manage GitHub repos and issues via CLI. | 通过命令行管理 GitHub 仓库和 Issue。 |


## 🚀 How to Use

Each skill is located in the `skills/` directory and contains a `SKILL.md` file. This file describes:
1.  **Purpose**: When the AI should use this skill.
2.  **Tools**: The specific scripts (Python/Node.js) to execute.
3.  **IO**: Expected input arguments and output JSON format.

### Interactive CLI

We provide a simple command-line interface to test these skills:

```bash
python main.py
```

## 📦 Dependencies

You can install all dependencies for the skills at once:

```bash
pip install -r requirements.txt
```

## 🤝 Contributing

We welcome contributions! If you have built a useful tool for AI agents, please submit a PR.

1.  Create a new folder in `skills/`.
2.  Add your script (e.g., `tool.py`).
3.  Add a `SKILL.md` following the standard format.
4.  Add an `Acknowledgments` section in your `SKILL.md` if adapted from another project.

## 📄 License

MIT License
