# Nano Movie Recommender System | 简易电影推荐系统

[English](#english) | [中文](#chinese)

<a name="english"></a>
# English Version

This is a simple movie recommendation system developed in Python, featuring a web interface built with Streamlit.

## Overview

This project is an educational implementation of a recommendation system, demonstrating the step-by-step process of building a basic recommender system. The project covers the complete development process, from environment setup to system implementation and frontend presentation.

## Features

- User-based collaborative filtering recommendations
- Movie data visualization analysis
- User behavior analysis
- Real-time recommendation display
- Intuitive web interface

## Tech Stack

- Python 3.x
- Streamlit - Web application framework
- Pandas - Data processing
- NumPy - Mathematical computations
- JSON - Data storage

## Project Structure

```
nano_movie_recommender/
├── app.py                    # Streamlit main application
├── load_data.py             # Data loading module
├── recommendation_insights.py # Recommendation system analysis
├── user_recommendations.py   # User recommendation logic
├── movies.json              # Movie data
├── users.json               # User data
├── requirements.txt         # Project dependencies
└── Blogs/                   # Tutorial documentation
    ├── Class_0:Course_Outline.md
    ├── Class_1:What_Is_a_Recommender_System.md
    ├── Class_2:How_to_Design_a_Nano_Recommender_System.md
    ├── Class_3-1:How to Set Up the Development Environment.md
    ├── Class_4:How to Design the Data Structure.md
    ├── Class_5:How to Get the Data.md
    ├── Class_6:How to Write the Streamlit Website to Show the Data.md
    └── Class_7:What else can we do?.md
```

## Installation Guide

1. Clone the repository:
```bash
git clone https://github.com/H-Freax/nano_movie_recommender.git
cd nano_movie_recommender
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

## Learning Resources

The project includes detailed tutorial documentation (in the Blogs directory) and a comprehensive course website:
- Course Website: [Nano Movie Recommender System Course](https://freaxruby.notion.site/Nano-Movie-Recommender-System-1829520a6b49805e8c4be6a4c862d6e9)

Follow the learning sequence:
1. Course Overview
2. Recommender System Basics
3. System Design Methodology
4. Development Environment Setup
5. Data Structure Design
6. Data Acquisition Methods
7. Streamlit Website Development
8. System Optimization and Extensions

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

- Submit an Issue on [GitHub](https://github.com/H-Freax/nano_movie_recommender)
- Email: limyoonaxi@gmail.com


---

<a name="chinese"></a>
# 中文版本

这是一个基于Python开发的简单电影推荐系统，通过Streamlit构建Web界面，实现电影推荐功能。

## 项目概述

本项目是一个教学性质的推荐系统实现，通过循序渐进的方式展示如何构建一个基础的推荐系统。项目包含完整的开发流程，从环境搭建到系统实现，再到前端展示。

## 功能特点

- 基于用户的协同过滤推荐
- 电影数据可视化分析
- 用户行为分析
- 实时推荐结果展示
- 直观的Web界面

## 技术栈

- Python 3.x
- Streamlit - Web应用框架
- Pandas - 数据处理
- NumPy - 数学计算
- JSON - 数据存储

## 项目结构

```
nano_movie_recommender/
├── app.py                    # Streamlit主应用程序
├── load_data.py             # 数据加载模块
├── recommendation_insights.py # 推荐系统分析模块
├── user_recommendations.py   # 用户推荐逻辑模块
├── movies.json              # 电影数据
├── users.json               # 用户数据
├── requirements.txt         # 项目依赖
└── Blogs/                   # 教程文档
    ├── Class_0:Course_Outline.md
    ├── Class_1:What_Is_a_Recommender_System.md
    ├── Class_2:How_to_Design_a_Nano_Recommender_System.md
    ├── Class_3-1:How to Set Up the Development Environment.md
    ├── Class_4:How to Design the Data Structure.md
    ├── Class_5:How to Get the Data.md
    ├── Class_6:How to Write the Streamlit Website to Show the Data.md
    └── Class_7:What else can we do?.md
```

## 安装指南

1. 克隆项目到本地：
```bash
git clone https://github.com/H-Freax/nano_movie_recommender.git
cd nano_movie_recommender
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

## 学习资源

项目包含详细的教程文档（位于Blogs目录）和完整的课程网站：
- 课程网站：[简易电影推荐系统课程](https://freaxruby.notion.site/Nano-Movie-Recommender-System-1829520a6b49805e8c4be6a4c862d6e9)

按照以下顺序学习：
1. 课程概述
2. 推荐系统基础知识
3. 推荐系统设计方法
4. 开发环境搭建
5. 数据结构设计
6. 数据获取方法
7. Streamlit网站开发
8. 系统优化与扩展

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

- 在[GitHub](https://github.com/H-Freax/nano_movie_recommender)上提交Issue
- 发送邮件至：limyoonaxi@gmail.com
