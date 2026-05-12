# GitHub Skill Hub V2.0 实施计划

> **目标**: 使用React 18 + TypeScript + Tailwind CSS v4 + Motion构建现代化的GitHub Skill Hub网站  
> **架构**: 单页面应用（SPA），组件化架构  
> **技术栈**: React 18, TypeScript 5, Tailwind CSS v4, Motion, Vite 5, Lucide React

---

## 第一阶段：项目初始化

### 任务 1.1: 初始化 Vite + React + TypeScript 项目

**目标**: 创建基础项目结构

```bash
# 创建新项目
cd c:\Users\KngLokiko\Desktop\HTML
npm create vite@latest github-skill-hub -- --template react-ts

# 进入项目目录
cd github-skill-hub

# 安装基础依赖
npm install

# 安装额外依赖
npm install motion lucide-react clsx tailwind-merge
npm install -D tailwindcss postcss autoprefixer
```

**验证**: 运行 `npm run dev` 确认项目启动

---

### 任务 1.2: 配置 Tailwind CSS v4

**修改文件**: `tailwind.config.js`

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Outfit', 'system-ui', 'sans-serif'],
      },
      colors: {
        primary: '#0a152d',
        'primary-dark': '#050a12',
        accent: '#3b82f6',
        text: '#0a1b33',
        'text-muted': '#64748b',
      },
    },
  },
  plugins: [],
}
```

**修改文件**: `src/index.css`

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;500;600&display=swap');

@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-display: 'Outfit', system-ui, sans-serif;
}

body {
  font-family: var(--font-sans);
  background: #f9fafb;
}

/* 动画偏好支持 */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

**验证**: 运行 `npm run dev` 确认Tailwind生效

---

## 第二阶段：类型定义和数据结构

### 任务 2.1: 创建类型定义

**新建文件**: `src/types/index.ts`

```typescript
export interface Skill {
  id: string;
  name: string;
  author: string;
  category: string;
  description: string;
  githubUrl: string;
  license: string;
}

export interface Category {
  id: string;
  name: string;
  icon: string;
  count: number;
}

export interface Logo {
  name: string;
  src: string;
  gradient: {
    from: string;
    to: string;
  };
}

export interface AdSlot {
  id: string;
  code?: string;
}

export interface NavItem {
  label: string;
  type: 'logo' | 'link' | 'button';
  icon?: string;
  href?: string;
}
```

**验证**: TypeScript编译无错误

---

### 任务 2.2: 创建数据文件

**新建文件**: `src/data/skills.ts`

```typescript
import { Skill, Category, Logo } from '../types';

