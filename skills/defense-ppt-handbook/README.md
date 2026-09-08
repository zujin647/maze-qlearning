# defense-ppt-handbook

Codex / Agent Skill，用于按 Odyphus《答辩核心手册》的八大黄金准则制作答辩类 PPT。

## What It Does

- 封面、侧边栏导航、超大数字、模块化版式的视觉规范
- 单页 50 字、递进逻辑链、总结复盘页的内容规范
- PPT 与讲稿逐页对应的表达与交付检查

## Files

- `SKILL.md`：技能主指令
- `agents/openai.yaml`：OpenAI / Codex UI 元数据

## Install

Codex / OpenAI Skills 环境：

```bash
python install-skill-from-github.py --repo WuHaolin318/maze-qlearning --path skills/defense-ppt-handbook
```

也可以直接下载：

- `SKILL.md`：https://raw.githubusercontent.com/WuHaolin318/maze-qlearning/main/skills/defense-ppt-handbook/SKILL.md
- `agents/openai.yaml`：https://raw.githubusercontent.com/WuHaolin318/maze-qlearning/main/skills/defense-ppt-handbook/agents/openai.yaml

下载后放到：

```text
~/.codex/skills/defense-ppt-handbook/SKILL.md
~/.codex/skills/defense-ppt-handbook/agents/openai.yaml
```

新对话或刷新 Codex 会话后生效。
