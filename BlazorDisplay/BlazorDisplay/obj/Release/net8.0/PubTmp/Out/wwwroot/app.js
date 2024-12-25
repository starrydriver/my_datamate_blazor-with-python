<script>
    async function PickDirectory()
    {
        try
        {
            const directoryHandle = await window.showDirectoryPicker();
            return directoryHandle.name; // 返回文件夹的名称
        }
        catch (err)
        {
            console.error(err);
            return null; // 如果出错，返回 null
        }   
    }
</script>