export const skills: Skill[] = [
  // 文案写作 - 8个
  { id: "1", name: "AI论文写作助手", author: "academic-ai", category: "writing", description: "基于GitHub开源的论文降重、大纲生成和润色提示词模板", githubUrl: "https://github.com/academic-ai/paper-writer", license: "MIT" },
  { id: "2", name: "营销文案生成器", author: "marketing-gpt", category: "writing", description: "电商产品描述、广告文案、社交媒体帖子自动生成工具", githubUrl: "https://github.com/marketing-gpt/copy-generator", license: "Apache-2.0" },
  { id: "3", name: "邮件写作助手", author: "email-pro", category: "writing", description: "专业商务邮件、感谢信、投诉信等各类邮件模板", githubUrl: "https://github.com/email-pro/email-writer", license: "MIT" },
  { id: "4", name: "SEO文章优化器", author: "seo-master", category: "writing", description: "文章SEO优化建议、关键词分析和标题生成工具", githubUrl: "https://github.com/seo-master/seo-optimizer", license: "MIT" },
  { id: "5", name: "短视频脚本生成", author: "video-script", category: "writing", description: "抖音、B站等短视频平台脚本创作助手", githubUrl: "https://github.com/video-script/short-video", license: "Apache-2.0" },
  { id: "6", name: "小说写作辅助", author: "novel-ai", category: "writing", description: "小说大纲、人物设定、情节发展辅助工具", githubUrl: "https://github.com/novel-ai/novel-assistant", license: "MIT" },
  { id: "7", name: "简历优化工具", author: "resume-pro", category: "writing", description: "简历内容优化、STAR法则描述生成器", githubUrl: "https://github.com/resume-pro/resume-builder", license: "MIT" },
  { id: "8", name: "翻译润色助手", author: "translate-ai", category: "writing", description: "多语言翻译+母语润色二合一工具", githubUrl: "https://github.com/translate-ai/polisher", license: "Apache-2.0" },
  
  // AI绘画 - 8个
  { id: "9", name: "Midjourney提示词库", author: "mj-prompts", category: "art", description: "精选Midjourney高质量提示词集合，包含各种风格", githubUrl: "https://github.com/mj-prompts/collection", license: "MIT" },
  { id: "10", name: "Stable Diffusion WebUI", author: "sd-webui", category: "art", description: "最流行的Stable Diffusion图形界面工具", githubUrl: "https://github.com/AUTOMATIC1111/stable-diffusion-webui", license: "AGPL-3.0" },
  { id: "11", name: "LoRA训练助手", author: "lora-trainer", category: "art", description: "简化版LoRA模型训练脚本和教程", githubUrl: "https://github.com/lora-trainer/guide", license: "MIT" },
  { id: "12", name: "ControlNet插件包", author: "controlnet-pack", category: "art", description: "ControlNet各种预处理器和模型合集", githubUrl: "https://github.com/controlnet-pack/plugins", license: "Apache-2.0" },
  { id: "13", name: "AI头像生成器", author: "avatar-ai", category: "art", description: "个性化AI头像生成工具，支持多种风格", githubUrl: "https://github.com/avatar-ai/generator", license: "MIT" },
  { id: "14", name: "图像修复工具", author: "inpaint-pro", category: "art", description: "智能图像修复、去水印、扩图工具", githubUrl: "https://github.com/inpaint-pro/tool", license: "MIT" },
  { id: "15", name: "Prompt工程师", author: "prompt-eng", category: "art", description: "AI绘画提示词优化和生成工具", githubUrl: "https://github.com/prompt-eng/optimizer", license: "Apache-2.0" },
  { id: "16", name: "动漫风格转换", author: "anime-style", category: "art", description: "照片转动漫风格的AI工具集合", githubUrl: "https://github.com/anime-style/converter", license: "MIT" },
  
  // 职场办公 - 8个
  { id: "17", name: "Excel公式助手", author: "excel-pro", category: "office", description: "Excel公式生成、解释和优化工具", githubUrl: "https://github.com/excel-pro/formula-helper", license: "MIT" },
  { id: "18", name: "PPT大纲生成器", author: "ppt-builder", category: "office", description: "快速生成专业PPT大纲和内容建议", githubUrl: "https://github.com/ppt-builder/outline", license: "Apache-2.0" },
  { id: "19", name: "会议纪要助手", author: "meeting-ai", category: "office", description: "会议录音转文字、自动摘要和行动项提取", githubUrl: "https://github.com/meeting-ai/minutes", license: "MIT" },
  { id: "20", name: "周报生成器", author: "weekly-report", category: "office", description: "工作周报、月报自动生成工具", githubUrl: "https://github.com/weekly-report/generator", license: "MIT" },
  { id: "21", name: "数据可视化助手", author: "data-viz", category: "office", description: "Python/R数据可视化代码生成和优化", githubUrl: "https://github.com/data-viz/helper", license: "Apache-2.0" },
  { id: "22", name: "项目管理工具", author: "pm-ai", category: "office", description: "项目计划、甘特图、风险评估辅助工具", githubUrl: "https://github.com/pm-ai/assistant", license: "MIT" },
  { id: "23", name: "合同审查助手", author: "contract-ai", category: "office", description: "合同文本审查、风险点提示和修改建议", githubUrl: "https://github.com/contract-ai/reviewer", license: "MIT" },
  { id: "24", name: "商务谈判助手", author: "negotiation-ai", category: "office", description: "商务谈判策略、话术建议和准备清单", githubUrl: "https://github.com/negotiation-ai/helper", license: "Apache-2.0" },
  
  // 学习备考 - 8个
  { id: "25", name: "知识点总结器", author: "study-summary", category: "study", description: "教材知识点自动总结和思维导图生成", githubUrl: "https://github.com/study-summary/tool", license: "MIT" },
  { id: "26", name: "题库生成助手", author: "quiz-builder", category: "study", description: "根据知识点自动生成练习题和答案", githubUrl: "https://github.com/quiz-builder/generator", license: "Apache-2.0" },
  { id: "27", name: "语言学习伙伴", author: "language-ai", category: "study", description: "多语言口语练习、语法纠错和词汇记忆", githubUrl: "https://github.com/language-ai/partner", license: "MIT" },
  { id: "28", name: "论文文献管理", author: "reference-pro", category: "study", description: "文献整理、引用格式生成和综述写作助手", githubUrl: "https://github.com/reference-pro/manager", license: "MIT" },
  { id: "29", name: "考试冲刺计划", author: "exam-plan", category: "study", description: "个性化考试复习计划制定和进度追踪", githubUrl: "https://github.com/exam-plan/planner", license: "Apache-2.0" },
  { id: "30", name: "代码学习助手", author: "code-learn", category: "study", description: "编程概念解释、代码示例生成和练习", githubUrl: "https://github.com/code-learn/assistant", license: "MIT" },
  { id: "31", name: "记忆卡片生成", author: "flashcard-ai", category: "study", description: "Anki风格记忆卡片自动生成工具", githubUrl: "https://github.com/flashcard-ai/generator", license: "MIT" },
  { id: "32", name: "课程笔记整理", author: "note-taker", category: "study", description: "课堂录音/笔记自动整理和结构化", githubUrl: "https://github.com/note-taker/ai", license: "Apache-2.0" },
  
  // 代码开发 - 8个
  { id: "33", name: "代码解释器", author: "code-explainer", category: "code", description: "代码逐行解释、复杂度分析和优化建议", githubUrl: "https://github.com/code-explainer/tool", license: "MIT" },
  { id: "34", name: "Bug调试助手", author: "debug-ai", category: "code", description: "错误信息分析、调试思路和修复建议", githubUrl: "https://github.com/debug-ai/helper", license: "Apache-2.0" },
  { id: "35", name: "API文档生成", author: "api-doc", category: "code", description: "自动生成API文档、示例代码和测试用例", githubUrl: "https://github.com/api-doc/generator", license: "MIT" },
  { id: "36", name: "代码审查工具", author: "code-review", category: "code", description: "代码质量审查、安全漏洞扫描和最佳实践建议", githubUrl: "https://github.com/code-review/ai", license: "MIT" },
  { id: "37", name: "Git提交助手", author: "git-helper", category: "code", description: "Git提交信息生成、分支管理和合并建议", githubUrl: "https://github.com/git-helper/ai", license: "Apache-2.0" },
  { id: "38", name: "测试用例生成", author: "test-gen", category: "code", description: "根据代码自动生成单元测试和集成测试", githubUrl: "https://github.com/test-gen/ai", license: "MIT" },
  { id: "39", name: "架构设计助手", author: "arch-ai", category: "code", description: "系统架构设计建议、技术选型和流程图生成", githubUrl: "https://github.com/arch-ai/assistant", license: "MIT" },
  { id: "40", name: "正则表达式生成", author: "regex-ai", category: "code", description: "自然语言描述生成正则表达式并解释", githubUrl: "https://github.com/regex-ai/generator", license: "Apache-2.0" },
  
  // 生活实用 - 8个
  { id: "41", name: "旅行规划助手", author: "travel-ai", category: "life", description: "行程规划、景点推荐、预算估算一站式服务", githubUrl: "https://github.com/travel-ai/planner", license: "MIT" },
  { id: "42", name: "健康饮食顾问", author: "health-ai", category: "life", description: "个性化饮食建议、食谱生成和营养分析", githubUrl: "https://github.com/health-ai/advisor", license: "Apache-2.0" },
  { id: "43", name: "理财规划助手", author: "finance-ai", category: "life", description: "个人理财规划、预算管理和投资建议", githubUrl: "https://github.com/finance-ai/planner", license: "MIT" },
  { id: "44", name: "智能家居控制", author: "smart-home", category: "life", description: "Home Assistant等智能家居自动化脚本集合", githubUrl: "https://github.com/smart-home/scripts", license: "MIT" },
  { id: "45", name: "摄影后期助手", author: "photo-ai", category: "life", description: "摄影后期处理建议和Lightroom预设", githubUrl: "https://github.com/photo-ai/editor", license: "Apache-2.0" },
  { id: "46", name: "音乐推荐助手", author: "music-ai", category: "life", description: "基于心情和场景的音乐推荐和歌单生成", githubUrl: "https://github.com/music-ai/recommender", license: "MIT" },
  { id: "47", name: "宠物护理顾问", author: "pet-ai", category: "life", description: "宠物饲养建议、健康问题初步判断", githubUrl: "https://github.com/pet-ai/advisor", license: "MIT" },
  { id: "48", name: "时间管理助手", author: "time-ai", category: "life", description: "番茄工作法、任务优先级排序和时间追踪", githubUrl: "https://github.com/time-ai/manager", license: "Apache-2.0" }
];

