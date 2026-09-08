#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Self-contained installer for the Codex skill: defense-ppt-handbook

How to use this file:
1. Run it directly with Python 3:
       python defense-ppt-handbook-installer.py
   or specify a different skill root:
       python defense-ppt-handbook-installer.py --dest C:/Users/you/.codex/skills

2. If you are an AI agent that cannot execute code but can write files:
   create the two files below at these locations:
       <skill-root>/defense-ppt-handbook/SKILL.md
       <skill-root>/defense-ppt-handbook/agents/openai.yaml
   where <skill-root> is $CODEX_HOME/skills, or ~/.codex/skills when CODEX_HOME
   is not set. Do not paraphrase or compress the instructions.

After installation, the skill is discovered in a new or refreshed Codex task.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

SKILL_NAME = "defense-ppt-handbook"

SKILL_MD = """---
name: defense-ppt-handbook
description: "按 Odyphus《答辩核心手册》的八大黄金准则制作或修改答辩、社会实践汇报、项目展示类 PPT；当用户要求制作这类演示文稿或指定使用该风格时启用。"
---

# 答辩 PPT 制作手册

本技能封装自用户提供的《答辩核心手册》。原始场景是 2 分钟社会实践答辩，评委为年轻老师和学长学姐；每次制作前先确认场合、时长、观众与核心成果，再按实际场景调整。手册要求未来制作中严格遵守以下规则。

## 工作顺序

1. 先产出整体逻辑方案，再生成 PPT 分页内容和配套讲稿；PPT 与讲稿逐页对应，反复修改到内容一致。
2. 内容定稿后再处理视觉：确定全屏背景与 3 色以内主题色，再统一封面、正文、总结页的版式。
3. 若交付 PPT 文件，按 16:9 制作；导出 PPTX 时复查字体、排版和放映效果，必要时同时提供 PDF 作为可靠版本。
4. 页面只承载精炼信息，讲稿的长句、证据细节和口头表达留在讲稿与排练中。

## 视觉与排版法则

1. 封面大片化：不要使用模板白底黑字；用契合主题、铺满全屏的高级背景图，并在图与文字之间加一层半透明暗色或毛玻璃蒙版，让封面文字醒目且具有发布会级质感。
2. 学术侧边栏导航：不做独立目录页；每页左侧设固定宽度导航栏，用框线分隔目录板块，当前板块以主题色高亮反白，让观众随时知道讲到哪一部分。
3. 数据巨物化：将 62%、200+、1+1 这类高光成果提取为 80-100pt 的超大数字，配小字号说明，用大小反差制造一眼可见的视觉重点。
4. 模块化排版：坚持字不如表、表不如图；图表和实证截图保持高清、裁剪得当，用卡片式色块归类内容，布局横平竖直，禁用无意义的弹跳、飞入等动画。
5. 全局高度一致：全篇主色不超过 3 种；各页配色、字体、标题位置、侧边栏宽度尽量像素级统一，形成完整视觉识别系统。

## 内容与逻辑法则

6. 单页 50 字铁律：PPT 是视觉辅助而不是提词器；单页文字尽量不超过 50 字，删掉冗长定语和修饰词，只留动宾式短句，长篇内容放进讲稿。
7. 逻辑链条递进：不用时间线流水账；按“痛点把脉 -> 硬核解法 -> 量化成果 -> 长效机制”编排，让每页环环相扣并服务同一主线。
8. 虎头豹尾收束：结尾不用单一“谢谢聆听”页；改用“答辩总结与致谢页”，用流程图复盘完整逻辑链条，让观众在提问与打分时仍看到项目价值。

## PPT 配套表达要点

- 页面语言采用短平快的子弹句；可适度使用对仗、押韵增强表现力，但不得影响信息准确。
- 讲稿与页面一一对应；讲到超大数字、硬核证据等亮点时，配合停顿和自然手势引导观众看屏幕。
- PPT 是配角、答辩人是主角；页面只帮助理清思路和快速理解，讲解者应自信表达，不背稿、不读稿。
- 动画只在推进逻辑时使用，用它展示步骤或因果关系，不做装饰性动效。

## 交付前检查

- 封面为全屏背景图加蒙版，不是模板首页。
- 内页有侧边栏导航，当前板块高亮。
- 高光成果以超大数字呈现，且版面不超过 3 种主色。
- 单页文字不超过 50 字，文字无溢出、重叠或裁切。
- 页面为 16:9，图表与色块对齐一致，版式横平竖直。
- 末页是总结复盘页而非单纯致谢页。
- PPT 分页与讲稿逐页对应。
"""

OPENAI_YAML = """interface:
  display_name: "Defense Ppt Handbook"
  short_description: "Help with Defense Ppt Handbook tasks"
"""


def default_skill_root() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home) / "skills"
    return Path.home() / ".codex" / "skills"


def main() -> None:
    parser = argparse.ArgumentParser(description="Install the defense-ppt-handbook Codex skill.")
    parser.add_argument(
        "--dest",
        help='Skill root directory. Defaults to $CODEX_HOME/skills or ~/.codex/skills.',
    )
    args = parser.parse_args()

    skill_root = Path(args.dest) if args.dest else default_skill_root()
    dest = skill_root / SKILL_NAME
    (dest / "agents").mkdir(parents=True, exist_ok=True)
    (dest / "SKILL.md").write_text(SKILL_MD, encoding="utf-8")
    (dest / "agents" / "openai.yaml").write_text(OPENAI_YAML, encoding="utf-8")

    print(f"Installed skill to: {dest}")
    print("It becomes available in the next new or refreshed Codex task.")


if __name__ == "__main__":
    main()
