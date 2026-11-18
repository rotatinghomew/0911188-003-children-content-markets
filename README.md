# 儿童内容播放概览

儿童内容版本、市场和播放时长。当前总览只按市场合计播放秒数。

样例数据均为本地合成记录，不对应真实个人、媒体、机构或交易。项目使用 Python 3.11.2 标准库，数据随项目保存，不访问外部服务。

## 使用

在项目根目录运行 `python3 -m app summary` 查看按当前基础口径生成的 JSON 总览。

## 验证

运行 `python3 -m unittest discover -s tests -v` 和 `python3 -m compileall -q app tests`。

## 结构

`data/data.json` 保存领域记录与基础汇总口径；`app/storage.py` 读取并检查数据形状；`app/analysis.py` 计算基础分组统计；`app/service.py` 组合数据读取和统计；`tests/` 验证产品入口及无效数据处理。

## 工作台

平台从当前在架内容选择上新候选。`catalog` 查某市场在架版本；同日换版时旧版结束日不含当天。`scorecard` 计入当前版本中得到许可的播放，并单列问卷邀请和回应数。`slate` 按获许可播放总时长排候选，最多列出市场预留席位数。

例如 `python3 -m app slate --key es`。`start` 区分主动选择和自动播放；`cohort` 对应问卷调查批次。问卷答案 `ballots` 只记录被问及的发行版本，回应总数则是调查批次的参与人数，并非所有回应都回答了这一项。

操作数据在 `data/workbench.json`。工作台涉及的领域代码：`catalog` 决定市场在架版本, `measurement` 筛选可用播放和问卷, `slate` 根据证据排上新候选。已有总览仍使用 `data/data.json`。