export const categories: Category[] = [
  { id: 'writing', name: '文案写作', icon: '✍️', count: 8 },
  { id: 'art', name: 'AI绘画', icon: '🎨', count: 8 },
  { id: 'office', name: '职场办公', icon: '💼', count: 8 },
  { id: 'study', name: '学习备考', icon: '📚', count: 8 },
  { id: 'code', name: '代码开发', icon: '💻', count: 8 },
  { id: 'life', name: '生活实用', icon: '🌟', count: 8 }
];

export const logos: Logo[] = [
  { name: 'Procure', src: 'https://svgl.app/library/procure.svg', gradient: { from: '#3b82f6', to: '#8b5cf6' } },
  { name: 'Shopify', src: 'https://svgl.app/library/shopify.svg', gradient: { from: '#f59e0b', to: '#fbbf24' } },
  { name: 'Blender', src: 'https://svgl.app/library/blender.svg', gradient: { from: '#3b82f6', to: '#06b6d4' } },
  { name: 'Figma', src: 'https://svgl.app/library/figma.svg', gradient: { from: '#8b5cf6', to: '#a855f7' } },
  { name: 'Spotify', src: 'https://svgl.app/library/spotify.svg', gradient: { from: '#ec4899', to: '#f43f5e' } },
  { name: 'Lottielab', src: 'https://svgl.app/library/lottielab.svg', gradient: { from: '#facc15', to: '#84cc16' } },
  { name: 'Google Cloud', src: 'https://svgl.app/library/google-cloud.svg', gradient: { from: '#38bdf8', to: '#0ea5e9' } },
  { name: 'Bing', src: 'https://svgl.app/library/bing.svg', gradient: { from: '#06b6d4', to: '#14b8a6' } }
];

