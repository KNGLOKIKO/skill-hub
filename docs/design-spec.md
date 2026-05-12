# GitHub Skill Hub - 现代化重构设计文档

> **项目版本**: V2.0  
> **更新日期**: 2026年5月  
> **设计风格**: 现代化、极简主义，科技感  
> **技术栈**: React 18 + TypeScript + Tailwind CSS v4 + Motion

---

## 1. 项目概述

### 1.1 核心定位
完全重构GitHub Skill Hub网站，采用现代化的React技术栈，提供极致的视觉体验和卓越的性能。保留原有的GitHub开源AI工具导航功能，同时增加动态视频Hero，品牌展示Marquee等现代化元素。

### 1.2 核心目标
1. **现代化技术栈**：采用React 18 + TypeScript + Tailwind CSS v4 + Motion
2. **卓越视觉效果**：视频背景Hero、流畅动画，品牌Logo滚动展示
3. **极致性能**：代码分割、懒加载
4. **完美可访问性**：符合WAI-ARIA标准、键盘导航支持
5. **商业化支持**：智能广告位管理（无广告代码时自动隐藏）

---

## 2. 技术架构

### 2.1 技术栈
- 前端框架: React 18 (使用Vite构建)
- 类型系统: TypeScript 5
- 样式方案: Tailwind CSS v4 + CSS Variables
- 动画库: Motion (Framer Motion)
- 图标库: Lucide React
- 打包工具: Vite 5
- 包管理: npm/pnpm

### 2.2 项目结构
```
github-skill-hub/
├── public/
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── Hero.tsx
│   │   ├── FloatingNav.tsx
│   │   ├── MarqueeLogos.tsx
│   │   ├── CategorySection.tsx
│   │   ├── SkillCard.tsx
│   │   ├── AdSpace.tsx
│   │   ├── SearchInput.tsx
│   │   ├── BackToTop.tsx
│   │   ├── Header.tsx
│   │   └── Footer.tsx
│   ├── pages/
│   │   ├── Home.tsx
│   │   └── Copyright.tsx
│   ├── data/
│   │   └── skills.ts
│   ├── hooks/
│   │   ├── useSearch.ts
│   │   └── useScrollAnimation.ts
│   ├── styles/
│   │   └── index.css
│   ├── types/
│   │   └── index.ts
│   ├── App.tsx
│   └── main.tsx
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.js
├── postcss.config.js
└── README.md
```

---

## 3. 核心组件设计

### 3.1 Hero Section - 主英雄区域

#### 设计规格
- **容器**: 圆角48px的白色卡片容器（1400px最大宽度）
- **高度**: 600px固定高度
- **背景**: 动态视频背景
- **阴影**: 精心设计的柔和阴影系统

#### 视觉效果
- **标题**: "Foundation of the new digital epoch"
  - 字体: Outfit (display)
  - 字号: 42px/56px (移动/桌面)
  - 颜色: #0a1b33 (深蓝)
  - 字重: 500 (medium)
  
- **副标题**: 
  - 字体: Inter (sans)
  - 字号: 14px/15px
  - 颜色: #64748b (灰色)
  
- **CTA按钮**: "Contact Us"
  - 背景: #0a152d (深蓝黑)
  - 悬停: 缩放动画 (scale: 1.05)

#### 动画设计
- **入场动画**: 淡入 + 向上滑动
- **时长**: 800ms
- **缓动**: ease-out
- **延迟**: 标题→副标题→按钮（200ms间隔）

### 3.2 Floating Navigation - 浮动导航栏

#### 设计规格
- **位置**: Hero底部居中 (bottom-10)
- **背景**: 白色90%透明度 + 毛玻璃效果
- **圆角**: 全圆角药丸形状
- **阴影**: 柔和的阴影系统

#### 导航元素
- Logo图标 (✦)
- Products 链接
- Docs 链接
- Get in touch 按钮 (带ChevronRight图标)

