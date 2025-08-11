## 环境说明
- 本框架是Blender Addon开发的最小单元。完全面向Blender开发新手，只需有python语言基础，即可通过该插件的框架，快速入门Blender插件开发。
- 推荐开发版本：windows + blender 4.27 LTS
- BlenderAPI自动补全, 推荐使用虚拟环境，相关package参考：requirements.txt
- 开发过程中，推荐使用 Debug 模式启动，参考：https://blog.csdn.net/qq_44874004/article/details/130649228
- 目前暂不支持热更新，需要 Ctrl Shift P，重新加载脚本 Blender:Reload Addons
- Debug模式：VsCode + Vscode插件Blender Development(Jacques Lucke)
- Load 插件，即可在Blender 侧边栏看到新的面板
  - ![addon_content.png](imgs/addon_content.png)
- 后续可以新增面板，修改属性，断点调试，将会十分方便。