export const categoryMap: Record<string, string> = {
  'writing': 'writing-skills',
  'art': 'art-skills',
  'office': 'office-skills',
  'study': 'study-skills',
  'code': 'code-skills',
  'life': 'life-skills'
};
```

---

## 第三阶段：核心组件开发

### 任务 3.1: 创建 Hero 组件

**新建文件**: `src/components/Hero.tsx`

```typescript
import { motion } from 'motion/react';
import { ChevronRight } from 'lucide-react';

export function Hero() {
  return (
    <div className="relative w-full max-w-[1400px] mx-auto rounded-[48px] bg-white border border-slate-200/50 shadow-[0_40px_100px_-20px_rgba(0,0,0,0.03)] overflow-hidden h-[600px] flex flex-col">
      {/* 视频背景 */}
      <div className="absolute inset-0 pointer-events-none z-0 overflow-hidden select-none">
        <video
          autoPlay
          loop
          muted
          playsInline
          className="w-full h-full object-cover scale-105 transition-transform duration-1000"
        >
          <source src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260505_101331_74f9b798-3f00-4e86-8a01-377aa16ffeaa.mp4" type="video/mp4" />
        </video>
      </div>

      {/* 文本内容 */}
      <div className="z-20 flex-1 px-8 md:px-16 pt-12 md:pt-16 flex flex-col items-start">
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: 'easeOut' }}
          className="font-display text-[42px] md:text-[56px] font-medium tracking-tight text-[#0a1b33]"
        >
          Foundation of the<br />new digital epoch
        </motion.h1>
        
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2, ease: 'easeOut' }}
          className="font-sans text-[14px] md:text-[15px] text-[#64748b] mt-6 max-w-2xl"
        >
          Designing products, powering ecosystems and laying the foundation of a decentralized web for enterprises, builders and communities alike.
        </motion.p>
        
        <motion.button
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.4, ease: 'easeOut' }}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          className="mt-8 bg-[#0a152d] text-white px-8 py-3 rounded-full font-sans font-medium"
        >
          Contact Us
        </motion.button>
      </div>

      {/* 浮动导航栏 */}
      <motion.nav
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.6, ease: 'easeOut' }}
        className="absolute bottom-10 left-1/2 -translate-x-1/2 z-30 flex items-center bg-white/90 backdrop-blur-2xl px-1.5 py-1.5 rounded-full shadow-[0_12px_40px_rgba(0,0,0,0.08)] border border-slate-200/40"
      >
        {/* Logo */}
        <div className="w-9 h-9 bg-white border-slate-100 shadow-sm rounded-full flex items-center justify-center mr-2">
          <span className="text-[#0a152d]">✦</span>
        </div>
        
        {/* 导航链接 */}
        <a href="#products" className="text-[12px] font-semibold text-slate-500 hover:text-[#0a1b33] transition-colors px-4 py-2">
          Products
        </a>
        <a href="#docs" className="text-[12px] font-semibold text-slate-500 hover:text-[#0a1b33] transition-colors px-4 py-2">
          Docs
        </a>
        
        {/* Get in touch 按钮 */}
        <button className="bg-white px-5 py-2 rounded-full text-[12px] font-semibold text-[#0a152d] border border-slate-200/60 shadow-sm hover:border-slate-300 transition-all flex items-center gap-1 ml-2">
          Get in touch
          <ChevronRight className="w-3 h-3" />
        </button>
      </motion.nav>
    </div>
  );
}
```

**验证**: Hero组件渲染正常，视频播放

---

### 任务 3.2: 创建 MarqueeLogos 组件

**新建文件**: `src/components/MarqueeLogos.tsx`

```typescript
import { logos } from '../data/skills';

