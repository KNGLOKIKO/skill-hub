import re
import os

base = os.path.join(os.path.dirname(__file__), '..', 'index.html')
with open(base, 'r', encoding='utf-8') as f:
    html = f.read()

# Specific zhDesc fixes for every untranslated entry found
zh_fixes = {
    "figures4papers": "用于在顶级AI会议上生成高质量出版物的Python脚本",
    "Unity-Skills": "专为Unity开发的AI自动化技能集合",
    "ProjectAlice": "ProjectAlice开源语音助手的技能系统",
    "openclaw-backup": "OpenClaw技能备份工具",
    "MindOS": "MindOS个性化AI代理技能平台",
    "clawgod": "ClawGod是官方Claude Code的运行时补丁，提供自动更新兼容的能力增强工具",
    "skillgrade": "AI驱动的技能评估和分级工具，帮助衡量和改善技能水平",
    "skill.color-expert": "面向AI代理的色彩科学和专业配色技能",
    "api2cli": "API转命令行工具，一键将REST API转换为可用的CLI工具",
    "iFly-Skills": "讯飞星火Agent技能注册中心，支持企业级RBAC和审计日志",
    "Tech-Doc-Style-Chinese": "技术文档中文风格指南和写作规范",
    "open-webui-plugins": "Open WebUI插件集合，扩展AI交互界面功能",
    "skillbridge": "技能桥接工具，连接不同AI平台和框架的技能生态",
    "ComfyUI_Skills_OpenClaw": "OpenClaw代理的ComfyUI技能集合，支持AI图像生成工作流",
    "debug-agent": "AI调试代理技能，自动识别和修复代码中的错误",
    "SkillZero": "AI代理零基础入门技能包",
    "LycheeMem": "荔枝记忆——AI代理的长期记忆管理系统",
    "PyEditorial": "AI驱动的Python文章编辑和内容创作工具",
    "skill-flow": "可视化技能流编辑器，用于构建AI代理工作流",
    "skills": "社区贡献的Caido AI技能集合",
    "patent-disclosure-skill": "AI驱动的专利交底书自动撰写技能，可生成结构化的专利申请文档",
    "humanacraft": "HumanaCraft AI代理角色和人格技能生成器",
    "MGM-Ability": "暂无描述",
    "da-vinci-code": "达芬奇密码——AI代理的创意编码和问题解决技能",
    "mini-program": "微信小程序开发技能包",
    "vibe-website-check": "AI驱动的网站视觉一致性检查技能",
    "magick-skills": "Magick AI代理技能和工具集合",
    "ecs-flow-fields": "ECS实体组件系统的流场技能框架",
    "claude-skill-converter": "Claude Code技能格式转换工具",
    "sabrina-assistant": "Sabrina AI个人助手技能系统",
    "code-scanner": "AI驱动的代码安全扫描和漏洞检测技能",
    "git-prompt": "Git命令行提示信息优化技能",
    "knowledge": "AI代理知识管理和检索增强生成技能包",
    "Knowledge": "AI代理知识管理和检索增强生成技能包",
    "openclaw-skill-imessage": "OpenClaw代理的iMessage集成技能",
    "hackernews-skill": "HackerNews内容抓取和智能摘要技能",
    "openclaw-zapier-mcp-skill": "OpenClaw代理的Zapier MCP集成技能，连接5000+应用",
    "firenvim": "Firenvim浏览器嵌入技能，在浏览器中使用Neovim编辑器",
    "SKILL_Tools": "Cadence SKILL/SKILL++开发工具集，包含单元测试框架",
    "xcode-claw": "Xcode代理开发工具，帮助AI代理进行iOS/macOS开发",
    "skill-library": "AI代理技能库管理系统",
    "android-h1": "Android和iOS平台漏洞赏金与安全研究技能，面向白帽黑客",
    "skill-prompt": "AI代理提示词工程和优化技能",
    "Boss Skill": "Boss直聘AI代理技能——智能职位搜索和简历匹配",
    "Claude-Code-Scaffolding-Skill": "Claude Code项目脚手架技能，快速创建新项目模板",
    "code-alchemist": "从Git提交历史中提取开发者编码风格和架构偏好的Claude Code技能",
    "floodsung-skill": "训练于Flood Sung知乎语料库的Claude Code技能，152篇文章+178条想法+254个回答",
    "Parent-Helper": "Claude Code家庭助手技能：每周简报、餐饮规划、多店购物优化",
    "openclaw-alpaca-trading-skill": "通过Alpaca交易API进行股票、ETF、期权和加密货币交易的OpenClaw技能",
    "LintConfig": "AI技能，根据编码规范自动配置代码检查工具并强制执行代码质量标准",
    "capek": "Capek自托管对话式AI平台",
    "gVal": "用于评估地理空间数据集的Python框架，通过比较候选地图和基准地图计算一致性指标",
    "frontend-distill": "将网站蒸馏为AI可读的前端系统：视觉设计、布局结构和响应式行为",
    "convert-claude-to-codex-skill": "自动将Claude技能转换为Codex技能，支持搜索、获取、转换和验证",
    "modeldriveprotocol": "模型驱动协议(MDP)：将运行时本地能力转化为MCP可访问能力",
    "ghostty-vibe-coding-stack": "基于Ghostty的编码技术栈，包含Fish、yazi、lazygit、Neovim、fzf、zoxide和atuin",
    "alexa-flask-FSM": "使用Flask、flask-ask和状态机构建Alexa对话处理的示例",
    "quarkus-skill": "Quarkus平台参考文档和AI编程助手可安装技能包",
    "md-wechat": "微信Markdown编辑器，支持OpenClaw和Mermaid图表",
    "vibe-writing": "基于Wiki方法论的AI协作小说写作方法论",
    "faster-whisper": "基于faster-whisper的音频转录OpenClaw技能",
    "t-trading": "EMA均线策略加提示词驱动的AI交易系统",
    "chitchatjs": "轻松构建Alexa语音应用",
    "skill-kotlin-jni-qt": "Kotlin、JNI和Qt结合使用的示例",
    "smart-short-video": "AI驱动的TikTok/Reels/Shorts短视频创作工具",
    "code-smells-skill": "120+命名代码坏味的检测技能，覆盖C、C++、C#、Java、Python、Go、Rust、JavaScript、TypeScript",
    "daisyLayoutAssist": "Cadence Virtuoso原理图与版图映射工具，简化版图设计流程",
    "zotero-obsidian-skill": "Claude Code与Zotero、Obsidian、Markdown的集成技能",
    "pwa-review-skill": "160项PWA审计技能，超越Lighthouse，支持iOS兼容性、安全区域和触摸事件",
    "orbit-prompt": "将AI请求转化为清晰、可控、可验证提示词的Claude Code技能",
    "clean-architecture-skills": "基于整洁架构原则审查和设计代码的Claude Code技能",
    "skill-bill": "AI代理技能治理系统，支持清单驱动路由、验证器背书合同和本地优先遥测",
    "cast-subagents": "Codex子代理编排技能，自动识别可委派任务并推荐角色阵容",
    "x-research-but-cheaper": "X/Twitter研究和监控代理，支持OpenClaw和Claude Code",
    "c4-diagram-skill": "遵循Simon Brown C4模型标准的容器图生成的Claude Code技能",
    "wenyanwen": "让AI使用文言文回复的技能",
    "Humanizer-zh": "AI写作痕迹检测工具，中文版v2.5.1",
    "erpnext-skill": "包含Frappe框架和ERPNext v15 API参考的Claude Code技能",
    "SKILL-adapter": "将SKILL路由和提示增强集成到LLM和代理应用的低侵入适配器",
    "dayif-portfolio": "基于Next.js和Tailwind CSS的个人作品集展示网站",
    "job-hunter-skill": "Boss直聘平台智能职位搜索的Claude Code技能",
    "website-design-systems-mcp": "从任意网站提取完整设计系统并生成AI可读的skill.md文件",
    "amazon-visual-architect-skill": "AI驱动的视觉架构设计提示工具",
    "effect-claudecode": "Effect v4与Claude Code插件原语的绑定：hooks、技能、设置、MCP服务器",
    "wechat-to-xiaohongshu": "微信公众号文章转小红书笔记格式转换器",
    "claude-skill-stitch-design": "通过MCP自动生成Google Stitch UI原型的Claude Code技能",
    "groundtruth": "Claude Code完成声明门控——没有证据就不让AI代理说完成了",
    "hyrox-training-skill": "HYROX健身训练计划和技能追踪系统",
    "learn-ai": "前端AI学习路线图",
    "html2elementor": "将HTML+CSS转换为WordPress Elementor JSON的技能",
    "registerskill": "通用skill.md创建器，AI代理可注册和操作任何网站",
    "data-engineer-resume-copilot": "数据工程师简历和职位描述优化技能",
    "blog": "关于专业领域的思考和分享",
    "t2i-skillguard": "AI技能文件安全扫描器，检测SKILL.md和代码中的高风险模式",
    "Alexa-Skill-Test-Autoescuela": "西班牙驾考理论测试的Amazon Alexa技能",
    "connectkgp": "KGP学生一站式信息平台，从学术到就业的全方位支持",
    "pytrio-skill": "PyTRIO SDK的Claude Code技能，教AI编程代理编写远程LLM训练和推理代码",
    "trent-openclaw-security-assessment": "OpenClaw环境免费安全评估，扫描网关配置、工具权限、MCP服务器和插件",
    "structai": "StructAI提供LLM交互工具包：结构化输出、上下文管理和并行执行",
    "alpaca-trading-skill": "通过Alpaca交易API进行股票、ETF、期权和加密货币的命令行交易技能",
    "visual-explainer-extension": "将Nico Bailon的代理技能仓库重构为Gemini CLI扩展",
    "nano-banana-prompting-skill": "将自然语言转化为Gemini图像生成优化提示词的技能",
    "quark-download-skill": "通过PanSou API和本地夸克桌面APP搜索、验证和保存云盘资源的技能",
    "engineering": "NICE Digital公司的工程方法论",
    "skill-expression-game-analysis": "使用强化学习客观量化游戏中技能表现的方法",
    "skill-memory-bank": "通用长期项目记忆和开发工具包，支持Claude Code、Cursor、Windsurf等AI工具",
    "oss-ai-skills": "开源项目skill.md存档，用于贡献和使用开源框架和插件",
    "llm-wiki-pm": "基于Karpathy LLM Wiki模式的产品管理知识库Claude Code技能",
    "ACI": "ACI(代理-计算机接口)开放标准，将任何应用转化为结构化、代理可操作的接口",
    "HecO": "HarmonyOS/鸿蒙系统的AI代理技能",
    "clawd-plugin-vault": "将本地目录转化为Clawdbot结构化知识库，支持快速语义搜索和Markdown",
    "x-api-skill": "让AI代理代表你使用X(Twitter)发布、回复、搜索、私信和书签",
    "gitlab-skill": "提供GitLab集成的AI代理技能：获取议题和合并请求、生成摘要、结构化分析",
    "vibe-code-health-check": "Claude Code技能：从A到F评分代码库的健康度，提供通俗易懂的修复建议",
    "scrcpy-claw": "Lobster Android助手——通过ADB和scrcpy实现AI驱动的Android设备控制",
    "ai-daily-digest": "OpenClaw技能：来自92个Karpathy精选博客的每日AI/技术摘要",
    "site-navigator": "OpenClaw直接链接访问和困难站点导航技能",
    "hyperframes-motion": "HyperFrames视频生成的After Effects风格动态图形技能",
    "prolexa": "Amazon Alexa的Prolog逻辑编程集成",
    "openclaw-persona-forge": "生成具有身份张力、边界规则和AI生成头像的龙虾角色的OpenClaw技能",
}

