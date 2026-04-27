#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse
import io
import os
import shutil
import sys


HELP_TEXT = u"""\
用法:
  python scripts/install_starter_kit.py [--source 目录] [--target 目录] [--overwrite] [--dry-run]
  python scripts/install_starter_kit.py --init-project 项目目录 [--project-overwrite]
  python scripts/install_starter_kit.py --target 技能目录 --init-project 项目目录 [--overwrite] [--project-overwrite]

说明:
  将 Codex 中文 starter kit 技能安装到 Codex 技能目录，并可选初始化项目级 AGENTS.md 入口文件。

参数:
  --source SOURCE   Starter kit 根目录，默认当前仓库根目录。
  --target TARGET   目标 Codex 技能目录，默认 ~/.codex/skills。
  --overwrite       覆盖目标目录中的同名技能。
  --init-project DIR
                    在指定项目根目录初始化 AGENTS.md 和最小项目骨架，让项目任务自动走项目入口规则。
  --project-overwrite
                    覆盖项目目录中已有的 AGENTS.md。
  --dry-run         只预览将要执行的动作，不实际复制文件。
  -h, --help        显示帮助并退出。
"""


def text_type():
    try:
        return unicode
    except NameError:
        return str


TEXT_TYPE = text_type()


def to_text(value):
    if isinstance(value, TEXT_TYPE):
        return value
    for encoding in ("utf-8", sys.getfilesystemencoding() or "utf-8", "mbcs", "gbk"):
        try:
            return value.decode(encoding)
        except (UnicodeDecodeError, LookupError, AttributeError):
            pass
    return value.decode("utf-8", "replace")


def normalize_path(path_value):
    return to_text(os.path.abspath(os.path.expanduser(path_value)))


def write_text(path, content):
    with io.open(path, "w", encoding="utf-8-sig") as handle:
        handle.write(to_text(content))


def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def default_target_dir():
    return os.path.join(os.path.expanduser("~"), ".codex", "skills")


def discover_skills(source_root):
    skills_dir = os.path.join(source_root, "skills")
    if not os.path.isdir(skills_dir):
        raise IOError(u"未找到 skills 目录: {0}".format(skills_dir))

    result = []
    for name in sorted(os.listdir(skills_dir)):
        child = os.path.join(skills_dir, name)
        if os.path.isdir(child) and os.path.isfile(os.path.join(child, "SKILL.md")):
            result.append(child)
    return result


def project_template_path(source_root):
    template = os.path.join(source_root, "templates", "project", "AGENTS.md")
    if not os.path.isfile(template):
        raise IOError(u"未找到项目模板文件: {0}".format(template))
    return template


def copy_skill(src, dst, overwrite):
    if os.path.exists(dst):
        if not overwrite:
            return u"已跳过"
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    return u"已安装"


def init_project_agents(template, project_root, overwrite):
    destination = os.path.join(project_root, "AGENTS.md")
    if os.path.exists(destination) and not overwrite:
        return u"已跳过"
    ensure_dir(project_root)
    shutil.copyfile(template, destination)
    return u"已初始化"


def init_project_scaffold(project_root):
    docs_v1 = os.path.join(project_root, "docs", "codex", "v1")
    for child in ("requirements", "designs", "plans", "trace"):
        folder = os.path.join(docs_v1, child)
        ensure_dir(folder)
        gitkeep = os.path.join(folder, ".gitkeep")
        if not os.path.exists(gitkeep):
            write_text(gitkeep, u"")

    status_file = os.path.join(docs_v1, "status.md")
    if not os.path.exists(status_file):
        write_text(
            status_file,
            u"# 项目状态\n\n"
            u"- 当前版本：v1\n"
            u"- 当前阶段：初始化\n"
            u"- 当前主题：待填写\n"
            u"- 说明：此文件用于记录需求、设计、计划、实现与追踪的主线状态。\n",
        )

    plans_root = os.path.join(project_root, ".codex", "plans", "main")
    ensure_dir(plans_root)
    tasks_file = os.path.join(plans_root, "TASKS.md")
    if not os.path.exists(tasks_file):
        write_text(
            tasks_file,
            u"# TASKS\n\n"
            u"- 暂无任务，请在接入首个长任务时补充。\n",
        )


def parse_args():
    if "-h" in sys.argv or "--help" in sys.argv:
        print(HELP_TEXT)
        sys.exit(0)

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--source", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    parser.add_argument("--target", default=default_target_dir())
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--init-project", default="")
    parser.add_argument("--project-overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    source_root = normalize_path(args.source)
    target_dir = normalize_path(args.target)
    init_project_dir = None
    if args.init_project:
        init_project_dir = normalize_path(args.init_project)

    try:
        skills = discover_skills(source_root)
    except IOError as exc:
        print(u"[ERROR] {0}".format(exc))
        return 1

    try:
        agents_template = project_template_path(source_root)
    except IOError as exc:
        print(u"[ERROR] {0}".format(exc))
        return 1

    if not skills:
        print(u"[ERROR] source skills 目录下未找到可安装的技能。")
        return 1

    print(u"来源目录: {0}".format(source_root))
    print(u"目标目录: {0}".format(target_dir))
    print(u"是否覆盖: {0}".format(u"是" if args.overwrite else u"否"))
    print(u"是否初始化项目: {0}".format(u"是" if init_project_dir else u"否"))
    if init_project_dir:
        print(u"项目目录: {0}".format(init_project_dir))
        print(u"是否覆盖项目规则: {0}".format(u"是" if args.project_overwrite else u"否"))
    print(u"是否仅预览: {0}".format(u"是" if args.dry_run else u"否"))
    print(u"")

    if not args.dry_run:
        ensure_dir(target_dir)

    installed = 0
    skipped = 0
    for skill_dir in skills:
        destination = os.path.join(target_dir, os.path.basename(skill_dir))
        if args.dry_run:
            if os.path.exists(destination) and args.overwrite:
                action = u"将覆盖"
            elif os.path.exists(destination):
                action = u"将跳过"
            else:
                action = u"将安装"
            print(u"- {0}: {1}".format(os.path.basename(skill_dir), action))
            continue

        status = copy_skill(skill_dir, destination, args.overwrite)
        print(u"- {0}: {1}".format(os.path.basename(skill_dir), status))
        if status == u"已安装":
            installed += 1
        else:
            skipped += 1

    project_status = u""
    if init_project_dir:
        destination = os.path.join(init_project_dir, "AGENTS.md")
        if args.dry_run:
            if os.path.exists(destination):
                project_status = u"将覆盖" if args.project_overwrite else u"将跳过"
            else:
                project_status = u"将初始化"
            print(u"- 项目入口 AGENTS.md: {0}".format(project_status))
        else:
            project_status = init_project_agents(
                agents_template,
                init_project_dir,
                args.project_overwrite,
            )
            init_project_scaffold(init_project_dir)
            print(u"- 项目入口 AGENTS.md: {0}".format(project_status))
            print(u"- 项目文档骨架: 已初始化")

    if args.dry_run:
        print(u"\n预览完成。")
        return 0

    print(u"\n已安装: {0}".format(installed))
    print(u"已跳过: {0}".format(skipped))
    if init_project_dir:
        print(u"项目入口: {0}".format(project_status))
    print(u"安装完成。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