export function MarqueeLogos() {
  return (
    <div className="mt-10 overflow-hidden relative">
      {/* 遮罩渐变 */}
      <div 
        className="absolute left-0 top-0 bottom-0 w-32 z-10 pointer-events-none"
        style={{
          background: 'linear-gradient(to right, #f9fafb, transparent)'
        }}
      />
      <div 
        className="absolute right-0 top-0 bottom-0 w-32 z-10 pointer-events-none"
        style={{
          background: 'linear-gradient(to left, #f9fafb, transparent)'
        }}
      />
      
      {/* 滚动容器 */}
      <div 
        className="flex gap-6 animate-marquee hover:[animation-play-state:paused]"
        style={{
          animation: 'marquee 30s linear infinite'
        }}
      >
        {/* 第一组Logo */}
        {[...logos, ...logos].map((logo, index) => (
          <div
            key={index}
            className="group relative h-24 w-40 shrink-0 flex items-center justify-center rounded-full bg-white border border-slate-200/60 shadow-sm hover:border-slate-300 transition-all overflow-hidden flex-shrink-0"
          >
            {/* 渐变背景 */}
            <div
              className="absolute inset-0 scale-150 opacity-0 group-hover:scale-100 group-hover:opacity-100 transition-all duration-300"
              style={{
                background: `linear-gradient(135deg, ${logo.gradient.from}, ${logo.gradient.to})`
              }}
            />
            
            {/* Logo图片 */}
            <img
              src={logo.src}
              alt={logo.name}
              className="relative z-10 w-12 h-12 group-hover:brightness-0 group-hover:invert transition-all"
            />
          </div>
        ))}
      </div>

      <style>{`
        @keyframes marquee {
          0% { transform: translateX(0); }
          100% { transform: translateX(-50%); }
        }
      `}</style>
    </div>
  );
}
```

---

### 任务 3.3: 创建 SkillCard 组件

**新建文件**: `src/components/SkillCard.tsx`

```typescript
import { motion } from 'motion/react';
import { Skill } from '../types';

