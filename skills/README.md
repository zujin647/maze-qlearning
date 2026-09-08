# Codex Skills

本仓库公开托管的 Agent Skills，均符合常见社区技能结构：

```text
skills/<skill-name>/
|-- SKILL.md
|-- agents/openai.yaml
`-- README.md
```

## Available Skills

### defense-ppt-handbook

按 Odyphus《答辩核心手册》的八大黄金准则制作答辩、社会实践汇报、项目展示类 PPT。

- 技能目录：[defense-ppt-handbook/](defense-ppt-handbook/)
- 主要规则：视觉排版、内容逻辑、讲稿协同、交付检查
- 适用请求：答辩 PPT、社会实践汇报 PPT、项目展示 PPT

安装方式（Codex / OpenAI Skills 环境）：

```bash
python install-skill-from-github.py --repo WuHaolin318/maze-qlearning --path skills/defense-ppt-handbook
```

其他 agent 也可以直接下载整个目录，并将 `SKILL.md` 放入本平台对应的 skills 目录。