#### 动画设计
- **入场**: 淡入 + 向上滑动（Hero文本后200ms）
- **悬停**: 按钮颜色过渡
- **过渡**: 300ms ease

### 3.3 Marquee Logo Scroller - 品牌滚动组件

#### 设计规格
- **位置**: Hero下方 (mt-10)
- **Logo数量**: 8个
- **布局**: 水平无限滚动

#### Logo列表
1. Procure (蓝色渐变)
2. Shopify (黄色渐变)
3. Blender (蓝色渐变)
4. Figma (紫色渐变)
5. Spotify (粉色/红色渐变)
6. Lottielab (黄色/绿色渐变)
7. Google Cloud (浅蓝色渐变)
8. Bing (青色/蓝绿色渐变)

#### 卡片设计
- **尺寸**: 96px × 160px
- **圆角**: 全圆角
- **背景**: 白色 + 边框
- **悬停效果**:
  - 边框颜色变化
  - 渐变背景显现
  - Logo颜色反转

#### 动画规格
- **类型**: 纯CSS @keyframes
- **方向**: translateX(0) → translateX(-50%)
- **时长**: 30s (可调整)
- **缓动**: linear
- **暂停**: hover时暂停

### 3.4 Category Sections - 分类区域

#### 分类列表
1. **文案写作** (✍️) - 8个工具
2. **AI绘画** (🎨) - 8个工具
3. **职场办公** (💼) - 8个工具
4. **学习备考** (📚) - 8个工具
5. **代码开发** (💻) - 8个工具
6. **生活实用** (🌟) - 8个工具

### 3.5 Ad Space Component - 广告位组件

#### 设计规格
- **智能显示**: 只在配置广告代码时显示
- **默认隐藏**: 无广告代码时自动隐藏
- **动画**: 流光shimmer效果

#### 广告位列表
- 顶部横幅广告
- 分类间信息流广告 (5个位置)
- 底部横幅广告

---

## 4. 样式系统

### 4.1 字体配置
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;500;600&display=swap');

:root {
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-display: 'Outfit', system-ui, sans-serif;
}

body {
  font-family: var(--font-sans);
  background: #f9fafb;
}
```

### 4.2 颜色系统
```css
:root {
  --color-primary: #0a152d;
  --color-primary-dark: #050a12;
  --color-accent: #3b82f6;
  --color-text: #0a1b33;
  --color-text-muted: #64748b;
  --color-bg: #f9fafb;
  --color-bg-white: #ffffff;
  --color-border: #e2e8f0;
}
```

---

## 5. 可访问性 (Accessibility)

### 5.1 ARIA标签
- 所有图标按钮添加 aria-label
- 搜索输入添加 aria-label
- 广告区域添加 aria-hidden 或 role="complementary"
- 导航使用语义化 nav 标签

### 5.2 键盘导航
- Tab键导航所有交互元素
- Enter/Space激活按钮
- Skip Link跳转到主要内容

### 5.3 动画偏好
支持 prefers-reduced-motion媒体查询

---

## 6. 性能优化

### 6.1 代码分割
- 使用 React.lazy() 懒加载页面
- 动态导入组件

### 6.2 动画性能
- 使用 CSS transform 和 opacity
- 使用 will-change 提示浏览器

---

## 7. 部署策略

### 7.1 部署平台
- Vercel (推荐): 自动部署、边缘网络、免费SSL
- Netlify: 静态站点托管、持续部署
- GitHub Pages: 免费托管

### 7.2 构建命令
```bash
npm install
npm run dev    # 开发环境
npm run build  # 构建生产版本
npm run preview # 预览生产版本
```

---

## 8. 文件清单

### 必需文件
- package.json
- vite.config.ts
- tsconfig.json
- tailwind.config.js
- postcss.config.js
- index.html
- src/main.tsx
- src/App.tsx
- src/index.css
- src/components/*.tsx
- src/pages/*.tsx
- src/data/skills.ts

---

**设计文档版本**: V1.0  
**创建日期**: 2026年5月9日  
**状态**: 待审批
