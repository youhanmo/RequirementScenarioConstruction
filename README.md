# RequirementScenarioConstruction

# 版本记录

- 1.0
  - 创建该项目，将现有的文件上传
- 1.1
  - 增加‘bridge’的描述
  - 修复了在一定情况下signplate 被识别成geograph的问题
- 1.2
  - 增加‘tunnel’的描述
  - 增加了一些变量以应对识别bridge和tunnel的情况，正在进行中
- 1.3
  - tunnel和bridge的识别已经可以使用了
  - 加了很多限制和实体识别的条件，并且对于不能搭建场景的句子信息有了提示
  - 使用CRF分词进行实体识别，取代了标准方法