interface SkillCardProps {
  skill: Skill;
  index: number;
}

export function SkillCard({ skill, index }: SkillCardProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: index * 0.05 }}
      whileHover={{ y: -8 }}
      className="bg-white border border-slate-200/60 rounded-2xl p-6 hover:shadow-lg hover:border-slate-300 transition-all relative overflow-hidden group"
    >
      {/* 顶部渐变条 */}
      <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 opacity-0 group-hover:opacity-100 transition-opacity" />
      
      <h3 className="font-display text-lg font-semibold text-[#0a1b33] mb-2">
        {skill.name}
      </h3>
      
      <p className="text-[#64748b] text-sm mb-4 line-clamp-2">
        {skill.description}
      </p>
      
      {/* 元数据标签 */}
      <div className="flex flex-wrap gap-2 mb-4">
        <span className="px-3 py-1 bg-slate-100 rounded-lg text-xs text-slate-600">
          👤 {skill.author}
        </span>
        <span className="px-3 py-1 bg-slate-100 rounded-lg text-xs text-slate-600">
          📄 {skill.license}
        </span>
      </div>
      
      {/* GitHub按钮 */}
      <a
        href={skill.githubUrl}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center justify-center gap-2 w-full py-3 bg-[#0a152d] text-white rounded-xl font-medium text-sm hover:bg-[#0a1b33] transition-colors"
      >
        GitHub仓库直达
        <span>→</span>
      </a>
    </motion.div>
  );
}
```

---

### 任务 3.4: 创建 CategorySection 组件

**新建文件**: `src/components/CategorySection.tsx`

```typescript
import { Category, Skill } from '../types';
import { SkillCard } from './SkillCard';

interface CategorySectionProps {
  category: Category;
  skills: Skill[];
}

export function CategorySection({ category, skills }: CategorySectionProps) {
  return (
    <section className="mb-16">
      <div className="flex items-center gap-3 mb-8 pb-4 border-b border-slate-200">
        <span className="text-3xl">{category.icon}</span>
        <h2 className="text-2xl font-display font-semibold text-[#0a1b33]">
          {category.name}
        </h2>
        <span className="ml-auto px-4 py-1 bg-blue-100 text-blue-600 rounded-full text-sm font-medium">
          {category.count} 个工具
        </span>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {skills.map((skill, index) => (
          <SkillCard key={skill.id} skill={skill} index={index} />
        ))}
      </div>
    </section>
  );
}
```

---

### 任务 3.5: 创建 AdSpace 组件

**新建文件**: `src/components/AdSpace.tsx`

```typescript
import { useState, useEffect } from 'react';

interface AdSpaceProps {
  slot: string;
  className?: string;
}

// 广告配置 - 在这里配置您的Google AdSense代码
const AD_CONFIG: Record<string, string> = {
  // 如果需要启用广告，取消注释并填入您的广告代码
  // top: 'ca-pub-XXXXX/XXXXX',
  // feed1: 'ca-pub-XXXXX/XXXXX',
  // feed2: 'ca-pub-XXXXX/XXXXX',
  // feed3: 'ca-pub-XXXXX/XXXXX',
  // feed4: 'ca-pub-XXXXX/XXXXX',
  // feed5: 'ca-pub-XXXXX/XXXXX',
  // bottom: 'ca-pub-XXXXX/XXXXX',
};

