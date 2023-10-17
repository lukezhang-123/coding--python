# 安装pywin32扩展后，报错 ImportError: DLL load failed

win32clipboard 是pywin32包内

处理：

1. 卸载 pypiwin32

    ```shell
    pip uninstall pypiwin32
    ```

2. 重新安装pywin32
    ```shell
    pip uninstall pywin32
    pip install pywin32
    ```
3. 如果还不行，试下手动执行后置脚本, 以管理员身份运行cmd，执行，主要复制 `%LOCALAPPDATA%\Programs\Python\Python37\Lib\site-packages\pywin32_system32\pywintypes37.dll` 到c盘system32系统目录
    ```shell
    cd %LOCALAPPDATA%\Programs\Python\Python37
    .\Scripts\pywin32_postinstall.py -install
    ```
4. 验证问题解决, 手动执行import不报错
    ```shell
    python
    import win32clipboard
    ```

参考：[python - How to fix &quot;ImportError: DLL load failed&quot; while importing win32api - Stack Overflow](https://stackoverflow.com/a/58613735/9868643)