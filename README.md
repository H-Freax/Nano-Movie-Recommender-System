# Nano Movie Recommender System | 简易电影推荐系统 🎬

[English](#english) | [中文](#chinese)

[![Nano Movie Recommender System](https://img.shields.io/static/v1?style=flat-square&message=Nano+Movie+Recommender+System&color=000000&logo=Notion&logoColor=FFFFFF&label=)](https://freaxruby.notion.site/Nano-Movie-Recommender-System-1829520a6b49805e8c4be6a4c862d6e9)
[![Watch on YouTube](https://img.shields.io/static/v1?style=flat-square&message=Watch+on+YouTube&color=FF0000&logo=YouTube&logoColor=FFFFFF&label=)](https://www.youtube.com/playlist?list=PLVxmJYWCZ7ZrFD0nmAhBTdbi-FsmISPj0)

> 💡 As a **Teaching Assistant for ENGR0201**, I have designed and launched an innovative **tutorial course** for building a movie recommender system from scratch.

<a name="english"></a>
# English Version 🌟

This is a simple movie recommendation system developed in Python, featuring a web interface built with Streamlit.

## Overview 📚

This project is an educational implementation of a recommendation system, demonstrating the step-by-step process of building a basic recommender system. The project covers the complete development process, from environment setup to system implementation and frontend presentation.

## Features 🚀

- 🤝 User-based collaborative filtering recommendations
- 📊 Movie data visualization analysis
- 👥 User behavior analysis
- ⚡ Real-time recommendation display
- 🎯 Intuitive web interface

## Tech Stack 💻

- 🐍 Python 3.x
- 🌐 Streamlit - Web application framework
- 📈 Pandas - Data processing
- 🔢 NumPy - Mathematical computations
- 📋 JSON - Data storage

## Project Structure

```
Nano-Movie-Recommender-System/
├── app.py                     # Streamlit main application - Web interface and user interaction
├── load_data.py              # Data loading module - JSON data management and utility functions
├── recommendation_insights.py # Recommendation system analysis - Advanced insights and analytics
├── user_recommendations.py    # User recommendation logic - Core recommendation algorithms
├── movies.json               # Sample movie database
├── users.json                # Sample user database
├── requirements.txt          # Project dependencies
└── Blogs/                    # Tutorial documentation
    ├── Class_0:Course_Outline.md
    ├── Class_1:What_Is_a_Recommender_System.md
    ├── Class_2:How_to_Design_a_Nano_Recommender_System.md
    ├── Class_3-1:How to Set Up the Development Environment.md
    ├── Class_4:How to Design the Data Structure.md
    ├── Class_5:How to Get the Data.md
    ├── Class_6:How to Write the Streamlit Website to Show the Data.md
    └── Class_7:What else can we do?.md
```

### Core Components

#### app.py
- Main Streamlit web application
- User interface and interaction handling
- Integration of all recommendation features
- Data visualization and display

#### load_data.py
- Data loading and management utilities
- JSON file handling functions
- Data validation and preprocessing
- Utility functions for data filtering and sorting

#### recommendation_insights.py
- Advanced recommendation system analytics
- Cold start problem handling
- User activity impact analysis
- Time-based recommendation adjustments
- Recommendation explanation generation

#### user_recommendations.py
- Core recommendation algorithms implementation
- Multiple recommendation strategies:
  - Genre-based recommendations
  - Collaborative filtering
  - Top-rated recommendations
  - Recent release recommendations
- User preference analysis
- Real-time recommendation generation

## Installation Guide

1. Clone the repository:
```bash
git clone https://github.com/H-Freax/Nano-Movie-Recommender-System.git
cd Nano-Movie-Recommender-System
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage Instructions

1. After launching, access the local Streamlit service via browser (default: http://localhost:8501)
2. Select a user ID or input new user information
3. View personalized movie recommendations
4. Explore movie analysis insights

## Learning Resources 📖

The project includes detailed tutorial documentation and comprehensive learning materials:
- 📚 Course Website: [Nano Movie Recommender System Course](https://freaxruby.notion.site/Nano-Movie-Recommender-System-1829520a6b49805e8c4be6a4c862d6e9)
- 🎥 Course Playlist: [Watch on YouTube](https://www.youtube.com/playlist?list=PLVxmJYWCZ7ZrFD0nmAhBTdbi-FsmISPj0)

### Detailed Course Materials 📚

| No. | Topic | Blog | Video | Duration |
|-----|-------|------|--------|----------|
| 0 | 📋 Course Overview | [Course Outline](Blogs/Class_0:Course_Outline.md) | Coming Soon | - |
| 1 | 🤔 What Is a Recommender System | [Introduction to Recommender Systems](Blogs/Class_1:What_Is_a_Recommender_System.md) | Coming Soon | - |
| 2 | 🎯 How to Design a Nano Recommender System | [System Design Guide](Blogs/Class_2:How_to_Design_a_Nano_Recommender_System.md) | Coming Soon | - |
| 3 | 🛠️ Development Environment Setup | [Setup Guide Part 1](Blogs/Class_3-1:How%20to%20Set%20Up%20the%20Development%20Environment.md)<br>[Setup Guide Part 2 (PDF)](Blogs/Class_3-2:How%20to%20Set%20Up%20the%20Development%20Environment.pdf)<br>[Setup Guide Part 3 (PDF)](Blogs/Class_3-3:How%20to%20Set%20Up%20the%20Development%20Environment.pdf) | Coming Soon | - |
| 4 | 📊 Data Structure Design | [Data Structure Guide](Blogs/Class_4:How%20to%20Design%20the%20Data%20Structure.md) | Coming Soon | - |
| 5 | 📥 Data Acquisition Methods | [Data Acquisition Guide](Blogs/Class_5:How%20to%20Get%20the%20Data.md) | Coming Soon | - |
| 6 | 🌐 Building Streamlit Website | [Streamlit Development Guide](Blogs/Class_6:How%20to%20Write%20the%20Streamlit%20Website%20to%20Show%20the%20Data.md) | Coming Soon | - |
| 7 | 🚀 System Extensions | [Advanced Features Guide](Blogs/Class_7:%20What%20else%20can%20we%20do?.md) | Coming Soon | - |



## Data Structure

### Movie Data (movies.json)
- Movie ID
- Title
- Genre
- Rating
- Other metadata

### User Data (users.json)
- User ID
- Watch history
- Rating records
- Preferences

## Contributing

Contributions via Issues and Pull Requests are welcome. Before submitting code, please ensure:

1. Code follows Python coding standards
2. Necessary comments and documentation are added
3. All tests pass

## License

This project is open-sourced under the MIT License.

## Contact

For questions or suggestions:

- Submit an Issue on [GitHub](https://github.com/H-Freax/Nano-Movie-Recommender-System)
- Email: limyoonaxi@gmail.com


---

<a name="chinese"></a>
# 中文版本 🌟

这是一个基于Python开发的简单电影推荐系统，通过Streamlit构建Web界面，实现电影推荐功能。

## 项目概述 📚

本项目是一个教学性质的推荐系统实现，通过循序渐进的方式展示如何构建一个基础的推荐系统。项目包含完整的开发流程，从环境搭建到系统实现，再到前端展示。

## 功能特点 🚀

- 🤝 基于用户的协同过滤推荐
- 📊 电影数据可视化分析
- 👥 用户行为分析
- ⚡ 实时推荐结果展示
- 🎯 直观的Web界面

## 技术栈 💻

- 🐍 Python 3.x
- 🌐 Streamlit - Web应用框架
- 📈 Pandas - 数据处理
- 🔢 NumPy - 数学计算
- 📋 JSON - 数据存储

## 项目结构

```
Nano-Movie-Recommender-System/
├── app.py                     # Streamlit主应用程序 - Web界面和用户交互
├── load_data.py              # 数据加载模块 - JSON数据管理和工具函数
├── recommendation_insights.py # 推荐系统分析 - 高级分析和洞察
├── user_recommendations.py    # 用户推荐逻辑 - 核心推荐算法
├── movies.json               # 示例电影数据库
├── users.json                # 示例用户数据库
├── requirements.txt          # 项目依赖
└── Blogs/                    # 教程文档
    ├── Class_0:Course_Outline.md
    ├── Class_1:What_Is_a_Recommender_System.md
    ├── Class_2:How_to_Design_a_Nano_Recommender_System.md
    ├── Class_3-1:How to Set Up the Development Environment.md
    ├── Class_4:How to Design the Data Structure.md
    ├── Class_5:How to Get the Data.md
    ├── Class_6:How to Write the Streamlit Website to Show the Data.md
    └── Class_7:What else can we do?.md
```

### 核心组件

#### app.py
- Streamlit主应用程序
- 用户界面和交互处理
- 整合所有推荐功能
- 数据可视化和展示

#### load_data.py
- 数据加载和管理工具
- JSON文件处理函数
- 数据验证和预处理
- 数据过滤和排序工具函数

#### recommendation_insights.py
- 高级推荐系统分析
- 冷启动问题处理
- 用户活动影响分析
- 基于时间的推荐调整
- 推荐解释生成

#### user_recommendations.py
- 核心推荐算法实现
- 多种推荐策略：
  - 基于类型的推荐
  - 协同过滤
  - 高评分推荐
  - 新片推荐
- 用户偏好分析
- 实时推荐生成

## 安装指南

1. 克隆项目到本地：
```bash
git clone https://github.com/H-Freax/Nano-Movie-Recommender-System.git
cd Nano-Movie-Recommender-System
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
streamlit run app.py
```

## 使用说明

1. 启动应用后，通过浏览器访问本地Streamlit服务（默认地址：http://localhost:8501）
2. 在界面上选择用户ID或输入新用户信息
3. 查看个性化电影推荐结果
4. 探索电影分析洞察

## 学习资源 📖

项目包含详细的教程文档和完整的学习材料：
- 📚 课程网站：[简易电影推荐系统课程](https://freaxruby.notion.site/Nano-Movie-Recommender-System-1829520a6b49805e8c4be6a4c862d6e9)
- 🎥 课程视频：[在YouTube上观看](https://www.youtube.com/playlist?list=PLVxmJYWCZ7ZrFD0nmAhBTdbi-FsmISPj0)

### 详细课程资料 📚

| 序号 | 主题 | 教程文档 | 视频 | 时长 |
|-----|------|---------|------|------|
| 0 | 📋 课程概述 | [课程大纲](Blogs/Class_0:Course_Outline.md) | 即将上线 | - |
| 1 | 🤔 什么是推荐系统 | [推荐系统介绍](Blogs/Class_1:What_Is_a_Recommender_System.md) | 即将上线 | - |
| 2 | 🎯 如何设计简易推荐系统 | [系统设计指南](Blogs/Class_2:How_to_Design_a_Nano_Recommender_System.md) | 即将上线 | - |
| 3 | 🛠️ 开发环境搭建 | [环境搭建指南 Part 1](Blogs/Class_3-1:How%20to%20Set%20Up%20the%20Development%20Environment.md)<br>[环境搭建指南 Part 2 (PDF)](Blogs/Class_3-2:How%20to%20Set%20Up%20the%20Development%20Environment.pdf)<br>[环境搭建指南 Part 3 (PDF)](Blogs/Class_3-3:How%20to%20Set%20Up%20the%20Development%20Environment.pdf) | 即将上线 | - |
| 4 | 📊 数据结构设计 | [数据结构指南](Blogs/Class_4:How%20to%20Design%20the%20Data%20Structure.md) | 即将上线 | - |
| 5 | 📥 数据获取方法 | [数据获取指南](Blogs/Class_5:How%20to%20Get%20the%20Data.md) | 即将上线 | - |
| 6 | 🌐 构建Streamlit网站 | [Streamlit开发指南](Blogs/Class_6:How%20to%20Write%20the%20Streamlit%20Website%20to%20Show%20the%20Data.md) | 即将上线 | - |
| 7 | 🚀 系统扩展 | [高级功能指南](Blogs/Class_7:%20What%20else%20can%20we%20do?.md) | 即将上线 | - |



## 数据结构

### 电影数据 (movies.json)
- 电影ID
- 标题
- 类型
- 评分
- 其他元数据

### 用户数据 (users.json)
- 用户ID
- 观看历史
- 评分记录
- 偏好设置

## 贡献指南

欢迎提交Issue和Pull Request来帮助改进项目。在提交代码前，请确保：

1. 代码符合Python代码规范
2. 添加必要的注释和文档
3. 确保所有测试通过

## 开源协议

本项目采用 MIT 协议开源。

## 联系方式

如有问题或建议，请通过以下方式联系：

- 在[GitHub](https://github.com/H-Freax/Nano-Movie-Recommender-System)上提交Issue
- 发送邮件至：limyoonaxi@gmail.com