export function AdSpace({ slot, className = '' }: AdSpaceProps) {
  const [hasAd, setHasAd] = useState(false);
  
  useEffect(() => {
    // 检查是否配置了广告代码
    const adCode = AD_CONFIG[slot];
    setHasAd(!!adCode);
    
    if (adCode) {
      // 如果有广告代码，加载Google AdSense
      try {
        (window as any).adsbygoogle = (window as any).adsbygoogle || [];
        (window as any).adsbygoogle.push({});
      } catch (err) {
        console.error('AdSense error:', err);
      }
    }
  }, [slot]);
  
  // 如果没有配置广告代码，不渲染任何内容
  if (!hasAd) {
    return null;
  }
  
  return (
    <div className={`my-8 relative overflow-hidden ${className}`}>
      {/* 流光效果 */}
      <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent animate-shimmer" />
      
      {/* 广告容器 */}
      <div className="relative bg-white/50 backdrop-blur-sm border-2 border-dashed border-slate-300 rounded-2xl p-8 text-center">
        <ins
          className="adsbygoogle"
          style={{ display: 'block' }}
          data-ad-client={AD_CONFIG[slot].split('/')[0]}
          data-ad-slot={AD_CONFIG[slot].split('/')[1]}
          data-ad-format="auto"
          data-full-width-responsive="true"
        />
        
        {/* 加载AdSense脚本 */}
        <script
          async
          src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"
        />
      </div>
      
      <style>{`
        @keyframes shimmer {
          0% { transform: translateX(-100%); }
          100% { transform: translateX(100%); }
        }
        .animate-shimmer {
          animation: shimmer 2s infinite;
        }
      `}</style>
    </div>
  );
}
```

---

### 任务 3.6: 创建 Header 和 Footer 组件

**新建文件**: `src/components/Header.tsx`

```typescript
import { useState, useEffect } from 'react';

export function Header() {
  const [scrolled, setScrolled] = useState(false);
  
  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);
  
  return (
    <header
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled
          ? 'bg-white/95 backdrop-blur-xl shadow-sm py-3'
          : 'bg-transparent py-5'
      }`}
    >
      <div className="max-w-[1400px] mx-auto px-6 flex items-center justify-between">
        <a href="/" className="flex items-center gap-2">
          <span className="text-2xl">🚀</span>
          <span className="font-display font-bold text-xl text-[#0a1b33]">
            GitHub Skill Hub
          </span>
        </a>
        
        <nav className="hidden md:flex items-center gap-8">
          <a href="/" className="text-[#64748b] hover:text-[#0a1b33] transition-colors font-medium">
            首页
          </a>
          <a href="#categories" className="text-[#64748b] hover:text-[#0a1b33] transition-colors font-medium">
            分类
          </a>
          <a href="/copyright" className="text-[#64748b] hover:text-[#0a1b33] transition-colors font-medium">
            版权声明
          </a>
        </nav>
      </div>
    </header>
  );
}
```

**新建文件**: `src/components/Footer.tsx`

```typescript
export function Footer() {
  return (
    <footer className="bg-[#0a152d] text-white py-16 mt-20">
      <div className="max-w-[1400px] mx-auto px-6 text-center">
        <div className="mb-6">
          <span className="text-3xl">🚀</span>
          <h3 className="font-display font-bold text-xl mt-2">GitHub Skill Hub</h3>
        </div>
        
        <p className="text-slate-400 mb-4">
          © 2026 GitHub Skill Hub - 开源AI工具导航
        </p>
        
        <p className="text-slate-500 text-sm mb-6">
          本站仅做GitHub开源仓库导航跳转，所有Skill资源均归原作者及开源社区所有
        </p>
        
        <p className="text-slate-400">
          侵权投诉邮箱：<a href="mailto:complaint@example.com" className="text-blue-400 hover:underline">complaint@example.com</a>
          {' | '}
          <a href="/copyright" className="text-blue-400 hover:underline">完整版权声明</a>
        </p>
      </div>
    </footer>
  );
}
```

---

## 第四阶段：页面组装

### 任务 4.1: 创建 Home 页面

**新建文件**: `src/pages/Home.tsx`

