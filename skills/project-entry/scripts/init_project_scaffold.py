#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import io
import os
import sys


def text_type():
    try:
        return unicode
    except NameError:
        return str


TEXT_TYPE = text_type()


def to_text(value):
    if isinstance(value, TEXT_TYPE):
        return value
    return value.decode("utf-8")


def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def write_text(path, content):
    ensure_dir(os.path.dirname(path))
    with io.open(path, "w", encoding="utf-8-sig") as handle:
        handle.write(to_text(content))


def ensure_file(path, content):
    if os.path.exists(path):
        return u"已存在"
    write_text(path, content)
    return u"已创建"


def ensure_gitkeep(folder):
    ensure_dir(folder)
    gitkeep = os.path.join(folder, ".gitkeep")
    if os.path.exists(gitkeep):
        return u"已存在"
    write_text(gitkeep, u"")
    return u"已创建"


def init_project(project_root):
    docs_v1 = os.path.join(project_root, "docs", "codex", "v1")
    logs = []

    for name in ("requirements", "designs", "plans", "trace"):
        folder = os.path.join(docs_v1, name)
        status = ensure_gitkeep(folder)
        logs.append(u"{0}: {1}".format(os.path.join(folder, ".gitkeep"), status))

    status_md = os.path.join(docs_v1, "status.md")
    status = ensure_file(
        status_md,
        u"# 项目状态\n\n"
        u"- 当前版本：v1\n"
        u"- 当前阶段：初始化\n"
        u"- 当前主题：待填写\n"
        u"- 说明：此文件用于记录需求、设计、计划、实现与追踪的主线状态。\n",
    )
    logs.append(u"{0}: {1}".format(status_md, status))

    tasks_md = os.path.join(project_root, ".codex", "plans", "main", "TASKS.md")
    status = ensure_file(
        tasks_md,
        u"# TASKS\n\n"
        u"- 暂无任务，请在接入首个长任务时补充。\n",
    )
    logs.append(u"{0}: {1}".format(tasks_md, status))
    return logs


def main():
    if len(sys.argv) > 1:
        project_root = os.path.abspath(sys.argv[1])
    else:
        project_root = os.path.abspath(os.getcwd())

    print(u"项目目录: {0}".format(project_root))
    for item in init_project(project_root):
        print(u"- {0}".format(item))
    print(u"项目骨架初始化完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