# Apply fixes by finding and replacing zhDesc for each entry
count = 0
for name, new_zh in zh_fixes.items():
    # Escape the new_zh for JS context
    new_zh_escaped = new_zh.replace('\\', '\\\\').replace("'", "\\'")
    
    # Find the entry by name and replace zhDesc
    # Use a pattern that matches: name: 'name', ... zhDesc: 'old_value', ... tags: [...]
    pattern = re.compile(
        r"(\s+{ name: '" + re.escape(name) + r"', url: '[^']+', stars: \d+, language: '[^']*', forks: \d+, enDesc: '(?:[^'\\]|\\.)*', zhDesc: ')((?:[^'\\]|\\.)*)(',\s*tags: \[)",
        re.DOTALL
    )
    
    def make_replacement(m, new_zh_e=new_zh_escaped):
        return m.group(1) + new_zh_e + m.group(3)
    
    new_html, n = pattern.subn(make_replacement, html)
    if n > 0:
        count += n
        html = new_html
    else:
        # Try a more flexible regex
        pattern2 = re.compile(
            r"(\s+{ name: '" + re.escape(name) + r"', url: '[^']+', stars: \d+, language: '[^']*', forks: \d+, enDesc: ')(?:(?:[^'\\]|\\.)*)(',\s*zhDesc: ')(?:(?:[^'\\]|\\.)*)(',\s*tags: \[)",
            re.DOTALL
        )
        def make_replacement2(m, new_zh_e=new_zh_escaped):
            return m.group(1) + m.group(2) + new_zh_e + m.group(3)
        new_html, n2 = pattern2.subn(make_replacement2, html)
        if n2 > 0:
            count += n2
            html = new_html
        else:
            print(f"  NOT FOUND: {name}")

print(f"Fixed {count} zhDesc entries")

with open(base, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")