```typescript
import { useState } from 'react';
import { Hero } from '../components/Hero';
import { MarqueeLogos } from '../components/MarqueeLogos';
import { CategorySection } from '../components/CategorySection';
import { AdSpace } from '../components/AdSpace';
import { Header } from '../components/Header';
import { Footer } from '../components/Footer';
import { skills, categories } from '../data/skills';

export function Home() {
  const [searchQuery, setSearchQuery] = useState('');
  
  return (
    <div className="min-h-screen bg-[#f9fafb]">
      <Header />
      
      <main className="pt-24 pb-10">
        <div className="max-w-[1400px] mx-auto px-6">
          {/* Hero区域 */}
          <Hero />
          
          {/* Marquee Logo滚动 */}
          <MarqueeLogos />
          
          {/* 顶部广告位 */}
          <AdSpace slot="top" />
          
          {/* 分类区域 */}
          <div id="categories" className="mt-16">
            {categories.map((category) => (
              <>
                <CategorySection
                  key={category.id}
                  category={category}
                  skills={skills.filter(s => s.category === category.id)}
                />
                <AdSpace slot={`feed${categories.indexOf(category) + 1}` as any} />
              </>
            ))}
          </div>
          
          {/* 底部广告位 */}
          <AdSpace slot="bottom" />
        </div>
      </main>
      
      <Footer />
    </div>
  );
}
```

---

### 任务 4.2: 更新 App.tsx

**修改文件**: `src/App.tsx`

```typescript
import { Home } from './pages/Home';

function App() {
  return <Home />;
}

export default App;
```

---

### 任务 4.3: 更新 main.tsx

**修改文件**: `src/main.tsx`

```typescript
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

---

### 任务 4.4: 更新 index.html

**修改文件**: `index.html`

```html
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>GitHub Skill Hub - 发现优质开源AI工具</title>
    <meta name="description" content="GitHub开源AI Skill聚合导航站，精选优质GitHub AI工具、提示词模板、自动化脚本">
    <meta name="theme-color" content="#0a152d">
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

---

## 第五阶段：测试和验证

### 任务 5.1: 运行开发服务器

```bash
npm run dev
```

**预期结果**: 
- Vite开发服务器启动在 http://localhost:5173
- Hero视频正常播放
- Marquee滚动动画正常
- 分类卡片正常显示

### 任务 5.2: 构建生产版本

```bash
npm run build
```

**预期结果**:
- 构建成功，无错误
- 生成 dist/ 目录
- 所有资源正确打包

### 任务 5.3: 预览生产版本

```bash
npm run preview
```

**预期结果**:
- 本地预览生产版本
- 验证所有功能正常

---

## 第六阶段：部署准备

### 任务 6.1: 创建 README.md

**新建文件**: `README.md`

```markdown
# GitHub Skill Hub

现代化GitHub开源AI工具导航网站

## 特性

- 🎨 现代化UI设计 - React + Tailwind CSS v4
- ✨ 流畅动画 - Motion动画库
- 🎬 视频Hero背景
- 🔄 品牌Logo滚动展示
- 📱 响应式设计
- ♿ 可访问性优化
- 📢 智能广告位管理

## 快速开始

```bash
# 安装依赖
npm install

# 开发环境
npm run dev

# 构建生产版本
npm run build

# 预览生产版本
npm run preview
```

## 部署

支持 Vercel、Netlify、GitHub Pages 等平台

## 广告接入

1. 编辑 `src/components/AdSpace.tsx` 文件
2. 在 `AD_CONFIG` 对象中配置您的Google AdSense代码
3. 未配置的广告位会自动隐藏

## License

MIT
```

---

## 实施检查清单

- [ ] 项目初始化完成
- [ ] Tailwind CSS配置完成
- [ ] Hero组件开发完成
- [ ] MarqueeLogos组件开发完成
- [ ] SkillCard组件开发完成
- [ ] CategorySection组件开发完成
- [ ] AdSpace组件开发完成
- [ ] Header和Footer组件开发完成
- [ ] Home页面组装完成
- [ ] 开发环境测试通过
- [ ] 生产构建成功
- [ ] README文档创建完成

---

**计划版本**: V1.0  
**创建日期**: 2026年5月9日  
**状态**: 待执行
